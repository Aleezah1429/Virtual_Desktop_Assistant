import pyttsx3  # text to audio library

engine = pyttsx3.init("sapi5")
rate = engine.getProperty("rate")
engine.setProperty("rate", 150)


class StartUp:
    """It coverts text in to audio format"""

    def Speak(self, audio):  # audio is a string type
        engine.say(audio)
        engine.runAndWait()
