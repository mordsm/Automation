from django.shortcuts import render
import logging

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK
from rest_framework.views import APIView
from Automation.settings import ContextViewMixIn, get_context
from selenium_convertor.traverse_driver import Traverse
from voice_chat.models import Sites

logger = logging.getLogger(__name__)


class SiteImportView(APIView, ContextViewMixIn):
    #permission_classes = (IsAuthenticated,)

    def post(self, request):
        logger.info("in ImportView POST")
        data = request.FILES['file'].read()
        try:
            Sites.objects.create(name=request.data['name'],script=data.decode())
            # process_script(data.decode(), request.user)
            logger.info("import success")
            # return _display_process_list(request)
            return Response("succeeded", status=HTTP_201_CREATED)
        except Exception as e:
            error_msg = e.messages[0]
            logger.error(error_msg)
            return Response(error_msg, status=HTTP_400_BAD_REQUEST)

    def get(self, request):
        return render(request, 'upload.html', self.context)
class SiteActivateTrial(APIView, ContextViewMixIn):
    def post(self, request):
        logger.info("in SiteActivateTrial POST")
        command = request.data["q"]
        try:
            script = Sites.objects.filter(name=command).values()[0]['script']
            traverse = Traverse(command,script)
            traverse.traverse()
            return Response("succeeded", status=HTTP_200_OK)
            # return _display_process_list(request)
        except Exception as e:
            logger.error(e)
            return Response(e, status=HTTP_400_BAD_REQUEST)
    def get(self, request):
        return render(request, 'wsapi-textarea.html', self.context)