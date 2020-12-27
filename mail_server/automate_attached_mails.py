import imaplib
import email
import logging
import regex
import re
logger = logging.getLogger(__name__)
user = ''
password = ''

server = imaplib.IMAP4_SSL('imap.gmail.com', '993')
server.login(user, password)
server.select('inbox')

msg_ids=[]
resp, messages = server.search(None, 'SUBJECT "electric bill"')
for message in messages[0].split():
        typ, data = server.fetch(message, '(RFC822)')
        msg= email.message_from_string(str(data[0][1]))

        #looking for 'Content-Type: application/pdf
        for part in msg.walk():
            logger.error(part.get_content_type())
            if part.get_content_type() == 'application/pdf':

                # When decode=True, get_payload will return None if part.is_multipart()
                # and the decoded content otherwise.
                payload = part.get_payload(decode=True)

                # Default filename can be passed as an argument to get_filename()
                filename = part.get_filename()

                # Save the file.
                if payload and filename:
                    with open(filename, 'wb') as f:
                        f.write(payload)
