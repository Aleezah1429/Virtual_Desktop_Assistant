import pyowm
import requests
from bs4 import BeautifulSoup
import datetime
from VDA.Engine import StartUp
from VDA.TakeCommand import CommandTaker


class Information:
    """It provide daily google news , time and  weather condition of any city . """
    sp = StartUp()  # COMPOSITION

    def GoogleNews(self):  # It scrap the headlines from google news
        news_url = "https://news.google.com.pk/news/rss"
        page = requests.get(news_url)
        soup = BeautifulSoup(page.content, "html.parser")
        news = soup.find_all("title")
        no_news = 0
        for new in news:
            if no_news == 0:
                print(new.text)
            else:
                print(no_news, ".", new.text)
            self.sp.Speak(new.text)
            no_news += 1
            if no_news == 6:
                break
        return None

    def WeatherForecast(self):  # It tell us the weather conditions like maximum minimum temperature and status .
        try:
            self.sp.Speak("please tell the city name")
            self.city = CommandTaker().MicroPhone()
        except:
            self.WeatherForecast()
        owm = pyowm.OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
        obs = owm.weather_at_place(self.city)
        w = obs.get_weather()
        status = w.get_detailed_status()
        temp = w.get_temperature(unit='celsius')
        temperature = int(temp["temp"])
        max_temperature = int(temp["temp_max"])
        min_temperature = int(temp["temp_min"])

        self.sp.Speak(
            f"the status is {status}  the temp is {temperature}  the maximum temperature is {max_temperature}  the minimum temperature is {min_temperature}")
        print(
            f"The status is {status} \nThe temp is {temperature}  the maximum temperature is {max_temperature}  \nThe minimum temperature is {min_temperature}")
        return None

    def ShowTime(self):  # It tells the time .
        Time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Time : ", Time)
        self.sp.Speak(f"Ma'am, the time is {Time}")
        return None
