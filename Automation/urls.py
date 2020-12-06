"""Automation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from Automation.templates import HomeView
from mail_server.views import AutomateMails
from voice_chat.views import SiteImportView, SiteActivateTrial,  SiteTraversing, ModelsView, \
    BrowserTraversing


class APiTemplateView(TemplateView):
    label = ""
    action = ""
    submit = ""

    def get_context_data(self, **kwargs):
        kwargs = super(APiTemplateView, self).get_context_data(**kwargs)
        kwargs["action"] = self.action
        kwargs["label"] = self.label
        kwargs["submit"] = self.submit
        return kwargs





urlpatterns = [
    url('^$', HomeView.as_view(), name='home'),
    url('admin/', admin.site.urls),
    url('^test$', APiTemplateView.as_view(template_name="test_annyyang.html", label="Get Command",
                                          )),
    url('^voice_activation$', APiTemplateView.as_view(template_name="voiceToText.html", label="Get Command",
                                                        )),

    url('^voice_tree_activation$', APiTemplateView.as_view(template_name="voiceTreeToText.html", label="Get Command Tree",
                                                        )),

    url('^site/import/$', SiteImportView.as_view(), name='site_import'),
    url('^command$', SiteActivateTrial.as_view(), name='command'),
    #url('^command_tree$', SiteTreeActivateTrial.as_view(), name='command_tree'),
    url('^voice_request', SiteTraversing.as_view(), name='voice_request'),
    url('^browser_request', csrf_exempt(BrowserTraversing.as_view()), name='browser_traversing'),
    url('^models_view', ModelsView.as_view(), name='model_view'),
    url('^automate_mails', AutomateMails.as_view(), name='automate_mails'),


]
