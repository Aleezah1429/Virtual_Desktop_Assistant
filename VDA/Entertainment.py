import random
import requests
from bs4 import BeautifulSoup
import os
from VDA.Engine import StartUp


class Entertainment:  # COMPOSITION
    sp = StartUp()

    def TellJokes(self):
        jokes_url = "https://icanhazdadjoke.com/"
        page = requests.get(jokes_url)
        soup = BeautifulSoup(page.content, "html.parser")
        jokes = soup.find("p", {"class": "subtitle"})
        print(jokes.text)
        self.sp.Speak(jokes.text)
        return None

    @staticmethod
    def Play_NAAT():
        lst_naat = ["NAAT\\naat1.mp3",
                    "NAAT\\naat2.mp3",
                    "NAAT\\naat3.mp3"]
        os.system(random.choice(lst_naat))

    @staticmethod
    def Play_National_song():
        lst_Nationalsong = ["National_song\\n1.mp3",
                            "National_song\\n2.mp3"]
        os.system(random.choice(lst_Nationalsong))

    @staticmethod
    def Play_POP():
        lst_POP = ["POP\\pop1.mp3",
                   "POP\\pop2.mp3",
                   "pop3.mp3"]
        os.system(random.choice(lst_POP))

    @staticmethod
    def Play_Sufi():
        lst_sufi = ["SUFI\\sufi1.mp3",
                    "SUFI\\sufi2.mp3"]
        os.system(random.choice(lst_sufi))
