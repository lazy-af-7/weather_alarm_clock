import os
import datetime
import time
from playsound import playsound
from gtts import gTTS
import requests
import urllib


def get_Weather(city):
    #insert your api key from https://openweathermap.org/ below
    api_key=""
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+api_key+"0&units=metric")
    if response.status_code==200:
        dictionary=response.json()
        lst = dictionary["weather"]
        lst_1=dictionary["main"]
        # print(lst[0]['main'])
        # print(lst_1['feels_like'])

        weather="It's currently "+lst[0]["main"]+" and feels like "+str(lst_1["feels_like"]) + " degrees."
        return weather
    else:
        weather=" "
        print("Please enter the correct city name. You can check if your citys weather is available or not at https://openweathermap.org/",)
        return weather




def alarm_clock():
    date_entry = input('Enter a date in YYYY-MM-DD format\n')
    year, month, day = map(int, date_entry.split('-'))
    date1 = datetime.date(year, month, day)
    alltimes = input("Enter times in HH:MM\n").split()
    city= input("Enter the name of the city:\n")
    weather=get_Weather(city)

    for time in alltimes:
        hour, minutes = [int(i) for i in time.split(":")]
    
    
    while(True):
        if datetime.datetime.now().date()==date1 and datetime.datetime.now().hour==hour and datetime.datetime.now().minute==minutes:
            text="Wake up!"+weather
            print(text)
            language='en'
            myobj=gTTS(text=text,lang=language,slow=False)
            myobj.save("Alarm.mp3")
            playsound("Alarm.mp3")
            break

alarm_clock()