# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:22:41 2023

@author: Jeyakumar Kasi
"""

import os
import atexit
from pytz import utc
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

from config import CRONConfig
from common import capri_logger
from exception import CapriTechApiException, ILOSException, ILOSDiagnoCode



class Scheduler:
    def __init__(self):
        self.jobs = []
        self.scheduler = None
        self.jobs_dir = 'crons/jobs'
        self.executors = {
            'default': ThreadPoolExecutor(20),
            'processpool': ProcessPoolExecutor(5)
        }
        self.jobstores = {
            'default': SQLAlchemyJobStore(
                url='sqlite:///cron_jobs.sqlite'
            )
        }
        self.job_defaults = {
            'coalesce': False,
            'max_instances': 3
        }


    def kill(self):
        # Kill all the Jobs
        for job_id in self.jobs:
            try:
                capri_logger.log(e=f'Stopping the Job <{job_id}>...', method='CRON', name='KILL_JOBS')
                self.scheduler.remove_job(job_id)
            except Exception as e:
                message = f"Error: Unable to stop the <{job_id}> job. Message: {str(e)}"
                print(message); capri_logger.log(e=message, method='CRON', name='KILL_JOBS')

        # Stop the CRON.
        self.scheduler.shutdown()


    def create(self, service_name, job_name, interval=1, interval_type=None, *args, **kwargs):
        if job_name is None:
            raise CapriTechApiException(ILOSException.CRON_CONSTRAINT_NOT_SATISFIED, ILOSDiagnoCode.LOS10102)

        # Search the Service under "Jobs" folder.
        jobs_dir = self.jobs_dir.replace('\\', '/').rstrip('/')
        service_filepath = os.path.join(os.path.abspath(jobs_dir), str(service_name) + '.py')  
        if service_name is None or not os.path.isfile(service_filepath):
            message = f'CRON Service: {service_name} <{service_filepath}> - not found.'
            print(message); capri_logger.log(e=message, method='CRON', name='CREATE_JOB')
            raise CapriTechApiException(ILOSException.CRON_JOB_NOT_FOUND, ILOSDiagnoCode.LOS10101)

        if self.scheduler is None:
            self.scheduler = BlockingScheduler(
                jobstores=self.jobstores,
                executors=self.executors,
                job_defaults = self.job_defaults,
                timezone=utc
            )

        try:
            # Call the Job
            _id = f'{service_name}_{job_name}'
            kwargs[interval_type] = interval
            module_path = jobs_dir.replace('/', '.').lstrip('..' or '.')
            module_path = f'{module_path}.{service_name}:{job_name}'
            self.scheduler.add_job(module_path, 'interval', id=_id, **kwargs)

            # Push the Job ID
            self.jobs.append(_id)

        except Exception as e:
            message = f'CRON Service: {service_name}, Error Message: {str(e)}'
            print(message); capri_logger.log(e=message, method='CRON', name='CREATE_JOB')
            raise CapriTechApiException(ILOSException.CRON_UNKNOWN_EXCEPTION, ILOSDiagnoCode.LOS10100)
        return self.scheduler


    def run(self):
        message = 'Started the CRON Service...'; 
        print(message); capri_logger.log(e=message, method='CRON', name='RUN')

        # Start the Jobs.
        self.scheduler.start()


if __name__ == '__main__':
    scheduler = Scheduler()

    # Regsiter the function to clean up all the jobs at exit.
    atexit.register(scheduler.kill)

    # Add the "Hold Documents" Job (Every 5mins)
    scheduler.create(service_name='lead', job_name='hold_doc', **CRONConfig.HOLD_DOC_TRIGGER)

    # Add the second job here...
    # ....

    # Start the Cron
    scheduler.run()