# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 18:10:26 2023

@author: Jeyakumar Kasi
"""

from fastapi import Request
from dao import LeadDao
from config import (
    CRONConfig, 
    EPOCH_24H_TIME_INTERVAL, 
    get_current_epoch_time, 
    LeadStatusEnum, 
    LeadSubStatusEnum,
    LegalStageEnum
)
from common import capri_logger
from exception import CapriTechApiException, ILOSException, ILOSDiagnoCode


# Create the database instances.
leadDao = LeadDao()


def hold_doc():
    """
    Job: Collect all the leads where Query Raised older than 'n' days.
    """
    args = {}
    message = 'Running "HOLD_DOC" job...'
    print(message); capri_logger.log(e=message, method='CRON', name='HOLD_DOC_JOB')

    # Filter: is Deleted?
    args['is_deleted'] = False

    # Filter: Query is opened?
    args['tat.open_query'] = True

    # Filter: Check whether lead status?
    args['lead_status'] = LeadStatusEnum.CREDIT_RECOMMENDATION
    args['lead_sub_status'] = LeadSubStatusEnum.PD_COMPLETED
    
    # Filter: Not already in "Negative" state or "Rejected"
    args['legal_stage'] = {
        '$nin': [LegalStageEnum.NEGATIVE, LegalStageEnum.REJECTED]
    }

    updated_ids = []
    current_time = get_current_epoch_time()
    hold_doc_expire_threshold_time = EPOCH_24H_TIME_INTERVAL * int(CRONConfig.HOLD_DOC_EXPIRE_DAYS) 
    hold_doc_reject_threshold_time = EPOCH_24H_TIME_INTERVAL * int(CRONConfig.HOLD_DOC_REJECT_DAYS)
    cursor = leadDao.find_by_params(Request, **args)
    for item in cursor:
        data = {}
        _id = str(item.get('_id'))
        queries = item.get('queries') or []

        # Filter the Queries which are not resolved yet.
        unresolved_queries = [q for q in queries if not q.get('resolved_at')]
        if unresolved_queries:
            for query in unresolved_queries:
                # Check for last activity time
                last_activity_at = query.get('rm_reply_at') or query.get('created_at')

                if not last_activity_at:
                    # Log the warning message.
                    message = f'{_id} - Failed to check the last activity time by the CRON service.'
                    print(message); capri_logger.log(e=message, method='CRON', name='HOLD_DOC_JOB')
                    continue

                last_activity_time = int(last_activity_at)
                inactive_time = current_time - last_activity_time
                if inactive_time > hold_doc_reject_threshold_time:
                    # Mark this Lead as "Rejected/deleted" since sales team has to re-login the file.
                    # data['is_deleted'] = True
                    data['legal_stage'] = LegalStageEnum.REJECTED                
                    data['lead_stage'] = LegalStageEnum.QUERY_NOT_RESOLVED
                    
                elif item.get('legal_stage') != LegalStageEnum.ON_HOLD:
                    # If not already 'On HOLD' then only check for other things.
                    if inactive_time > hold_doc_expire_threshold_time:
                        # Mark this Lead under "Hold"
                        data['legal_stage'] = LegalStageEnum.ON_HOLD                
                        data['lead_stage'] = LegalStageEnum.HOLD_DOC_PENDING
                    else:
                        # @todo:
                        # Check If there is a response from sales team then 
                        # it should be notified to the Legal Coordinator here.
                        pass

        if data:
            # Update the basic things
            data['updated_on'] = current_time
            data['updated_by'] = f'{CRONConfig.UPDATED_BY_PREFIX}HOLD_DOC'

            try:
                 # Update the Lead
                 leadDao.update_object_by_id(_id, data)
                 updated_ids.append(_id)
            except Exception as e:
                message = f'{_id} is failed to update by the CRON service. Error Message: {str(e)}'
                print(message); capri_logger.log(e=message, method='CRON', name='HOLD_DOC_JOB')
                raise CapriTechApiException(ILOSException.CRON_UNKNOWN_EXCEPTION, ILOSDiagnoCode.LOS10100)


    # Returns the list of "_id" got updated. 
    message = f'Total: {len(updated_ids)}, Updated IDs: {updated_ids}'
    print(message); capri_logger.log(e=message, method='CRON', name='HOLD_DOC_JOB')
    return updated_ids