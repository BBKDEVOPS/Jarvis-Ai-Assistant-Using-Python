
import random
import time

import requests

from FUNCTION.listen import listen
from FUNCTION.speak import speak


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

def advice():
    while True:
        x = [600, 550, 580, 400, 3000, 800, 700, 8200 ,8000, 50 ,568]
        x = random.choice(x)
        time.sleep(x)
        speak("I have some suggestion for you, sir")
        text = listen().lower()
        if "yes tell me" in text or "yes" in text:
            advice = get_random_advice()
            speak(advice)
            pass
        else:
            speak("no problem, I think you need some advice, so I'll give you one.")
            pass
