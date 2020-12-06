import speech_recognition as sr
import logging
logger = logging.getLogger(__name__)

fsm = {


}
def main():

    r = sr.Recognizer()
    transcript = ""
    while True:
        with sr.Microphone() as source:
            print("Please say something ")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source,timeout=5)

            print("Reconizing Now ... ")

            try:
                transcript = r.recognize_google(audio)
                print("You have said : " + transcript)

                #web.get(path).open(dest)

            except Exception as e:
                print("Error : " + str(e))

        if transcript.strip() == 'quit':
            break

def get_text():

    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Please say something ")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source,timeout=5)
            logger.info("Reconizing Now ... ")

            try:

                transcript = r.recognize_google(audio)
                if transcript == "quit":
                    return None
                print("You have said : " + transcript)
                return transcript
            except Exception as e:
                logger.error("Error : " + str(e))
                print ("Can you say it again or say <quit> to leave")



if __name__ == "__main__":

    main()