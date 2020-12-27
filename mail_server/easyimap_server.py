import easyimap
import logging
import pdf_to_text as pdf
logger = logging.getLogger(__name__)
login = ''
password = ''

imapper = easyimap.connect('imap.gmail.com', login, password)
for mail_id in imapper.listids(limit=100):
    mail = imapper.mail(mail_id)
    print("from" ,mail.from_addr)
    print("to" ,mail.to)
    print(mail.cc)
    print(mail.title)
    print(mail.body)
    if (mail.attachments and 'application/pdf' in mail.attachments[0]) :
        pdf.read_pdf_object(mail.attachments[0][1])
        print(mail.attachments)