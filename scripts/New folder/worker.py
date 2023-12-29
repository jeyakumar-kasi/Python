# -*- coding: utf-8 -*-
"""
Created on Fri May 19 10:25:13 2023

@author: JeyakumarKasi
"""


import multiprocessing
from config import statuses, LIMIT
from math import ceil
from concurrent.futures import as_completed
from concurrent.futures import ThreadPoolExecutor


from db import execute


tbl_name = 'public.tbl_acquisition_partner'
tbl_name2 = 'public.tbl_acquisition_partner_reactivation_config'
def initiated(_id, offset, limit):
    q = f"SELECT id, partner_name FROM {tbl_name} LIMIT {limit} OFFSET {offset}"
    res = execute(q).fetchall()
    for row in res:
        partner_name = row["partner_name"]
        print(f"{_id}: {row['id']:.<30} {partner_name}")
    return res
    
        
def expired(_id, offset, limit):
    q = f"SELECT id, fk_acquisition_partner_id FROM {tbl_name2} LIMIT {limit} OFFSET {offset}"
    res = execute(q).fetchall()
    for row in res:
        print(f"{_id}: {row['id']:.<30} {row['fk_acquisition_partner_id']}")
    return res
    

def scheduler(pid, offset, limit=None, n_workers=None, waiters_list=None):
    waiters_list = waiters_list or {}
    n_workers= n_workers or len(statuses)
    sub_offset = offset
    sub_limit = limit or ceil(LIMIT / n_workers)
    print(f'{pid}: Offset: {sub_offset} Sub Limit: {sub_limit} Scheduling...')
    if len(statuses) > 0:
        with ThreadPoolExecutor(max_workers=n_workers) as executor:
            for idx, status in enumerate(statuses, 1):
                _id = f'{pid}_{idx}'
                args = (_id, sub_offset, sub_limit)
                if status == 'Initiated':
                    waiters_list[status] = executor.submit(initiated, *args)
                elif status == 'Expired':
                    waiters_list[status] = executor.submit(expired, *args)
            
            if len(waiters_list) > 0:
                
                # try:
                waiter_statuses = list(waiters_list.keys())
                for idx, waiter in enumerate(as_completed(waiters_list.values())):
                    status = waiter_statuses[idx]
                    if not waiter.result():
                        # No results found, remove from the list.
                        # print(f'{_id}: NO RESULTS FOUND. Removing {status}...')
                        statuses.remove(status)
                    else:
                        # print(waiter.result())
                        
                        # @todo: Write into CSV file
                        
                        # Initiate for next offset
                        sub_offset += sub_limit
                        return scheduler(pid, offset=sub_offset, limit=sub_limit, n_workers=1, waiters_list=waiters_list)
                        
                    #print(f'Completed: {status} Offset: {offset} To: {offset+limit}')
                return True
                # except Exception as e:
                #     print(f'Error is occured.')
    return False


def run(params):
    return multiprocessing.Process(target=scheduler, args=params)