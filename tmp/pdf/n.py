import tempfile
import pdfkit
import jinja2
import base64

templateLoader = jinja2.FileSystemLoader(searchpath='./')
templateEnv = jinja2.Environment(loader=templateLoader, autoescape=True)

post_data = {
    "property_id": 1,
    "application_id": "100503_JSK1",
    "logo_url": "./logo2.jpg",
    # "esign_url": "./logo2.jpg",
    "letterhead": "Lorem ipsum dolor sit amet. Qui voluptatem ducimus vel dolor dolorum aut repudiandae voluptatem non reprehenderit voluptatibus. Non obcaecati iusto id esse quod in omnis inventore? Ea expedita tempore est quos facere et consectetur accusantium eos voluptate dolores quo autem quia est sequi illo qui molestiae harum. Ut galisum aspernatur et provident enim vel quos nemo id dicta explicabo id dolores voluptatem est cupiditate repellat.",
    "date": 1702294786106,
    "report_status": "positive",
    "lop_person_name": "Lorem ipsum dolor sit amet. Et maiores provident quo aliquam ipsam eum libero accusamus vel autem eveniet non tempore laborum sed esse corporis ab repellendus quos. Vel omnis consequatur ea excepturi dolorum et voluptas officiis et dolor repudiandae. Qui vitae autem et nesciunt nisi sed esse consequatur sit perspiciatis facere ab illo nisi a harum laboriosam nam accusantium error. Aut mollitia reiciendis in dolores eveniet ad quas alias vel minus quia est pariatur rerum. Aut nesciunt similique aut eligendi ullam est animi sint. Ea harum incidunt eum earum rerum qui tempore dicta. Aut perferendis nesciunt qui autem aperiam sed nesciunt dicta id porro quas est quod unde cum eligendi ducimus sit fugit perferendis. Et debitis adipisci ut galisum sapiente aut quisquam fuga est facere voluptatem eum quam accusamus sed eveniet eius. Ut minima voluptatem est dolorem dolor sed laudantium inventore ea recusandae sapiente sit nostrum aspernatur! Est ipsum perferendis aut dolores similique et sint quis. Et dolorum voluptates ut sapiente fugit et sapiente adipisci rem nulla voluptas et ipsa fugiat ut iure rerum vel nostrum maiores.",
    "proposed_owner_names": [
        "Lorem ipsum dolor sit amet. Et maiores provident quo aliquam ipsam eum libero accusamus vel autem eveniet non tempore laborum sed esse corporis ab repellendus quos. Vel omnis consequatur ea excepturi dolorum et voluptas officiis et dolor repudiandae. Qui vitae autem et nesciunt nisi sed esse consequatur sit perspiciatis facere ab illo nisi a harum laboriosam nam accusantium error. Aut mollitia reiciendis in dolores eveniet ad quas alias vel minus quia est pariatur rerum. Aut nesciunt similique aut eligendi ullam est animi sint. Ea harum incidunt eum earum rerum qui tempore dicta. Aut perferendis nesciunt qui autem aperiam sed nesciunt dicta id porro quas est quod unde cum eligendi ducimus sit fugit perferendis. Et debitis adipisci ut galisum sapiente aut quisquam fuga est facere voluptatem eum quam accusamus sed eveniet eius. Ut minima voluptatem est dolorem dolor sed laudantium inventore ea recusandae sapiente sit nostrum aspernatur! Est ipsum perferendis aut dolores similique et sint quis. Et dolorum voluptates ut sapiente fugit et sapiente adipisci rem nulla voluptas et ipsa fugiat ut iure rerum vel nostrum maiores.",
        "Lorem ipsum dolor sit amet. Et maiores provident quo aliquam ipsam eum libero accusamus vel autem eveniet non tempore laborum sed esse corporis ab repellendus quos. Vel omnis consequatur ea excepturi dolorum et voluptas officiis et dolor repudiandae. Qui vitae autem et nesciunt nisi sed esse consequatur sit perspiciatis facere ab illo nisi a harum laboriosam nam accusantium error. Aut mollitia reiciendis in dolores eveniet ad quas alias vel minus quia est pariatur rerum. Aut nesciunt similique aut eligendi ullam est animi sint. Ea harum incidunt eum earum rerum qui tempore dicta. Aut perferendis nesciunt qui autem aperiam sed nesciunt dicta id porro quas est quod unde cum eligendi ducimus sit fugit perferendis. Et debitis adipisci ut galisum sapiente aut quisquam fuga est facere voluptatem eum quam accusamus sed eveniet eius. Ut minima voluptatem est dolorem dolor sed laudantium inventore ea recusandae sapiente sit nostrum aspernatur! Est ipsum perferendis aut dolores similique et sint quis. Et dolorum voluptates ut sapiente fugit et sapiente adipisci rem nulla voluptas et ipsa fugiat ut iure rerum vel nostrum maiores.",
        "Lorem ipsum dolor sit amet. Et maiores provident quo aliquam ipsam eum libero accusamus vel autem eveniet non tempore laborum sed esse corporis ab repellendus quos. Vel omnis consequatur ea excepturi dolorum et voluptas officiis et dolor repudiandae. Qui vitae autem et nesciunt nisi sed esse consequatur sit perspiciatis facere ab illo nisi a harum laboriosam nam accusantium error. Aut mollitia reiciendis in dolores eveniet ad quas alias vel minus quia est pariatur rerum. Aut nesciunt similique aut eligendi ullam est animi sint. Ea harum incidunt eum earum rerum qui tempore dicta. Aut perferendis nesciunt qui autem aperiam sed nesciunt dicta id porro quas est quod unde cum eligendi ducimus sit fugit perferendis. Et debitis adipisci ut galisum sapiente aut quisquam fuga est facere voluptatem eum quam accusamus sed eveniet eius. Ut minima voluptatem est dolorem dolor sed laudantium inventore ea recusandae sapiente sit nostrum aspernatur! Est ipsum perferendis aut dolores similique et sint quis. Et dolorum voluptates ut sapiente fugit et sapiente adipisci rem nulla voluptas et ipsa fugiat ut iure rerum vel nostrum maiores."
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
        "summary": "<ol><li>Qui saepe corrupti et inventore quis eum quia  saepe corrupti et inventore quis eum quia saepe corrupti et inventore quis eum quia saepe corrupti et inventore quis eum quia nemo eos autem dolorem!</li><li>Qui enim culpa eum perferendis eligendi aut veniam exercitationem.</li><li>Et autem mo saepe corrupti et inventore quis eum quia saepe corrupti et inventore quis eum quia saepe corrupti et inventore quis eum quialestias et iure assumenda nam dolor perferendis ab atque quia.</li><li>Nam similique autem ut blanditiis sapiente et totam fuga est quam illum.</li><li>Aut magni rerum id consequatur fugiat non similique accusamus id repellat ipsam!</li></ol>"
    },
    "pre_disbursal_text": "<ol><li>Qui saepe corrupti et inventore quis  saepe corrupti et inventore quis eum quia saepe corrupti et inventore quis eum quia saepe corrupti et inventore quis eum quiaeum quia nemo eos autem d saepe corrupti et inventore quis eum quia saepe corrupti et inventore quis eum quia saepe corrupti et inventore quis eum quia saepe corrupti et inventore quis eum quia saepe corrupti et inventore quis eum quia saepe corrupti et inventore quis eum quiaolorem!</li><li>Qui enim culpa eum perferendis eligendi aut veniam exercitationem.</li><li>Et autem molestias et iure assumenda nam dolor perferendis ab atque quia.</li><li>Nam similique autem ut blanditiis sapiente et totam fuga est quam illum.</li><li>Aut magni rerum id consequatur fugiat non similique accusamus id repellat ipsam!</li></ol>",
    "pdd_text": "<ol><li>Qui saepe corrupti et inventore quis eum quia nemo eos autem dolorem!</li><li>Qui enim culpa eum perferendis eligendi aut veniam exercitationem.</li><li>Et autem molestias et iure assumenda nam dolor perferendis ab atque quia.</li><li>Nam similique autem ut blanditiis sapiente et totam fuga est quam illum.</li><li>Aut magni rerum id consequatur fugiat non similique accusamus id repellat ipsam!</li></ol>",
    "receipt_no": "sadads",
    "receipt_date": 1702294786106,
    "legal_firm_name": "Lorem ipsum dolor sit amet. Et maiores provident quo aliquam ipsam eum libero accusamus vel autem eveniet non tempore laborum sed esse corporis ab repellendus quos. Vel omnis consequatur ea excepturi dolorum et voluptas officiis et dolor repudiandae. Qui vitae autem et nesciunt nisi sed esse consequatur sit perspiciatis facere ab illo nisi a harum laboriosam nam accusantium error. Aut mollitia reiciendis in dolores eveniet ad quas alias vel minus quia est pariatur rerum. Aut nesciunt similique aut eligendi ullam est animi sint. Ea harum incidunt eum earum rerum qui tempore dicta. Aut perferendis nesciunt qui autem aperiam sed nesciunt dicta id porro quas est quod unde cum eligendi ducimus sit fugit perferendis. Et debitis adipisci ut galisum sapiente aut quisquam fuga est facere voluptatem eum quam accusamus sed eveniet eius. Ut minima voluptatem est dolorem dolor sed laudantium inventore ea recusandae sapiente sit nostrum aspernatur! Est ipsum perferendis aut dolores similique et sint quis. Et dolorum voluptates ut sapiente fugit et sapiente adipisci rem nulla voluptas et ipsa fugiat ut iure rerum vel nostrum maiores.",
    "authorized_person_name": "Lorem ipsum dolor sit amet. Et maiores provident quo aliquam ipsam eum libero accusamus vel autem eveniet non tempore laborum sed esse corporis ab repellendus quos. Vel omnis consequatur ea excepturi dolorum et voluptas officiis et dolor repudiandae. Qui vitae autem et nesciunt nisi sed esse consequatur sit perspiciatis facere ab illo nisi a harum laboriosam nam accusantium error. Aut mollitia reiciendis in dolores eveniet ad quas alias vel minus quia est pariatur rerum. Aut nesciunt similique aut eligendi ullam est animi sint. Ea harum incidunt eum earum rerum qui tempore dicta. Aut perferendis nesciunt qui autem aperiam sed nesciunt dicta id porro quas est quod unde cum eligendi ducimus sit fugit perferendis. Et debitis adipisci ut galisum sapiente aut quisquam fuga est facere voluptatem eum quam accusamus sed eveniet eius. Ut minima voluptatem est dolorem dolor sed laudantium inventore ea recusandae sapiente sit nostrum aspernatur! Est ipsum perferendis aut dolores similique et sint quis. Et dolorum voluptates ut sapiente fugit et sapiente adipisci rem nulla voluptas et ipsa fugiat ut iure rerum vel nostrum maiores.",
    "authorized_person_designation": "Lorem ipsum dolor sit amet. Et maiores provident quo aliquam ipsam eum libero accusamus vel autem eveniet non tempore laborum sed esse corporis ab repellendus quos. Vel omnis consequatur ea excepturi dolorum et voluptas officiis et dolor repudiandae. Qui vitae autem et nesciunt nisi sed esse consequatur sit perspiciatis facere ab illo nisi a harum laboriosam nam accusantium error. Aut mollitia reiciendis in dolores eveniet ad quas alias vel minus quia est pariatur rerum. Aut nesciunt similique aut eligendi ullam est animi sint. Ea harum incidunt eum earum rerum qui tempore dicta. Aut perferendis nesciunt qui autem aperiam sed nesciunt dicta id porro quas est quod unde cum eligendi ducimus sit fugit perferendis. Et debitis adipisci ut galisum sapiente aut quisquam fuga est facere voluptatem eum quam accusamus sed eveniet eius. Ut minima voluptatem est dolorem dolor sed laudantium inventore ea recusandae sapiente sit nostrum aspernatur! Est ipsum perferendis aut dolores similique et sint quis. Et dolorum voluptates ut sapiente fugit et sapiente adipisci rem nulla voluptas et ipsa fugiat ut iure rerum vel nostrum maiores.",
    "enclosure_type": "<ol><li>Qui saepe corrupti et invent saepe corrupti et inventore quis eum quia saepe corrupti et inventore quis eum quia saepe corrupti et inventore quis eum quia saepe corrupti et inventore quis eum quiaore quis eum quia nemo eos autem dolorem!</li><li>Qui enim culpa eum perferendis eligendi aut veniam exercitationem.</li><li>Et autem molestias et iure assumenda nam dolor perferendis ab atque quia.</li><li>Nam similique autem ut blanditiis sapiente et totam fuga est quam illum.</li><li>Aut magni rerum id consequatur fugiat non similique accusamus id repella saepe corrupti et inventore quis eum quia saepe corrupti et inventore quis eum quia saepe corrupti et inventore quis eum quia saepe corrupti et inventore quis eum quia saepe corrupti et inventore quis eum quiat ipsam!</li></ol>",
    "footer_text": "This is the footer text. s is the footer text.the footer text. This is the footer text.This is the footer text.This is the footer text.This is the footer text.This is the footer text.This is the footer text.This is the footer text.the footer text. This is the footer text.This is the footer text.This is the footer text.This is the footer text.This is the footer text.This is the footer text.This is the footer text.the footer text. This is the footer text.This is the footer text.This is the footer text.This is the footer text.This is the footer text.This is the footer text.This is the footer text.the footer text. This is the footer text.This is the footer text.This is the footer text.This is the footer text.This is the footer text.This is the footer text.This is the footer text."
}

