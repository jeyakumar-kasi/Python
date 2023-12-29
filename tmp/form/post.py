# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 16:44:46 2023

@author: Jeyak
"""

# pip install python-multipart
from dataclasses import dataclass
from fastapi import FastAPI, Form, Depends, UploadFile, File

app = FastAPI()

# class FormSubmitRequest():
#     password: str = None

@dataclass
class LVFormData():
    password: str = Form(...)
    property_details_text: str = Form(...)

@app.post('/submit')
def submit(
    form_data: LVFormData = Depends(), 
    pfx_file: UploadFile = File()
):
    print("Data received")
    print(form_data.property_details_text)
    print(type(form_data.property_details_text))
    print(pfx_file.content_type)
    for i in [k for k in dir(pfx_file) if not k.startswith('__')]:
        print(i)
        
    with open('./upload', 'wb') as fh:
        fh.write(pfx_file.file.read())
    return "OK"



# if __name__ == "__main__":
    # app.run()