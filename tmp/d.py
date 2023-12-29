# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 14:04:23 2023

@author: JeyakumarKasi
"""

args = {
    "act": "update",
    "dt": {
        "property_details": [
            {
                "id": "2",
                "property_owner_id": "100380"
            },
            {
                "id": "1",
                "property_owner_id": "100382"
            },
            {
                "id": "1",
                "property_owner_id": "100380"
            }
        ]
    }
    
}


d = {
     "name": "XYZ",
     "applicant": {
         "primary": {
              "property_details": [
                  {
                      "id": 2,
                      "property_ownership": {
                           "type": "single",
                           "owners": [
                               {
                                   "owner_type": "co_applicant",
                                    "owner_id": 100382,
                                    "owner_name": "Suhana"
                             }]
                       }
                   },
                  {
                      "id": 1,
                      "property_ownership": {
                           "type": "single",
                           "owners": [
                               {
                                   "owner_type": "primary_applicant",
                                    "owner_id": 100380,
                                    "owner_name": "TRIMUPH890"
                             }]
                       }
                   },
                ]   
          }    
     }
}


input_args = args['dt']['property_details']
property_details = {int(p['id']): p for p in d['applicant']['primary']['property_details']}

for item in input_args:
    property_id = int(item['id'])
    print(property_id)
    
    d.setdefault('tracking_details', {}).setdefault('property_ownership_history', [])
    d['tracking_details']['property_ownership_history'].append(property_details[property_id]['property_ownership'])

print(d['tracking_details'])