with open(post_data['logo_url'], 'rb') as f:
    img_data = base64.b64encode(f.read()).decode()
    post_data['logo_data'] =  f'data:image/jpg;base64,{img_data}'
# with open(post_data['esign_url'], 'rb') as f:
#     img_data = base64.b64encode(f.read()).decode()
#     post_data['esign_data'] =  f'data:image/jpg;base64,{img_data}'
post_data['deal_no'] = post_data['application_id']
post_data['transaction_type'] = 'RESALEgfgfgfhgjfhgfjghfjghfgf'
post_data['applicant_name'] = 'Ashok'
post_data['co_applicant_names'] = 'John, Peter'
post_data['current_owner_names'] = 'Khan'
post_data["proposed_owner_names"] = ", ".join(post_data["proposed_owner_names"])
post_data['product_type'] ='CGHFL'
post_data['product_type_str'] ='Capri Global Housing Finance Limited'

post_data['to_address_text'] ="""
Tower A, Peninsula Business Park, Senapati Bapat Marg, Lower Parel, Mumbai 40013.
""" 

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


# try:
with open('./style.css') as f:
    post_data['style'] = f.read()

header_html = templateEnv.get_template('header.html').render(post_data)
with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as header_file:
    header_file.write(header_html.encode('utf-8'))

