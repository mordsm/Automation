'''
Created on Oct 16, 2019

@author: eytan
'''

import json
import logging
import os
import re
from datetime import datetime

import requests
from django.conf.global_settings import STATIC_ROOT
from django.forms import model_to_dict
from django.http.response import HttpResponse, \
    JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from Automation.common.settings import get_context
from voice_chat.models import Sites

logger = logging.getLogger(__name__)

TRAILING_SLASH = re.compile("/$")


def get_user_context(user):
    return {"user_full_name": user.profile.full_name, "user_photo": user.profile.photo} \
        if os.path.exists(os.path.join(STATIC_ROOT, user.profile.photo)) else \
        {"user_full_name": user.profile.full_name}


def get_home_view_context(user):
    context = get_context()
    context['title'] = "Home"
    #context.update(get_user_context(user))
    # context["processes"] = recent_processes(user)
    # context["schedules"] = upcoming_process_runs(user)
    # context["accessibility"] = get_accessibility_pie_context(user)

    return context


class HomeView(APIView):

    def get(self, request):
        """Renders the home page."""
        #TODO add login page
        context = get_home_view_context(request.user)




        return render(
            request,
            'home.html',
            None#context
        )


'''

       obj = Sites.objects.get(name="תרגול")

        dict_obj = model_to_dict(obj)
        serialized = json.dumps(dict_obj)
        #script = json.loads(serialized.script)
        #print(script)
        # now write output to a file
        DataFile = open("/home/moshe/Downloads/bp_selenium_converted.side", "w")

        DataFile.write(dict_obj)
        DataFile.close()

        print(serialized)
'''
