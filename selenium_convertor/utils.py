import yaml
import json
import os
import sys


# find all steps nodes
# using :with open("tree.yaml", 'r') as yaml_in:
#     yaml_object = yaml.safe_load(yaml_in)
# print (find_key(yaml_object,"תנועות עתידיות"))
from Automation import settings


def find_path(d, value):
    for k, v in d.items():
        # print (v)
        if isinstance(v, dict):
            p = find_path(v, value)
            if p:
                return [k] + p
        elif isinstance(v, list):
            for n in v:
                p = find_path(n, value)
                if p:
                    return [k] + p
        elif k == value:
            return [k]
'''

if __name__=='__main__':
    # find all steps nodes
    with open("tree.yaml", 'r') as yaml_in:
        yaml_object = yaml.safe_load(yaml_in)
        print (find_path(yaml_object,"תנועות עתידיות"))


from voice_chat.models import *
from django.forms.models import model_to_dict
import json

settings.configure()
obj = Sites.objects.get(name="תרגול")


dict_obj = model_to_dict( obj )
serialized = json.dumps(dict_obj)

print (serialized)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'Automation.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Automation.settings")

def setup_environment():
 pathname = os.path.dirname(sys.argv[0])
 sys.path.append(os.path.abspath(pathname))
 sys.path.append(os.path.normpath(os.path.join(os.path.abspath(pathname), '../')))
 os.environ['DJANGO_SETTINGS_MODULE'] = 'Automation.settings'

setup_environment()

import django
django.setup()


'''
