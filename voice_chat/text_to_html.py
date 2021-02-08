from transitions import Machine, State as s
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, ElementTree
from nltk.tokenize import sent_tokenize
import numpy as np
import yaml
import sys, os
import logging

from voice_chat.yaml_utils import nested_item_children

jump_over = [",", "and", "|"]
logger = logging.getLogger("__name__")



# import xml.etree.ElementTree as ET
try:
    # f =open("site.yaml", "r")
    f = os.path.join(sys.path[0], 'site.yaml')
    data = yaml.load(f, Loader=yaml.FullLoader)
except:
    with open("site.yaml") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
root = Element('my_site')
SubElement(root, 'head')
body = SubElement(root, 'body')


def find(key, dictionary):
    for k, v in dictionary.items():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in find(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                for result in find(key, d):
                    yield result


states = ['initial', 'create_state', 'create_form_state', 'GG']
transitions = [
    ['create', 'initial', 'create_state'],
    ['form', 'create_state', 'create_form_state'],
    ['input', 'create_state', 'create_element_state'],
    ['with', 'create_form_state', None],

]
m = Machine(states=states, transitions=transitions, initial='initial')
m.add_transition('id', source='create_form_state', dest=None, after='set_attr')
m.add_transition('name', source='create_form_state', dest=None, after='set_attr')
m.add_transition('value', source='create_form_state', dest=None, after='set_attr')


def get_word(sentence):
    for word in sentence:
        yield word


def get_base_word(word):
    arr = np.array([["create", "add", 'build'],
                    ["with", "where", "and"],
                    ["=", "is", "eq"],
                    ["", "2", ""]])
    result = np.where(arr == word)
    return (arr[result[0], 0][0])




def get_configuration():
    try:
        file_path = os.path.join(sys.path[0], 'config.yaml')
        f = open(file_path, "r")
        return (yaml.safe_load(f.read()))
    except Exception as e:
        logger.error(e)
class Model():
    handlers = {}
    word = ""
    c_tokens = ""
    c_parent = None
    c_element = None
    c_value = None
    word_gen = None
    config = get_configuration()


    def set_attr_name(self):
        self.c_attr = self.word

    def set_attr_value(self, value):
        # self.c_element[self.c_attr] = value
        self.c_element.set(self.c_attr, value)

    def model_callback(self):
        print("callback called")
        pass

    def after_create_state_form(self):
        self.c_element_type = "form"
        print(self.c_element)

    def add_form_id(self):
        pass

    def set_handlers(self, names, func):
        for name in names:
            self.handlers[name] = func

    def m_create(self):
        print("you are in Create word")
        m.state = "create_form_state"
        return False,m.state

    def create_attr_modal(self,param):
        modal = "<form id='details' class='form-group'>"
        modal += "<fieldset><legend>Fill details</legend>"
        for attr in nested_item_children(self.config, param):
            modal = modal + "  <input type=txt id='{}' name='{}' placeholder='{}' >".format(attr, attr, attr,
                                                                                                      attr)
        modal+=  "<br/><input type=button id ='update' name='update' value='Update'/> </form>"
        modal += "</fieldset>"
        return modal
    def m_create_form(self):
        self.c_element_type = "form"
        form = SubElement(body, 'form', method="POST", action="")
        self.c_element = form
        return True,self.create_attr_modal("form")
        # open("test_html", "w")

    def m_set_form_attr(self):
        while len(self.c_tokens) > 0:
            self.word = next(self.word_gen)

            if self.word in nested_item_children(self.config, "form"):
                self.set_attr_name()
                self.word = next(self.word_gen)
                if self.word in ["is", "eq", "="]:
                    self.set_attr_value(next(self.word_gen))
                    self.c_tokens[:] = self.c_tokens[3:]

        is_end = True

    def m_set_element(self):
        if self.c_parent is None:
            self.c_parent = self.c_element
        self.c_element = SubElement(self.c_parent, 'input', id="", name="", value="", placeholder="")
        while len(self.c_tokens) > 0:
            self.word = next(self.word_gen)
            if self.word in nested_item_children(self.config, "jump_over"):
                self.word = next(self.word_gen)
            if self.word in nested_item_children(self.config, "element"):
                self.set_attr_name()
                self.word = next(self.word_gen)
                if self.word in ["is", "eq", "="]:
                    self.set_attr_value(next(self.word_gen))
                    self.c_tokens[:] = self.c_tokens[3:]
        is_end = True



    def traverse_command(self, para):
        is_end = False
        lines = ""
        self.c_tokens = para["todo"].split(' ')
        self.word_gen = get_word(self.c_tokens)
        while len(self.c_tokens) > 0:
            self.word = next(self.word_gen)
            self.c_tokens = self.c_tokens[1:]
            if self.word in self.handlers.keys():
                result,data = self.handlers[self.word]()
                if result:
                    return data
    tree = ElementTree(root)
    tree.write("test_html.xml")
    print(tree)

if __name__ == "__main__":
    model = Model()
    model.set_handlers(["create"], model.m_create)
    model.set_handlers(["form"], model.m_create_form)
    model.set_handlers(["with", "where"], model.m_set_form_attr)
    model.set_handlers(["add"], model.m_set_element)
    model.traverse_string("create form with id = myform method = GET. add user name input field.")
'''
    def traverse_string(self, para):
        is_end = False
        commands = sent_tokenize(para["todo"])
        for command in commands:
            lines = ""
            self.c_tokens = command.split(' ')
            self.word_gen = get_word(self.c_tokens)
            while len(self.c_tokens) > 0:
                self.word = next(self.word_gen)
                self.c_tokens = self.c_tokens[1:]
                if self.word in self.handlers.keys():
                    is_end = self.handlers[self.word]()
                elif command.startswith('{'):
                    pass
                else:
                    print("{} doesn't exist in dictionary".format(self.word))
                    while True:
                        inp = input()
                        if inp == "quit":
                            break
                        lines += inp + "\n"
                    self.handlers[self.word] = "def m_{}()".format(self.word) + lines
                if is_end:
                    break
        tree = ElementTree(root)
        tree.write("test_html.xml")
        print(tree)
'''