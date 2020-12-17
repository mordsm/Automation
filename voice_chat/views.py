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
from Automation.settings import ContextViewMixIn, get_context
from selenium_convertor.traverse_driver import Traverse
from selenium_convertor.utils import find_path
from voice_chat.forms.forms import AuthForm
from voice_chat.models import Sites, Config
import speech_recognition as sr

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


'''
class SiteTreeActivateTrial(APIView, ContextViewMixIn):

 def post(self, request):

        context = ContextViewMixIn().context
        logger.info("in SiteTreeActivateTrial POST")
        command = request.data["action"]

        try:
            if command == "סיום":
                if 'current_root' in request.session:
                    del request.session['current_root']
                return JsonResponse({"status": "succeeded"}, status=HTTP_200_OK)
                # TODO add tree yaml to sites model
               
            script = Sites.objects.filter(name=path[0]).values()[0]['tree_script','site_yaml']


            if 'current_root' in request.session:
                is_logged = True

            else:
                is_logged = False

                request.session['current_root'] = path[0]
                path[0] = "login"

            traverse = Traverse(webdriver.Chrome())
            traverse.__set__(request.session['current_root'],
                             command, script, path,
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

'''


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


if __name__ == "__main__":
    SiteTraversing().run()
