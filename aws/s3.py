# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 11:47:49 2023

@author: Jeyak
"""

import pdfkit
import jinja2
import boto3



class settings:
    AWS_ACCESS_KEY_ID = 'AKIAQTELWWVQGB4DLOXM'
    AWS_SECRET_ACCESS_KEY = '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'
    AWS_REGION = 'eu-north-1'
    AWS_S3_BUCKET = 'cgcl-ilos-dev-ui-datamatics'

bucket = settings.AWS_S3_BUCKET


s3_client = boto3.client(
    's3',
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_REGION,
)

url = 'https://cgcl-ilos-dev-ui-datamatics.s3.eu-north-1.amazonaws.com/LORreport.pdf'


def upload():
    post_data = {
                "logo_url": "https://pragati-uat-bucket.s3.ap-south-1.amazonaws.com/uploads/535914e8-242c-4dbc-b8ee-0dc9ea27ebcb.jpg",
                "letterhead": "This is the Letterhead",
                "deal_no": "100941",
                "property_id": 2,
                "product_type": "Capri Global Housing Finance Limited",
                "report_status": "positive",
                "date": "20/11/2023",
                "transaction_type": "RESALE",
                "lop_person_name": "Ashok",
                "payment_made_favor_of": "Ashok",
                "property_details_text": {
                  "house_details": "Flat No. 604, 6 Floor in B Wing ,admeasuring 57.00 Square Meters Carpet area",
                  "property_location": "Thane District",
                  "measurement_of_land": "453.56 sq ft"
                },
                "nature_of_property_text": {
                  "land_type": "Copy of registered Power of Attorney dated 11.10.2010 made and executed",
                  "property_type": " by M/s Tanay Developers a Proprietary Concern through its Proprietor Laxminarayan Prabhudayal Agarwal in favour of 1.Kishor Choudhary and 4 Others."
                },
                "examined_doc_text": {
                  "name_of_document": "registered Power of Attorney dated 11.10.2010 m",
                  "date_of_document": "23/11/2012",
                  "measurement_of_property": "",
                  "document_type": "",
                  "registration_type": "",
                  "document_register_type": ""
                },
                "legal_intervention_text": {
                  "type": "registered Power of Attorney dated 11.10.2010 m",
                  "summary": "registered Power of Attorney dated 11.10.2010 mregistered Power of Attorney dated 11.10.2010 m"
                },
                "conclusion_text": {
                  "type": "Power of Attorney",
                  "summary": "Attorney dated 11.10.2010 mregistered PowerAttorney dated 11.10.2010 mregistered PowerAttorney dated 11.10.2010 mregistered Power"
                },
                "receipt_no": "CLOS3722",
                "receipt_date": "30/11/2023",
                "pre_disbursal_text": {
                  "point1": "Attorney dated 11.10.2010 mregistered Power",
                  "point2": "10.2010 mregistered Power"
                },
                "pdd_text": {
                  "point1": "Attorney dated 11.10.2010 mregistered Power",
                  "point2": "10.2010 mregistered Power"
                },
                "legal_firm_name": "XYZ Ltd.",
                "authorized_person_name": "Japoer Crystel",
                "authorized_person_designation": "Manager",
                "enclosure_type": "Search Report",
                "footer_text": "<div>This is the footer</div>",
                "proposed_owner_names": [
                  "Mayannk",
                  "Kelvin"
                ],
                "esign_url": "https://pragati-uat-bucket.s3.ap-south-1.amazonaws.com/uploads/535914e8-242c-4dbc-b8ee-0dc9ea27ebcb.jpg",
                "to_address_text": "\n            Towerr A, Peninsula Business Park, Senapati Bapat Marg, Lower Parel, Mubai 40013.\n            ",
                "applicant_name": "Mayannk",
                "co_applicant_names": [
                  "Mayank"
                ],
                "current_owner_names": [
                  "Mayannk"
                ]
    }
    template_filepath = 'LORreport.html'
    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    
    templateLoader = jinja2.FileSystemLoader(searchpath='./')
    templateEnv = jinja2.Environment(loader=templateLoader, autoescape=True)
    template = templateEnv.get_template(template_filepath)
    text = template.render(post_data)
    # print(text)
    
    key_file = 'logo.png' #template_filepath.replace('.html', '.pdf')
    # output = pdfkit.from_string(text, key_file, configuration=config)
    # print(output)    
    
    #contents = pdfkit.from_string(text, output_path=False, configuration=config)
    # res = s3_client.put_object(Body=contents, Bucket=bucket, Key=key_file) 
    res = s3_client.upload_file(key_file, bucket, key_file) 
    print(res)
    
import os
from io import BytesIO
import base64
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

url = 'https://cgcl-ilos-dev-ui-datamatics.s3.eu-north-1.amazonaws.com/logo.png'

@app.route('/download')
def download(request):
  
    # with open('./common/sample_generated.pdf') as fh:
    #     return {'Body': fh.raw}
    
    if url.startswith('https') and '.s3' in url:
        # Extract the bucket name
        bucket_domain, file_key = url.split('/', 3)[2:]
        bucket_name = bucket_domain.split('.s3')[0]
        print(f'Reading {url}...')
        res = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        print(res)
        
        filename, ext = os.path.splitext(file_key)
        ext = ext.lower()
        if ext == '.pdf':
            mime_type = 'application/pdf'
        elif ext == '.png':
            mime_type = 'image/png'
        elif ext in ('.jpg', '.jpeg'):
            mime_type = 'image/jpg'
        else:
            mime_type = res['ContentType']
        #return StreamingResponse(res['Body'].iter_chunks(), media_type=mime_type)#res['ContentType'])#'application/octet-stream')
        
        img_data = base64.b64encode(res['Body'].read()).decode("utf-8")
        print(img_data)
    


# if __name__ == "__main__":
    # upload()
    
    # download(url)