footer_html = templateEnv.get_template('footer.html').render(post_data)
with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as footer_file:
    footer_file.write(footer_html.encode('utf-8'))


# with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as temp:
#     temp.write("""
#             <!DOCTYPE html>
#             <html>
#             <head>
#                 <meta charset="UTF-8">
#             </head>
#             <body>
  
#                 SAmple HEAder Text!!!!
  
#             </body>
#             </html>
#         """.encode("utf-8"))

# footer_html = """
#     <div class="c9" style="margin-top: 20px;">
#       <div class="f1rem">{footer_text}</div>
#     </div>
#     <div style="text-align: center;">Page [page] of [topage]</div>
#   </body>
# </html>
# """.format(footer_text=post_data["footer_text"])

# footer_html = post_data["footer_text"] 

options = {
    'page-size': 'A4',
    'margin-top': '1.75in',
    'margin-bottom': '1.25in',
    'margin-right': '0.25in',
    'margin-left': '0.25in',
    'encoding': "UTF-8",
    'header-html': header_file.name,
    'footer-html': footer_file.name,
    # 'footer-left': footer_html,
    # 'footer-center': 'Page [page] of [topage]',
    'footer-right': 'Page [page]',
    'footer-spacing': "5",
    'header-spacing': "2",
    # 'header-line': True,
    'footer-line': True,
    'footer-font-size': "6",
     'custom-header': [
        ('Accept-Encoding', 'gzip')
      ],
     'enable-local-file-access': False,
     'no-outline': None
}

text = templateEnv.get_template('body.html').render(post_data)
# for i in range(50):
#     text += '<br />'
# text += '<h2>This is next page body</h2>'    
# for i in range(10):
#     text += '<br />'

html = header_html + text + footer_html
with open('./my.html', 'w') as fh:
    fh.write(html)
    
config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe') #!
pdf = pdfkit.from_string(text, 'LORreport.pdf', options=options, css="./style.css", configuration=config) #!
print(header_file.name)
header_file.close()
footer_file.close()
