# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 22:31:30 2023

@author: JeyakumarKasi
"""

import requests


def internal_request(path, payload):
    url = current_app.config['BASE_URL'] + '/' + path
    print(url)
    payload = json.dumps(payload)
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache"
    }

    print(payload)
    
    try:
        resp = requests.request("POST", url, data=payload, auth=(str(cf.flask_user_id), str(cf.flask_pass)),
                                headers=headers)
        print(resp)
        resp.raise_for_status() # For raising any HTTP Errors.
        if resp.status_code == 200:
            return resp.json()
        else:
            log.info('error received in request %s', resp.text)
            return {"status": False}
    except requests.exceptions.Timeout as e:
        log.error('Timeout Exception in internal request function {}'.format(e))
    except requests.exceptions.TooManyRedirects as e:        
        log.error('Too many redirections in internal request function {}'.format(e))
    except requests.exceptions.RequestException as e:
        log.error('Exception on request in internal request function {}'.format(e))
    except requests.exceptions.HTTPError as err:
        log.error('HTTP errors are raised in internal request function {}'.format(e))
    except Exception as e:
        log.error('Exception in internal request function {}'.format(e))
    
    return {"status": False}





def strip_dict(thisdict):
    newdict = {}
    try:
        for key in thisdict:
            val = thisdict[key]
            if isinstance(val, dict):
                for key2 in val:
                    val2 = val[key2]
                    val[key2] = val2.strip() if isinstance(val2, str) else val2
            newdict[key] = val.strip() if isinstance(val, str) else val
        return newdict
    except Exception as err:
        log("Error in strip_dict function - %s", err)
        return thisdict


d = {
    'name': '  dhsjdsh '     
}
dd = strip_dict(d)

print(dd)



# url = 'http://hyproid.com/'

# headers = {
#     'Content-Type': "application/json",
#     'cache-control': "no-cache"
# }

# payload = {
#     'user': 'xyz'    
# }

# try:
#     res = requests.request('POST', url, data=payload, headers=headers)
#     if res.status_code == 200:
#         print("OK")
#     else:
#         print("Error is occured.")
# except Exception as e:
#         print('Exception in internal request function {}'.format(e))
