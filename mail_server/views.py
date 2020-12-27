import os
import webbrowser
from email.header import decode_header

from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.views import APIView
import json
import logging
import yaml

import email
import imaplib

# from Automation.mail_server.reading_emails import get_mails
from Automation.settings import ContextViewMixIn
from mail_server.pdf_to_text import read_pdf
from voice_chat.models import Config

logger = logging.getLogger(__name__)
'''
    def post(self, request):
        logger.info("in ImportView POST")
        data = request.FILES['file'].read()
        try:
            obj = Sites.objects.get_or_create(name=request.data['name'])

            if (request.data["script_type"] == "script"):
                obj[0].script = data.decode()
            elif (request.data["script_type"] == "tree_script"):
                obj[0].tree_script = data.decode()
                #Sites.objects.get_or_create(name=request.data['name'], tree_script=data.decode())
            else:
                obj[0].site_yaml = data.decode()
                #Sites.objects.get_or_create(name=request.data['name'], site_yaml=data.decode())
            obj[0].save()
            # process_script(data.decode(), request.user)
            logger.info("import success")
            # return _display_process_list(request)
            return Response("succeeded", status=HTTP_201_CREATED)
        except Exception as e:
            logger.error(e)
            return Response(e, status=HTTP_400_BAD_REQUEST)
 def get(self, request):
        return render(request, 'upload.html', self.context)
'''

def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)
def get_mails():
    # number of top emails to fetch
    N = 8

    auth_data = list(Config.objects.filter(name="email").values("code", "password"))[0]

    # create an IMAP4 class with SSL, use your email provider's IMAP server
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    # authenticate
    imap.login(auth_data["code"], auth_data["password"])

    # select a mailbox (in this case, the inbox mailbox)
    # use imap.list() to get the list of mailboxes

    status, messages = imap.select("INBOX")
    #status, messages = imap.search(None, 'SUBJECT "electric bill"')


    # total number of emails
    messages = int(messages[0])

    for i in range(messages, messages-N, -1):
        # fetch the email message by ID
        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])
                # decode the email subject
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    # if it's a bytes, decode to str
                    subject = subject.decode(encoding)
                # decode email sender
                From, encoding = decode_header(msg.get("From"))[0]
                if isinstance(From, bytes):
                    From = From.decode(encoding)
                print("Subject:", subject)
                print("From:", From)
                # if the email message is multipart
                if msg.is_multipart():
                    # iterate over email parts
                    for part in msg.walk():
                        # extract content type of email
                        content_type = part.get_content_type()

                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                            # get the email body
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            # print text/plain emails and skip attachments
                            print(body)
                        elif "attachment" in content_disposition:
                            # download attachment
                            filename = part.get_filename()
                            if filename:
                                folder_name = clean(subject)
                                if not os.path.isdir(folder_name):
                                    # make a folder for this email (named after the subject)
                                    os.mkdir(folder_name)
                                filepath = os.path.join(folder_name, filename)
                                # download attachment and save it
                                open(filepath, "wb").write(part.get_payload(decode=True))
                                if ("pdf" in content_type):
                                    read_pdf(filepath)
                else:
                    # extract content type of email
                    content_type = msg.get_content_type()
                    # get the email body
                    body = msg.get_payload(decode=True).decode()
                    if content_type == "text/plain":
                        # print only text email parts
                        print(body)
                if content_type == "text/html":
                    # if it's HTML, create a new HTML file and open it in browser
                    folder_name = clean(subject)
                    if not os.path.isdir(folder_name):
                        # make a folder for this email (named after the subject)
                        os.mkdir(folder_name)
                    filename = "index.html"
                    filepath = os.path.join(folder_name, filename)
                    # write the file
                    open(filepath, "w").write(body)
                    # open in the default browser
                    webbrowser.open(filepath)
                print("="*100)
    # close the connection and logout
    imap.close()
    imap.logout()
class AutomateMails(APIView, ContextViewMixIn):
    def post(self, request):
        logger.info("in AutomateMails POST")


        SERVER = 'imap.gmail.com'

        # connect to the server and go to its inbox
        mail = imaplib.IMAP4_SSL(SERVER)
        #mail.login(EMAIL, PASSWORD)
        # we choose the inbox but you can select others
        mail.select('inbox')

        # we'll search using the ALL criteria to retrieve
        # every message inside the inbox
        # it will return with its status and a list of ids
        status, data = mail.search(None, 'ALL')
        # the list returned is a list of bytes separated
        # by white spaces on this format: [b'1 2 3', b'4 5 6']
        # so, to separate it first we create an empty list
        mail_ids = []
        # then we go through the list splitting its blocks
        # of bytes and appending to the mail_ids list
        for block in data:
            # the split function called without parameter
            # transforms the text or bytes into a list using
            # as separator the white spaces:
            # b'1 2 3'.split() => [b'1', b'2', b'3']
            mail_ids += block.split()

        # now for every id we'll fetch the email
        # to extract its content
        for i in mail_ids:
            # the fetch function fetch the email given its id
            # and format that you want the message to be
            status, data = mail.fetch(i, '(RFC822)')

            # the content data at the '(RFC822)' format comes on
            # a list with a tuple with header, content, and the closing
            # byte b')'
            for response_part in data:
                # so if its a tuple...
                if isinstance(response_part, tuple):
                    # we go for the content at its second element
                    # skipping the header at the first and the closing
                    # at the third
                    message = email.message_from_bytes(response_part[1])

                    # with the content we can extract the info about
                    # who sent the message and its subject
                    mail_from = message['from']
                    mail_subject = message['subject']

                    # then for the text we have a little more work to do
                    # because it can be in plain text or multipart
                    # if its not plain text we need to separate the message
                    # from its annexes to get the text
                    if message.is_multipart():
                        mail_content = ''

                        # on multipart we have the text message and
                        # another things like annex, and html version
                        # of the message, in that case we loop through
                        # the email payload
                        for part in message.get_payload():
                            # if the content type is text/plain
                            # we extract it
                            if part.get_content_type() == 'text/plain':
                                mail_content += part.get_payload()
                    else:
                        # if the message isn't multipart, just extract it
                        mail_content = message.get_payload()

                    # and then let's show its result
                    print(f'From: {mail_from}')
                    print(f'Subject: {mail_subject}')
                    print(f'Content: {mail_content}')

    def get(self, request):
        get_mails()
