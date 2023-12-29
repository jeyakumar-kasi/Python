# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 10:52:45 2022

@author: <jeyakumar.k@datafoundry.ai>
"""
import datetime as dt


import re
def get_var_name(name):
    return re.sub("[\s]+", "_", re.search("[\w\s]+", name.strip())[0]).lower()

# q = f"SELECT partner_name FROM {tbl_name}"
# res = execute(q).fetchall()

# for row in res:
#     partner_name = row["partner_name"]
    # print(f"{partner_name:.<30} {get_var_name(partner_name)}")

    # q = f"UPDATE {tbl_name} SET partner_slug_name=%s WHERE partner_name=%s;"
    # execute(q, params=(get_var_name(partner_name), partner_name))

def get_datetime():
    return str(dt.datetime.now().strftime('%H:%M:%S'))

# -------------------------------------

# Config
MAX_ALLOWED_USAGE = 60 # %


import multiprocessing
from math import ceil

from concurrent.futures import as_completed
from concurrent.futures import ThreadPoolExecutor
from worker import run
from config import statuses, LIMIT

cpu_count = multiprocessing.cpu_count()
max_cpu_count = ceil((cpu_count/100) * MAX_ALLOWED_USAGE)
print(f'Total: {cpu_count}, Allocated: {max_cpu_count}')

processes = []

def init(process_count):
    print('INIT function.....')
    offset = 0
    for pid in range(process_count):
        params = (pid, offset)
        p = run(params)
        processes.append((p, params)) 
        p.start()
        print(f'Process #{pid} - Started.')
        
        offset += LIMIT
    
    # Join
    for p, params in processes:
        p.join()
        print(f'Process #{params[0]} - Completed.')
    print('-'*40, get_datetime(), '-'*40) 
    
    
# Start
if __name__ == '__main__':
    init(1) # max_cpu_count)
        
        
    




#partner(thread_id=1, offset=0, limit=10)
#config(thread_id=2, offset=0, limit=10)






