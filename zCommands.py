import subprocess
import os
from MachineLearning.get_answer import Fetcher


class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "yeah", "confirm"]
        self.cancel = ["no", "negative", "cancel"]

    def discover(self, text):
        if "what" in text and "name" in text:
            if "my" in text:
                self.respond("You haven't told me your name! ")
            else:
                self.respond("My name in Zoleikha Commander. How are you?")
        # if "open" or "launch" in text:
        #     app = text.split(" ", 1)[-1]
        #     self.respond("opening" + app)
        #     os.system("open -a " + app + ".app")
        else:
            f = Fetcher("http://www.google.ca/search/?q=" + text)
            answer = f.lookup()
            self.respond(answer)

    def respond(self, response):
        print(response)
        subprocess.call("say " + response, shell=True)