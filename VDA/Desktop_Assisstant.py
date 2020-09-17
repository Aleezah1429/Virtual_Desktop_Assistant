from VDA.TakeCommand import CommandTaker
from VDA.Engine import StartUp
from VDA.SendEmail import EmailSender
from VDA.Entertainment import Entertainment
from VDA.Information import Information
from VDA.ApplicationOpener import AppOpener
from VDA.Greet import Greeting
from VDA.Search import Searcher
from VDA.Browser import WebsiteBrowser

#Aggregiation
S = Searcher()
W = WebsiteBrowser()
I = Information()
J = Entertainment()
G = Searcher()
A = AppOpener()

class Main:
    Greeting().Greet()
    def main_method(self):
        while True:
            print("What can I do for you?")
            StartUp().Speak("What can I do for you?")
            query = CommandTaker().MicroPhone().lower()

            if 'wikipedia' in query:
                S.WikipediaSearch()

            elif 'website' in query:
                W.OpenWebsite()

            elif 'time' in query:
                I.ShowTime()

            elif 'email' in query:
                try:
                    StartUp().Speak("What should I say?")
                    print("What should I say?")
                    content = CommandTaker().MicroPhone()
                    E = EmailSender(content)
                    E.SendEmail()
                    StartUp().Speak("Email has been sent!")
                    print("Email has been sent!")
                except Exception as e:
                    print(e)
                    StartUp().Speak("Sorry I am not able to send this email")


            elif "weather" in query:
                I.WeatherForecast()

            elif "news" in query:
                I.GoogleNews()

            elif "joke" in query:
                J.TellJokes()


            elif "google search" in query:
                G.GoogleSearch()

            elif "song" in query or "music" in query:
                StartUp().Speak("Tell me the genre you want to Listen!")
                print("Tell me the genre you want to Listen!")
                print("  1.Naat\n  2.POP\n  3.National Song\n  4.Sufi")
                song = CommandTaker().MicroPhone().lower()
                if "naat" in song:
                    Entertainment().Play_NAAT()
                elif "pop" in song:
                    Entertainment().Play_POP()
                elif "national song" in song:
                    Entertainment().Play_National_song()
                elif "sufi" in song:
                    Entertainment().Play_Sufi()

            elif "open application" in query:
                A.OpenApplication()

            elif "background" in query:
                A.desktop_background()

            elif "shutdown" in query or "terminate" in query:
                print("ok bye take care")
                StartUp().Speak("ok bye take care")
                break
            else:
                print("Command not found.")
                StartUp().Speak("Command not found")

Main().main_method()
