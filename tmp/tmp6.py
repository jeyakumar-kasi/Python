# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 18:28:25 2023

@author: Jeyak
"""


from time import time
from datetime import datetime, timedelta

current_time = time()
def get_working_days(start_time, end_time=None):
    end_time = int(str(end_time)[:10]) if end_time else current_time
    start_date = datetime.fromtimestamp(int(str(start_time)[:10]))
    end_date = datetime.fromtimestamp(end_time)
    bw_dates = []
    while start_date <= end_date:
        if start_date.strftime("%a") not in ('Sat', 'Sun'):
            bw_dates.append(str(start_date))
        start_date += timedelta(days=1)
    return bw_dates



for date in get_working_days(1701868229699):
    print(date)
    
for date in range(1, 10):
    print(date)


# q = [{'comment_id': '53b7e4b2-7a15-443a-839a-0c54d411518b', 'query_type': 'change', 'created_at': 1693984435096, 'rm_reply_at': 1693998675334, 'resolved_at': 1695981747599}, {'comment_id': '9a6d4b9b-e547-4aa5-b7ee-850edc28b834', 'query_type': 'change', 'created_at': 1694598510145, 'rm_reply_at': 0, 'resolved_at': 1694684224291}, {'comment_id': 'cd1f949b-97b7-4464-bce0-1ba18df1f7bf', 'query_type': 'change', 'created_at': 1695033386618, 'previous_status': {'lead_status': 'CREDIT_RECOMMENDATION', 'lead_sub_status': 'SUBMITTED_TO_CPU'}, 'resolved_at': 1695033508236}, {'comment_id': '6f6c3074-40da-41df-acd1-19f9a43b1bbc', 'query_type': 'change', 'created_at': 1695034212570, 'previous_status': {'lead_status': 'CREDIT_RECOMMENDATION', 'lead_sub_status': 'ASSIGNED_TO_UNDERWRITER'}, 'resolved_at': 1695034226368}, {'comment_id': '6f64c1b3-0257-47b1-b150-b7a9fb7cf842', 'query_type': 'add_coapplicant', 'created_at': 1695979556619, 'previous_status': {'lead_status': 'CREDIT_RECOMMENDATION', 'lead_sub_status': 'ASSIGNED_TO_UNDERWRITER'}, 'resolved_at': 1695981753081}, {'comment_id': 'b31c51a4-77fd-4cf5-a83f-1c301b795fb0', 'query_type': 'change', 'created_at': 1697447663539, 'previous_status': {'lead_status': 'QUERY_RAISED_TO_SALES', 'lead_sub_status': 'QUERY_RAISED_TO_SALES'}}, {'comment_id': '87ecf91c-8c4b-48e8-81d6-cacb4ccb4c41', 'query_type': 'change', 'created_at': 1697710085032, 'previous_status': {'lead_status': 'QUERY_RAISED_TO_SALES', 'lead_sub_status': 'QUERY_RAISED_TO_SALES'}, 'rm_reply_at': 0}, {'comment_id': '20bab162-36ac-4ae7-9634-5efb08576d9f', 'query_type': 'change', 'created_at': 1697794742859, 'previous_status': {'lead_status': 'CREDIT_RECOMMENDATION', 'lead_sub_status': 'QUERY_RAISED_TO_SALES'}}, {'comment_id': 'c86ce917-cb70-4c8b-b2c5-96e6a9afad17', 'query_type': 'change', 'created_at': 1698068055815, 'previous_status': {'lead_status': 'CREDIT_RECOMMENDATION', 'lead_sub_status': 'QUERY_RAISED_TO_SALES'}}]



# unresolved_queries = [
#     query
#     for query in q 
#     if query.get('resolved_at')
# ]

# recent_queries = sorted(unresolved_queries, key=lambda x: x['created_at'], reverse=True)

# for query in recent_queries:
#     try:
#         print(query.get('created_at'))
#     except AttributeError:
#         print(query)
#     print('------------------------')
    
