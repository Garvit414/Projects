import subprocess
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import time
import datetime
import pyjokes
import requests
import bs4


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<17:
        speak("Good Afternoon Sir !")  
  
    else:
        speak("Good Evening Sir !") 
    speak("I am your Assistant...How may I help u??")    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print("User said:",query,"\n")
    except Exception as e:
        # print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
    return query
      

if __name__== "__main__":
    # speak("Hello sir!! How are you?")
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'who is' in query:
            speak('Searching Wikipedia...')
            query = query.replace("who is", "")
            results = wikipedia.summary(query, sentences = 1)
            speak("According to Wikipedia..")
            print(results)
            speak(results)

        elif 'what is' in query:
            speak('Searching Wikipedia...')
            query = query.replace("what is", "")
            results = wikipedia.summary(query, sentences = 1)
            speak("According to Wikipedia..")
            print(results)
            speak(results)
            
        elif "hello" in query:
            speak("Hello sir..")                

        elif 'you do' in query:
            speak("i can do a lot of things such as fetch information from wikipedia, open google, make u laugh through jokes, tell u current time and many more...")    
 
        elif 'open google' in query:
            speak("Welcome to Google\n")
            webbrowser.open("google.com")   

        elif 'the time' in query:
            strTime = time.strftime("%m-%d-%Y %T:%M%p")
            print(strTime)  
            speak(f"Sir, the time is {strTime}")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you?") 

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "made you" in query or "created you" in query:
            speak("I have been created by the Garvit.")    

        elif 'joke' in query or'jokes' in query:
            speak(pyjokes.get_joke())  

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)      

        elif 'exit' in query or 'quit' in query:
            speak("Thanks for giving me your time")
            exit()   
  
        elif 'alexa' in query:
            speak("I don't know Alexa, but I've heard of Alexa. If you have Alexa, I may have just triggered Alexa. If so, sorry Alexa.") 

        elif 'weather' in query or 'temperature' in query:
            try:
                speak("Tell me the city name.")
                city = takeCommand().lower()
                api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=eea37893e6d01d234eca31616e48c631"
                w_data = requests.get(api).json()
                weather = w_data['weather'][0]['main']
                temp = int(w_data['main']['temp'] - 273.15)
                temp_min = int(w_data['main']['temp_min'] - 273.15)
                temp_max = int(w_data['main']['temp_max'] - 273.15)
                pressure = w_data['main']['pressure']
                humidity = w_data['main']['humidity']
                visibility = w_data['visibility']
                wind = w_data['wind']['speed']
                sunrise = time.strftime("%H:%M:%S", time.gmtime(w_data['sys']['sunrise'] + 19800))
                sunset = time.strftime("%H:%M:%S", time.gmtime(w_data['sys']['sunset'] + 19800))

                all_data1 = f"Condition: {weather} \nTemperature: {str(temp)}°C\n"
                all_data2 = f"Minimum Temperature: {str(temp_min)}°C \nMaximum Temperature: {str(temp_max)}°C \n" \
                            f"Pressure: {str(pressure)} millibar \nHumidity: {str(humidity)}% \n\n" \
                            f"Visibility: {str(visibility)} metres \nWind: {str(wind)} km/hr \nSunrise: {sunrise}  " \
                            f"\nSunset: {sunset}"
                speak(f"Gathering the weather information of {city}...")
                print(f"Gathering the weather information of {city}...")
                print(all_data1)
                speak(all_data1)
                print(all_data2)
                speak(all_data2)

            except Exception as e:
                pass

        elif "latest news" in query:
            url="https://www.indiatoday.in/india"
            info_html = requests.get(url)   
            # print (info_html)
            info = bs4.BeautifulSoup(info_html.text, 'html.parser')
            # print(info.prettify)
            title=info.title
            print(title)
            info2=info.find('div', class_='content__section')
            # print(info2.prettify)
            new_info = info2.find('main', class_='main__content')
            # print(new_info)
            datan= new_info.find('div',class_='story__grid')
            # print(datan)
            data1=datan.findAll('h2')
            for i in data1[:4]:
                print(i.get_text())
                speak(i.get_text())
                
            # print(data1)

        else:
            speak("Please repeat...")         

