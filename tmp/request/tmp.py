# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 13:09:16 2023

@author: Jeyak
"""

import requests
from http import HTTPStatus
from requests.exceptions import HTTPError

url = 'https://middleware-dev.capriglobal.in/ilos/pdfsign/encrypt-pdf?password=Qwerty%40123'

with open('../pdf/LORreport.pdf', 'rb') as f:
    pdf_content = f.read()
with open('../pdf/client-identity 2.pfx', 'rb') as f:
    pfx_content = f.read()
files = [
    ('pdf_file', ('input.pdf', pdf_content, 'application/pdf')),
    ('pfx_file', ('client-identity.pfx', pfx_content, 'application/octet-stream'))
]

try:
    print(f'Requesting to <{url}>...')
    res = requests.post(url, headers={}, files=files)
    
    res.raise_for_status()
    
    print(res)
except (HTTPError, Exception) as e:
    error_msg = "E-sign failed. "
    if e.response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        error_msg += "Incorrect Password."
    print(error_msg)
else:
    try:
        # Upload into S3
        a = 10
        print("Uploading to S3...")
        raise Exception('Error.')
    except Exception as e:
        print("Upload failed.", e, a)
