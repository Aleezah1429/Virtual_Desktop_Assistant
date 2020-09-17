from VDA.Engine import StartUp

import datetime


class Greeting:
    """It greets the user according to the time ."""
    sp = StartUp()
    hour = int(datetime.datetime.now().hour)
    print("Hey! I am JARVIS . Your Desktop Assistant")
    sp.Speak("Hey! I am JARVIS")
    sp.Speak("Your Desktop Assistant.")

    def Greet(self):
        if 0 <= self.hour < 12:
            self.sp.Speak("Good Morning!")
            print("Good Morning!")

        elif 12 <= self.hour < 18:
            self.sp.Speak("Good Afternoon!")
            print("Good Afternoon!")

        else:
            self.sp.Speak("Good Evening!")
            print("Good Evening!")

