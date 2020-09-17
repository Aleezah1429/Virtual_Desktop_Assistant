from VDA.Engine import StartUp
from VDA.TakeCommand import CommandTaker
from googlesearch import search
import wikipedia


class Searcher:
    """This class allow us to search using google search engine and wikipedia"""
    sp = StartUp()  # COMPOSITION

    def GoogleSearch(self):  # It searches according to Google and give the links
        self.sp.Speak("what do you want to search?")
        print("what do you want to search?")
        result = CommandTaker().MicroPhone()
        for results in search(result, tld="co.in", num=10, stop=10, pause=2):
            print(results)

    def WikipediaSearch(self):   # It searches according to Wikipedia and gives a short paragraph
        self.sp.Speak('Searching Wikipedia...')
        print("Searching Wikipedia...")
        self.sp.Speak("what do you want to search?")
        print("what do you want to search?")
        query = CommandTaker().MicroPhone().replace("wikipedia", "")
        try:
            results = wikipedia.summary(query, sentences=2)
            self.sp.Speak("According to Wikipedia")
            print("According to Wikipedia")
            print(results)
            self.sp.Speak(results)
        except:
            print("Sorry I can not found it.Say Something else!")
            self.sp.Speak("Sorry I can not found it.Say Something else!")
            self.WikipediaSearch()
        return None
