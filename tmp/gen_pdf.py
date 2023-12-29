# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 18:11:52 2023

@author: Jeyak
"""

import pdfkit
import jinja2

config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')



post_data = {
    "property_id": 1,
    "application_id": "100503_JSK1",
    "logo_url": "#",
    "esign_url": "#",
    "letterhead": "ksndlksdfnlfs",
    "date": 1702294786106,
    "report_status": "positive",
    "lop_person_name": "sndlskadnl",
    "proposed_owner_names": [
        "sdfsdf",
        "sdadad",
        "qweqwe"
    ],
    "payment_made_favor_of": "lkjdoiewjdoiew",
    "property_details_text": {
        "house_details": "smncdsfnk",
        "property_location": "ds,mnfdskjfn",
        "measurement_of_land": "kfnksjdnfkjdsnfkjds"
    },
    "nature_of_property_text": {
        "land_type": "Freehold",
        "property_type": "Commercial"
    },
    "examined_doc_text": "<ol><li>Qui saepe corrupti et inventore quis eum quia nemo eos autem dolorem!</li><li>Qui enim culpa eum perferendis eligendi aut veniam exercitationem.</li><li>Et autem molestias et iure assumenda nam dolor perferendis ab atque quia.</li><li>Nam similique autem ut blanditiis sapiente et totam fuga est quam illum.</li><li>Aut magni rerum id consequatur fugiat non similique accusamus id repellat ipsam!</li></ol>",
    "legal_intervention_text": {
        "type": "yes",
        "summary": "<ol><li>Qui saepe corrupti et inventore quis eum quia nemo eos autem dolorem!</li><li>Qui enim culpa eum perferendis eligendi aut veniam exercitationem.</li><li>Et autem molestias et iure assumenda nam dolor perferendis ab atque quia.</li><li>Nam similique autem ut blanditiis sapiente et totam fuga est quam illum.</li><li>Aut magni rerum id consequatur fugiat non similique accusamus id repellat ipsam!</li></ol>"
    },
    "conclusion_text": {
        "type": "yes",
        "summary": "<ol><li>Qui saepe corrupti et inventore quis eum quia nemo eos autem dolorem!</li><li>Qui enim culpa eum perferendis eligendi aut veniam exercitationem.</li><li>Et autem molestias et iure assumenda nam dolor perferendis ab atque quia.</li><li>Nam similique autem ut blanditiis sapiente et totam fuga est quam illum.</li><li>Aut magni rerum id consequatur fugiat non similique accusamus id repellat ipsam!</li></ol>"
    },
    "pre_disbursal_text": "<ol><li>Qui saepe corrupti et inventore quis eum quia nemo eos autem dolorem!</li><li>Qui enim culpa eum perferendis eligendi aut veniam exercitationem.</li><li>Et autem molestias et iure assumenda nam dolor perferendis ab atque quia.</li><li>Nam similique autem ut blanditiis sapiente et totam fuga est quam illum.</li><li>Aut magni rerum id consequatur fugiat non similique accusamus id repellat ipsam!</li></ol>",
    "pdd_text": "<ol><li>Qui saepe corrupti et inventore quis eum quia nemo eos autem dolorem!</li><li>Qui enim culpa eum perferendis eligendi aut veniam exercitationem.</li><li>Et autem molestias et iure assumenda nam dolor perferendis ab atque quia.</li><li>Nam similique autem ut blanditiis sapiente et totam fuga est quam illum.</li><li>Aut magni rerum id consequatur fugiat non similique accusamus id repellat ipsam!</li></ol>",
    "receipt_no": "sadads",
    "receipt_date": 1702294786106,
    "legal_firm_name": "lskamdlkadmsa",
    "authorized_person_name": "s,nlkdsf",
    "authorized_person_designation": "skdjfndskjf",
    "enclosure_type": "<ol><li>Qui saepe corrupti et inventore quis eum quia nemo eos autem dolorem!</li><li>Qui enim culpa eum perferendis eligendi aut veniam exercitationem.</li><li>Et autem molestias et iure assumenda nam dolor perferendis ab atque quia.</li><li>Nam similique autem ut blanditiis sapiente et totam fuga est quam illum.</li><li>Aut magni rerum id consequatur fugiat non similique accusamus id repellat ipsam!</li></ol>",
    "footer_text": "ksfjkjdsfkdsf"
}

post_data['logo_data'] = post_data['logo_url']
post_data['esign_data'] = post_data['esign_url']
post_data['deal_no'] = post_data['application_id']
post_data['transaction_type'] = 'RESALE'
post_data['applicant_name'] = 'Ashok'
post_data['co_applicant_names'] = 'John, Peter'
post_data['current_owner_names'] = 'Khan'

# New changes
# ------------------

from datetime import datetime
def epoch_to_dd_mm_yyyy(epoch_timestamp, format_str="%d-%m-%Y"):
    # Convert epoch timestamp to datetime object
    dt_object = datetime.fromtimestamp(epoch_timestamp)

    # Format the datetime object as "dd-mm-yyyy"
    formatted_date = dt_object.strftime(format_str)

    return formatted_date
    # return '30/12/2023'

# date_of_document = post_data.get('examined_doc_text', {}).get('date_of_document')
# if date_of_document:
#     # Make a valid datetime
#    date_of_document = int(str(date_of_document)[:10])
#    post_data['examined_doc_text']['date_of_document'] = epoch_to_dd_mm_yyyy(date_of_document, format_str="%d/%m/%Y")
   
# Make a valid datetime
post_data['date'] = epoch_to_dd_mm_yyyy(int(str(post_data['date'])[:10]), format_str="%d/%m/%Y")
post_data['receipt_date'] = epoch_to_dd_mm_yyyy(int(str(post_data['receipt_date'])[:10]), format_str="%d/%m/%Y")
post_data['report_status'] = post_data['report_status'].upper()

post_data['legal_intervention_decision'] = post_data.get('legal_intervention_text', {}).pop('type', 'no').strip().upper() == 'YES'
post_data['conclusion_decision'] = post_data.get('conclusion_text', {}).pop('type', 'no').strip().upper() == 'YES'


template_filename = 'LORreport.html'
templateLoader = jinja2.FileSystemLoader(searchpath='./')
templateEnv = jinja2.Environment(loader=templateLoader, autoescape=True)
template = templateEnv.get_template(template_filename)
text = template.render(post_data)
print(text)
with open('./my.html', 'w') as fh:
    fh.write(text)

output = pdfkit.from_string(text, template_filename.replace('.html', '.pdf'), configuration=config)#, options={'enable-local-file-access': ''})
print(output)
 
