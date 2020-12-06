"""
WSGI config for Automation project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
path = '/home/moshe/workspace/projects/Automation'
if path not in sys.path:
    sys.path.append(path)
path = '/home/moshe/workspace/projects/Automation/env'
if path not in sys.path:
    sys.path.append(path)
path = '/home/moshe/workspace/projects/Automation/Automation'
if path not in sys.path:
    sys.path.append(path)

#path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Automation.settings')

application = get_wsgi_application()
