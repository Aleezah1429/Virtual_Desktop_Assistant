import speech_recognition as sr


class CommandTaker:
    """This Class takes input from user in the form of voice and return string after processing it """

    def MicroPhone(self):

        self.recognize = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")
            self.recognize.pause_threshold = 1
            self.recognize.adjust_for_ambient_noise(source, duration=1)
            self.audio = self.recognize.listen(source)

        # TRY EXCEPTION In try block the User Command is recognized by google API and if it will not recognize our
        # voice the except block will execute.

        try:
            print("Recognizing...")
            query = self.recognize.recognize_google(self.audio, language='en-in')
            print(f"User said: {query}\n")

        except:
            print("Say that again please...")
            return "None"

        return query


CT = CommandTaker()

