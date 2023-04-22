# -*- coding: utf-8 -*-
"""
Created on Mon Apr 03 20:23 2023

@author: <jeyakumar.kasi@hyproid.com>
"""
partner_id = 53 # MDS


filters_data = {
    'fk_acquisition_user_filter_id': (1, 6, 5, 4, 8, 7),
    'filter_value': ('18', '35000', '9000', 'Self Employed', 'email', '45'),
    '"profession_type"': (
        '\'Salaried\'::public."profession_type"', '\'Salaried\'::public."profession_type"',
        '\'Salaried\'::public."profession_type"', '\'Self Employed\'::public."profession_type"',
        '\'All\'::public."profession_type"', '\'Salaried\'::public."profession_type"'
    )
}

import datetime as dt
def current_timestamp():
    return dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

now_str = current_timestamp()
print(now_str)
static_columns = {
    'fk_acquisition_partner_id': partner_id,
    'is_active': True,
    'added_by': '1',
    'created_on': now_str,
    'updated_on': now_str,
    # 'parent_id': None,
    'created_at': now_str
}

columns = list(filters_data.keys())
columns.extend(list(static_columns.keys()))
elements_len = len(filters_data[columns[0]])
static_values = [val if isinstance(val, str) else str(val) for val in static_columns.values()]

for i in range(elements_len):
    q = "INSERT INTO public.tbl_mapping_acquisition_user_filter "
    q += "(" + (", ".join(columns)) + ") VALUES ("

    for clm in filters_data:
        val = str(filters_data[clm][i])
        if val[0] != "'":
            q += "'" + val + "', "
        else:
            q += val + ", "

    q += "'" + ("', '".join(static_values)) + "')"
    print(q); print('-' * 20)


