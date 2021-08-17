import email
import imaplib
import os
import webbrowser
from email.header import decode_header

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
import json
import logging
import yaml
from django.views.decorators.csrf import csrf_exempt
from selenium import webdriver
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK
from rest_framework.views import APIView

import speech_recognition as sr
#from setuptools._distutils.command.clean import clean

from Automation.settings import ContextViewMixIn, get_context
from mail_server.pdf_to_text import read_pdf
from selenium_convertor.traverse_driver import Traverse
from selenium_convertor.utils import find_path
from voice_chat.forms.forms import AuthForm
from voice_chat.models import Sites, Config,Work
from voice_chat.text_to_html import Model

logger = logging.getLogger(__name__)
from webdriver_manager.chrome import ChromeDriverManager


# driver = webdriver.Chrome(ChromeDriverManager().install())
def get_request_script(command):
    # TODO add tree yaml to sites model
    with open("/home/moshe/workspace/projects/Automation/tree.yaml") as yaml_in:
        yaml_object = yaml.safe_load(yaml_in)
        path = find_path(yaml_object, command)
        script = Sites.objects.filter(name=path[0]).values()[0]['tree_script']
        return path, script


class SiteImportView(APIView, ContextViewMixIn):
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        logger.info("in ImportView POST")
        data = request.FILES['file'].read()
        try:
            obj = Sites.objects.get_or_create(name=request.data['name'])

            if (request.data["script_type"] == "script"):
                obj[0].script = data.decode()
            elif (request.data["script_type"] == "tree_script"):
                obj[0].tree_script = data.decode()
                # Sites.objects.get_or_create(name=request.data['name'], tree_script=data.decode())
            else:
                obj[0].site_yaml = data.decode()
                # Sites.objects.get_or_create(name=request.data['name'], site_yaml=data.decode())
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


class SiteActivateTrial(APIView, ContextViewMixIn):
    def post(self, request):
        logger.info("in SiteActivateTrial POST")
        command = request.data["transcript"]
        try:
            script = Sites.objects.filter(name=command).values()[0]['script']
            traverse = Traverse(command, script)
            traverse.traverse()
            return Response("succeeded", status=HTTP_200_OK)
            # return _display_process_list(request)
        except Exception as e:
            logger.error(e)
            return Response(e, status=HTTP_400_BAD_REQUEST)

    def get(self, request):
        return render(request, 'wsapi-textarea.html', self.context)



class SiteTreeActivateTrial(APIView, ContextViewMixIn):

 def post(self, request):

        context = ContextViewMixIn().context
        logger.info("in SiteTreeActivateTrial POST")
        command = request.data["action"]
        path = []
        path.append("login")
        try:
            if command == "סיום":
                if 'current_root' in request.session:
                    del request.session['current_root']
                return JsonResponse({"status": "succeeded"}, status=HTTP_200_OK)
                # TODO add tree yaml to sites model
               
            #script = Sites.objects.filter(name=path[0]).values()[0]['tree_script','site_yaml']

            data = Sites.objects.filter(name=command).values('tree_script', 'site_yaml')

            if 'current_root' in request.session: # we are after login
                is_logged = True
            else:
                is_logged = False
                request.session['current_root'] = path[0]
                path[0] = "login"

            traverse = Traverse(webdriver.Chrome())
            traverse.__set__(request.session['current_root'],
                             command, data, path,
                             is_logged)



            traverse.tree_traverse()
            return JsonResponse({"status": "succeeded"}, status=HTTP_200_OK)

            # return Response("succeeded", status=HTTP_200_OK)
            # return render(request, "home.html", context)

            # return _display_process_list(request)
        except Exception as e:
            logger.error(e)
            return Response(e, status=HTTP_400_BAD_REQUEST)


   
 def get(self, request):
        return render(request, 'wsapi-textarea.html', self.context)




class BrowserTraversing(APIView, ContextViewMixIn):
    '''

        def post(self, request):
        logger.info("Starting BrowserTraversing POST")
        context = get_context()

    '''

    def front_end_traverse(self):
        logger.info("Starting 'front_end_traverse'")
        try:
            traverse = Traverse(webdriver.Chrome())

            self.convert_to_js(self.data)
        except Exception as e:
            logger.error("traverse error : {} ".format(e))

    @csrf_exempt
    def get(self, request):
        try:
            context = ContextViewMixIn().context
            logger.info("in BrowserTraversing GET")
            command = request.query_params["action"]  # request.data["action"]
            data = Sites.objects.filter(name=command).values('tree_script', 'site_yaml')
            traverse = Traverse(webdriver.Chrome())

            js_data = traverse.convert_to_js(data[0]['tree_script'], command)
            authentication = Config.objects.get(name=command)

            js_data["code"] = authentication.get_code()
            js_data["password"] = authentication.get_password()
            # response = JsonResponse({"script": str(js_data)})
            response = JsonResponse(js_data)
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Methods'] = 'GET'
            response['Access-Control-Allow-Credentials'] = True
            return response
            # return render(request, 'model_view.html', self.context)
        except Exception as e:
            logger.error(e)


