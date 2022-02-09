import json
import time
import logging
from time import sleep
import sys

from GoogleTrans2020.Translator import translator
from selenium.webdriver.common.by import By
import vlc

import speech_recognition as sr

heb_dict = {"עובר ושב": "Current account"}
logger = logging.getLogger(__name__)

from voice_chat.models import Sites
from gtts import gTTS
from langdetect import detect
from googletrans import Translator

'''
     def __init__(self, file):
       with open(file, 'r') as f:
           self.data = json.load(f)
   '''

def log(message):
    import inspect
    import gc
    code = inspect.currentframe().f_back.f_code
    func = [obj for  obj in  gc.get_referrers(code) if inspect.isfunction(obj)][0]
    print(func.__qualname__, message)

class Traverse():

    def __init__(self, driver):
        self.driver = driver

    def __set__(self, base, name, script, path, is_logged):
        self.path = path
        self.is_logged = is_logged
        self.base = base
        self.name = name
        script = script[0]['tree_script']
        # script[0].replace("\'", "\"")
        self.data = json.loads(script)

    def text_to_speech(self, text):

        try:
            tts = gTTS(text)
            tts.save('voice.mp3')
            vlc.MediaPlayer('voice.mp3').play()

        except Exception as e:
            logger.error(e)

    def teardown_method(self, method):
        self.driver.quit()

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def traverse(self):
        try:
            tests = self.data["tests"]
            for test in tests:
                for command in test["commands"]:
                    accessible_name, title = self.action(command)
                    command["name"] = accessible_name
                    command["title"] = title
            script = json.dumps(self.data)
            Sites.objects.filter(name=self.name).update(script=script)
        except Exception as e:
            logger.error("traverse error : {} ".format(e))

    def front_end_traverse(self):
        logger.info("Starting 'front_end_traverse'")
        try:
            script = self.convert_to_js(self.data)
        except Exception as e:
            logger.error("traverse error : {} ".format(e))

    def tree_traverse(self):
        logger.info("Starting 'tree_traverse'")
        try:
            start = 0
            # TODO temporary fix for debugging  self.is_logged = False
            self.is_logged = False
            if self.is_logged:
                start = 1
                self.action(self.data["home"])
            steps = self.data["tests"]
            for step in steps[start:]:
                # part = [item for item in self.data[self.base] if item["name"] == action]
                # part = [item for item in self.data[self.name] if item["name"] == action["name"]]

                # part = self.data[action]
                for command in step["commands"]:
                    accessible_name, title = self.action(command)
                    command["name"] = accessible_name
                    command["title"] = title
            script = json.dumps(self.data)
            Sites.objects.filter(name=self.name).update(script=script)
        except Exception as e:
            logger.error("traverse error : {} {}".format(e, step))

    def get_locator(self, target):
        if target[0].startswith("css"):
            return By.CSS_SELECTOR
        elif target[0].startswith("xpath"):
            return By.XPATH
        elif target[0].startswith("id"):
            return By.ID

    def get_transcript(self):
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source, timeout=4)
                if audio is None:
                    return None
                logger.info("Recognizing Now ... ")
                return r.recognize_google(audio)
        except Exception as e:
            logger.error("get_transcript: {e}")

    def get_user_answer(self, question):
        try:
            while True:
                self.text_to_speech(question)
                transcript = self.get_transcript()
                if transcript == "quit":
                    return None
                self.text_to_speech("Did You  say : " + transcript + "? y(es) / n(o)")
                confirm = self.get_transcript()
                if confirm == 'y' or 'yes':
                    return transcript
        except Exception as e:
            logger.error("get_user_answer: {}".format(e))
            return None

    def getTranslate(self, text, **kwargs):
        # translator = Translator()
        translator = Translator(service_urls=['translate.googleapis.com'])

        result = None
        i = 0;
        while result == None and i < 2:
            try:
                sleep(1)
                result = translator.translate(text)
            except Exception as e:
                i = i + 1
                print(e)
                # translator = Translator()
                sleep(0.5)
                pass
        result = result.text if result is not None else result
        return result

    def getAny(self, dic, keys, default=None):

        for k in keys:
            k = k.replace('\n', ' ')
            if k in dic:
                return dic[k]
        return default

    def build_question(self, field_name):
        result = None
        try:
            lang = detect(field_name)
            if lang == "he":
                field_name = self.getTranslate(field_name, dest="en")
            if field_name != None:
                field = field_name
            else:
                field = ""
                # translator.translate(field_name).pronunciation
            result = "please enter " + field
            return result
        except Exception as e:
            log(e)
            print("build_question : {} ".format(e))

    def action(self, command):
        logger.info("starting 'action'")
        try:
            result = None
            match command["command"]:
                case "open":
                    if (len(command["target"]) > 10):
                        element = self.driver.get(command["target"])
                    else:
                        element = self.driver.get(self.data["url"] + command["target"])
                    self.driver.title


                case "setWindowSize":
                    sizes = command["target"].split("x")
                    element = self.driver.set_window_size(int(sizes[0]), int(sizes[1]))
                case "selectFrame":
                    time.sleep(1)
                    frame = command["target"].split("=")[1]
                    if frame.isnumeric():
                        self.driver.switch_to.frame(int(frame))
                    elif frame == "parent":
                        self.driver.switch_to.default_content()
                    # self.wait_for_window()

                case "click":
                    element, result = self.find_element(command)
                    if element:
                        try:
                            #  TODO change condition to be specific on unput types using enums
                            if element.tag_name not in ["span", 'fieldset', 'button', 'a']:
                                lang = detect(result)
                                if lang == "he":
                                    result_en = self.getAny(heb_dict, [result])
                                    if result_en == None:
                                        result_en = self.getTranslate(result, dest="en")
                                    # translator.translate(text = result)
                                    self.text_to_speech("please enter " + result_en)
                                    print(result_en)
                                elif result != None:
                                    self.text_to_speech("please enter " + result)
                                    print(result)

                        except Exception as e:
                            print(f"error {e} on command {command['command']}  target: {command['target']}")
                        finally:
                            element.click()
                    else:
                        print(command)

                case "type":
                    element, result = self.find_element(command)
                    element.clear()
                    element.send_keys(command["value"])
                case "mouseOver":
                    element, result = self.find_element(command)
                case "mouseOut":
                    element, result = self.find_element(command)
                case "doubleClick":
                    element, result = self.find_element(command)
                    element.click()
                case "storeWindowHandle":
                    element, result = self.find_element(command)

                case "doubleClick":
                    element, result = self.find_element(command)
                case _:
                    result = None
                    print(f"command {command['command'] } is not handled")

            return result, self.driver.title
        except Exception as e:
            log(e)
            logger.error(f"action error : {e} command : {command}")
        logger.info("Ending 'action'")

    def find_element(self, command):
        logger.info("Starting 'find_element'")
        result = None
        element = None
        for target in command["targets"]:
            try:
                locator = self.get_locator(target)
                trgt = target[0].split("=")[1]
                element = self.driver.find_element(locator,trgt )

                if element is None:
                    continue
                match element.tag_name:
                    case "label":
                        result = element.get_attribute("innerText")
                    case "button":
                        if element.text:
                            result = element.text
                    case "span":
                        if element.text:
                            result = element.text
                    case "a":
                        result = element.text
                        if result == "":
                            result = element.get_attribute("title")
                        elif result is None:
                            result = element.get_attribute("aria-label")
                    case "input":
                        result = self.driver.find_element_by_xpath(
                            '//label[@for="' + element.get_attribute('id') + '"]').text
                    case _:
                        result = element.tag_name
                        print(f"{element.tag_name} Didn't match a case")
                return element, result
            except Exception as e:
                print (f"{e} in  {__name__} ->find_element")
                logger.info(f" Error while searching for {target} or when getting text from it")

        logger.info("Ending 'find_element'")


    '''
     result = 'get_user_answer("' + question + '").then(ans=>{alert(ans);console.log(ans);' + setAnswer + '}) \
                                                                         .catch((error) => {console.error(error)});'

                            result = '(async () => {const answer = await get_user_answer("' + question + '");' \
                                     + setAnswer + '})()'


    '''

    def convert_to_js(self, data, action):
        try:
            js_data = {}
            key = action
            js_data[key] = []
            # for request in json.loads(data)[key]:
            for request in list(json.loads(data).values())[0]:
                part = {}
                part["name"] = request["name"]
                part["commands"] = []
                for action in request["commands"]:
                    if action["command"] == 'click':
                        target = action["target"];
                        target_parts = target.split("=");
                        if target_parts[0] == "id":
                            result = "$('#" + target_parts[1] + "').click()"
                        elif target_parts[0] == "css":
                            result = "$('" + target_parts[1] + "').click()"
                        elif target_parts[0] == "linkText":
                            result = "$('a:contains(" + target_parts[1] + "').click()"

                    elif action["command"] == 'type':
                        question = self.build_question(action['name'])
                        # result = 'answer = get_user_answer("' + question + '");'
                        target = action["target"];
                        target_parts = target.split("=");
                        if target_parts[0] == "id":
                            element = "$('#" + target_parts[1] + "')"
                        elif target_parts[0] == "css":
                            element = "$(" + target_parts[1] + ")"

                        setAnswer = element + ".val(ans)"
                        result = '(async () => {' \
                                 'await get_user_answer("' + question + '")' \
                                                                        '.then((ans)=>{' + setAnswer + ';})' \
                                                                                                       '.catch((error) => {console.log(error);})' \
                                                                                                       '.finally((ans)=> {ans  = null}); })();'
                        # 'simulate_input('+element+');'
                        # part["commands"].append(result);
                    # '.then((ans)=>{' + setAnswer + '.trigger("input");})' \

                    elif action["command"] == 'open':
                        temp_url = "https://login.bankhapoalim.co.il/ng-portals/auth/he/?frame=false"
                        result = "window.location = '" + action["target"] + "'"
                        # result = "window.location = '" + temp_url + "'"

                    elif action["command"] == 'setWindowSize':
                        width = action["target"].split("x")[0]
                        height = action["target"].split("x")[1]
                        result = "window.resizeTo(" + width + "," + height + ")";
                    elif action["command"] == 'selectFrame':
                        result = "parent.frames[" + action["target"].split("=")[1] + "]"
                    part["commands"].append(result);
                js_data[key].append(part)

        except Exception as e:
            log(e)
            logger.error("convert_to_js {}".format(e), exc_info=True)
            js_data = None
        return js_data


'''
    def tree_traverse(self):
        logger.info("Starting 'tree_traverse'")
        try:
            #parts = self.data[self.base]
            #self.convert_to_js(self.data)
            start = 0
            if self.is_logged:
                start = 1
                self.action(self.data["home"])
            part = self.data[self.name]
            for action in part[start:]:
                #part = [item for item in self.data[self.base] if item["name"] == action]
                part = [item for item in self.data[self.name] if item["name"] == action["name"]]

                # part = self.data[action]
                for command in part[start]["commands"]:
                    accessible_name, title = self.action(command)
                    command["name"] = accessible_name
                    command["title"] = title
            script = json.dumps(self.data)
            Sites.objects.filter(name=self.name).update(script=script)
        except Exception as e:
            logger.error("traverse error : {} {}".format(e, part))
'''
