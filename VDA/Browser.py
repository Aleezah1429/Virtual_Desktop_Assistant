from VDA.Engine import StartUp
from VDA.TakeCommand import CommandTaker
import webbrowser


class WebsiteBrowser:
    """It opens a website according to our choice"""
    def OpenWebsite(self):
        StartUp().Speak("please tell the website name")
        print("please tell the website name")
        a = CommandTaker().MicroPhone().lower()
        link = "https://www." + a + ".com"
        webbrowser.open(link)
        print("Website of",a,"opened successfully!")
        StartUp().Speak(f"Website of {a} opened successfully!")
        return None

