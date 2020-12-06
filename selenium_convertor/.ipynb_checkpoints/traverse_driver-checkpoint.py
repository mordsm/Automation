import json
import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
import vlc
logger = logging.getLogger(__name__)
from voice_chat.models import Sites
from gtts import gTTS
from langdetect import detect
from googletrans import Translator

translator = Translator()

'''
     def __init__(self, file):
       with open(file, 'r') as f:
           self.data = json.load(f)
   '''


class Traverse():

    def __init__(self, name, script):
        self.name = name
        self.data = json.loads(script)
        self.driver = webdriver.Chrome()
        self.vars = {}

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

    def get_locator(self, target):
        if target[0].startswith("css"):
            return By.CSS_SELECTOR
        elif target[0].startswith("xpath"):
            return By.XPATH
        elif target[0].startswith("id"):
            return By.ID

    def action(self, command):
        try:
            result = None
            if command["command"] == "open":
                element = self.driver.get(self.data["url"] + command["target"])
                result = self.driver.title

            elif command["command"] == "set_window_size":
                element = self.driver.set_window_size(command["target"])
            elif command["command"] == "selectFrame":
                time.sleep(1)
                frame = command["target"].split("=")[1]
                if frame.isnumeric():
                    self.driver.switch_to.frame(int(frame))
                elif frame == "parent":
                    self.driver.switch_to.default_content()
                # self.wait_for_window()

            elif command["command"] == "click":
                element, result = self.find_element(command)
                if element:
                    try:
                        element.click()
                        lang = detect(result)

                        if lang == "he":
                            result_en =  translator.translate(result)
                            self.text_to_speech("please enter " +result_en.pronunciation)
                            print (result_en.pronunciation)
                        else:
                            self.text_to_speech("please enter " + result)
                            print(result.pronunciation)

                    except Exception as e:
                        print("error {} on command {} ".format(e, command))
                else:
                    print(command)

            elif command["command"] == "type":
                element, result = self.find_element(command)
                element.send_keys(command["value"])
            elif command["command"] == "mouseOver":
                element, result = self.find_element(command)
            elif command["command"] == "mouseOut":
                element, result = self.find_element(command)
            elif command["command"] == "doubleClick":
                element, result = self.find_element(command)
                element.click()
            elif command["command"] == "storeWindowHandle":
                element, result = self.find_element(command)

            elif command["command"] == "doubleClick":
                element, result = self.find_element(command)

            return result, self.driver.title
        except Exception as e:
            logger.error("action error : {}".format(e))

    def find_element(self, command):
        result = None
        element = None
        for target in command["targets"]:
            try:
                element = self.driver.find_element(self.get_locator(target), target[0].split("=", 1)[1])
                if element.tag_name == "span":
                    if element.text:
                        result = element.text
                        break
                elif element.tag_name == "input":
                    result = self.driver.find_element_by_xpath(
                        '//label[@for="' + element.get_attribute('id') + '"]').text
                    break
                elif element.tag_name == "button":
                    result = element.text
                    break
                elif element.tag_name == "a":
                    result = element.text
                    if result == "":
                        result = element.get_attribute("title")
                    if result == None:
                        result = element.get_attribute("aria-label")
                    break
            except Exception as e:
                pass
        return element, result

# traverse = Traverse("save_lastyear_expenses_to_excel.side")
# traverse.traverse()