class SiteTraversing(APIView):

    def get(self, request):
        r = sr.Recognizer()
        logger.info("in SiteTreeActivateTrial POST")
        command = None
        driver = webdriver.Chrome()
        traverse = Traverse(command, request.data['script'])
        while True:
            try:
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    print("בקשתך??")
                    audio = r.listen(source)
                    command = r.recognize_google(audio, language="iw-IL")
                    if command == "סיום":
                        if 'current_root' in request.session:
                            del request.session['current_root']
                        break
                    path, script = get_request_script(command)
                    if 'current_root' in request.session:
                        is_logged = True
                    else:
                        is_logged = False
                        request.session['current_root'] = path[0]
                        path[0] = "login"
                    traverse.__set__(request.session['current_root'], command, script, path, is_logged)
                    traverse.tree_traverse()

            except Exception as e:
                logger.error(e)
                return Response(e, status=HTTP_400_BAD_REQUEST)
        return JsonResponse({"status": "succeeded"}, status=HTTP_200_OK)


'''
       if request.method == "POST":
       form = AuthForm(request.POST)
       if form.is_valid():
           name = form.cleaned_data('name')
           code = form.cleaned_data('code')
           password = form.cleaned_data('password')
           obj = Config.objects.get_or_create(name=form.name)
           obj[0].code = form.code  # request.data["code"]
           obj[0].password = form.password  # request.data["password"]
           obj[0].save()
           logger.info("import success")
           return Response("succeeded", status=HTTP_201_CREATED)
   else:
       form = AuthForm()
   render(request,"auth.html",{'form':form})

   '''

'''
class AuthView(APIView, ContextViewMixIn):

    def post(self, request):
        logger.info("in PrivateView POST")
        name = request.data["name"]
        try:
            obj = Config.objects.get_or_create(name=name)
            obj[0].code = request.data["code"]
            obj[0].password = request.data["password"]
            obj[0].save()
            logger.info("import success")
            return Response("succeeded", status=HTTP_201_CREATED)
        except Exception as e:
            logger.error(e)
            return Response(e, status=HTTP_400_BAD_REQUEST)

    def get(self,request):
        context = get_context()
        logger.info("in Config  GET")
        name = request.query_params["name"]  # request.data["action"]
        data = Config.objects.filter(name=name).values('code', 'password')

'''


def auth(request):
    form = AuthForm()
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            obj = Config.objects.get_or_create(name=form.cleaned_data["name"])
            obj[0].code = form.cleaned_data["code"]
            obj[0].password = form.cleaned_data["password"]
            obj[0].save()
            #user = form.get_user()
            #login(request, user)
            #return render(request, "auth.html", )
        else:
            return render(request, "auth.html", {'form': form, 'errors': form.errors})

    return render(request, "auth.html", {'form': form})

class SiriForProgrammers(APIView):
    def get(self,request):
        return render(request, 'siri.html')

    def post(self, request):
        model = Model()
        model.set_handlers(["create"], model.m_create)
        model.set_handlers(["form"], model.m_create_form)
        model.set_handlers(["with", "where"], model.m_set_form_attr)
        model.set_handlers(["add"], model.m_set_element)
        data = {}
        if list(request.data.keys())[0] == "todo":
            data["htmlString"]=model.traverse_command(request.data)
            data["is_html"] = True
        elif list(request.data.keys())[0] == "update":
            request.data.split("&")



        return Response(data, status=HTTP_201_CREATED)


class SaveWork(APIView):
    def post(self,request):
        logger.info("in SaveWork POST")
        obj, created = Work.objects.get_or_create(
            work_done=request.data['what_done'],
            how_done = request.data['how_done'],
            learn=request.data['learn'],
            work_next =request.data['what_next'],
            how_next = request.data['how_next'],
            code = request.data['code'],

        )


    def get(self, request):
        return render(request, 'daily_managment.html')



class ModelsView(APIView, ContextViewMixIn):

    def post(self, request):
        context = get_context()
        logger.info("in ModelsView POST")
        model = request.data["model_name"]
        try:
            model_rows = list(eval(model + ".objects.values()"))
            # context.update({"model_values": model_rows})
            return render(request, 'model_view.html', {'model_values': model_rows})
            # context = {'model_values': model_rows}
            # response = redirect('/models_view')
            # return response
        except Exception as e:
            logger.error(e)
            return Response(e, status=HTTP_400_BAD_REQUEST)

    def get(self, request):
        return render(request, 'model_view.html', self.context)

    def clean(self,text):
        # clean text for creating a folder
        return "".join(c if c.isalnum() else "_" for c in text)
    def get_mails(self):
        # number of top emails to fetch
        N = 8
        username, password = Config.objects.filter(name="email").values("code", "password")

        # create an IMAP4 class with SSL, use your email provider's IMAP server
        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        # authenticate
        imap.login(username, password)

        # select a mailbox (in this case, the inbox mailbox)
        # use imap.list() to get the list of mailboxes

        status, messages = imap.select("INBOX")
        status, messages = imap.search(None, 'SUBJECT "electric bill"')


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
if __name__ == "__main__":
    SiteTraversing().run()
