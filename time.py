
from sqlite3 import Time
import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
from secret import senderemail , epwd, to
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
import requests
from newsapi import NewsApiClient
import clipboard
import os 
import pyjokes
import time as tt
import string
import random
import psutil
from nltk.tokenize import word_tokenize

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishme():
    speak("Welcome back sir")



def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)



def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Today's date is")
    speak(date)
    speak(month)
    speak(year)  
       


def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12 :
        speak("good morning sir" )
    elif hour >=12 and hour <15:
        speak("Good afternoon sir")
    elif hour >=15 and hour <18:
        speak("Good Evining sir")
    else:
        speak("Good night sir")        



    speak("vision at your service ,please tell me how can i help you?")

wishme()               
greeting()    


    
def takecommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = "en-IN")
        print(query)

    except Exception as e:
        print (e)
        speak ("say that again please")
        return "None"
    return query    



def sendEmail(content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(senderemail , epwd)
    server.sendmail(senderemail , to , content)
    server.close()



def  sendwhatsmsg(phone_no , message):
    Message = message  
    wb.open('https://web.whatsapp.com/send?phone=' +phone_no+ '&text=' +Message)
    sleep(10)
    pyautogui.press('enter')



def searchgoogle():
    speak("what should i search ?")    
    search = takecommandMic()
    wb.open('https://www.google.com/search?q=' +search)



def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)    



def covid():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all') 
    data = r.json()
    covid_data = f'Confirmed cases : {data["cases"]} \n Deaths : {data["deaths"]} \n Recovered : {data["recovered"]}'
    print(covid_data)
    speak(covid_data)



def screenshot():
    name_img = tt.time()
    name_img =f'C:\\Users\\Rhutvik Teli\\Downloads\\Learn To Create Advance AI Assistant (JARVIS 2.0)With Python\\screenshot\\{name_img}.png'    
    img = pyautogui.screenshot(name_img)
    img.show()


def passwordgen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passlen  = 8
    s =[]
    s.extend(list(s1))    
    s.extend(list(s2))  
    s.extend(list(s3)) 
    s.extend(list(s4)) 

    random.shuffle(s)
    newpass = ("" . join(s[0:passlen]))
    print(newpass)
    speak(newpass)


def flip():
    speak("Ok sir , flipping a coin")
    coin =['heads' , 'tails']
    toss =[]
    toss.extend(coin)
    random.shuffle(toss)
    toss =(" ".join(toss[0]))
    print("i flipped a coin and you got" +toss)
    speak("i flipped a coin and you got" +toss)


def roll():
    speak("ok sir , rolling a die for you")
    die=['1','2','3','4','5','6']   
    roll =[]
    roll.extend(die)
    random.shuffle(roll) 
    roll = ("" .join(roll[0]))
    print("i rolled a die and you got"+roll)
    speak("i rolled a die and you got"+roll)



def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu is at" +usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
     


def news():
    newsapi =NewsApiClient(api_key = '6fd87fff9486433e8cede26548ccaf89')
    speak("what topic to listen news about")
    topic = takecommandMic()
    data = newsapi.get_top_headlines (q = topic ,
                                       language = 'en' ,
                                       page_size = 5)

    newsdata = data['articles']
    for x , y in  enumerate (newsdata):
        print(f'{x}{y ["description"]}')
        speak(f' {x}{y ["description"]}')


    speak("that's for now i'll update you in some time")     











                             

if __name__ == "__main__":
    wakeword = 'vision'
    while True:
        query = takecommandMic().lower()
         
        
        if wakeword in query:


            if 'time' in query:
                time()


            elif 'date' in query:
                date()


            elif 'email' in query:
                try:
                    speak("what should i say?")
                    content = takecommandMic()
                    sendEmail(content)
                    speak("email has been send")
                except Exception as e:
                    print(e)
                    speak("Unable to send the email ")


            elif 'message' in query:
                user_name ={
                    'vision': '+91 9545965062'
                    
                }        
                try:
                    speak("To whom want to send whatsapp message?")
                    name = takecommandMic()
                    phone_no = user_name[name]
                    speak("what is the message?")
                    message = takecommandMic()
                    sendwhatsmsg(phone_no , message)
                    speak("Message hass been send")
                except Exception as e:
                    print(e)
                    speak("unable to send message")    



            elif 'wikipedia' in query :
                speak("searching on wikipedia....")
                query = query.replace("wikipedia" , " ")
                result = wikipedia.summary(query, sentences = 2)
                print(result)
                speak (result)    



            elif 'google' in query:
                searchgoogle()  



            elif 'youtube' in query: 
                speak("what i should search on youtube") 
                topic = takecommandMic()
                pywhatkit.playonyt(topic)     



            elif 'weather' in query:
                speak("which city's wheather?")
                city = takecommandMic()
                url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=6cc2d6aed8de100ee02fd53388b92648'      
                res = requests.get(url) 
                data = res.json()


                weather = data['weather'] [0] ['main']
                temp = data['main'] ['temp']
                desp = data['weather'] [0] ['description']
                temp = round ((temp - 32) * 5/9)
                print(weather)
                print(temp)
                print(desp)
                speak(f'weather in{city} city is like')
                speak('Temprature: {} degree celcuis'.format(temp))
                speak('weather is {}'.format(desp))


            elif 'remember that' in query:
                speak("what should i remember")
                data = takecommandMic()
                speak("you said me to remember that" +data)
                remember =open('data.txt' , 'w')
                remember.write(data)
                remember.close()


            elif "do you know anything" in query:
                remember = open('data.txt' , 'r')
                speak("you told me to remember that" +remember.read())   


            elif 'read' in query:
                text2speech()



            elif 'news' in query:
                news()    



            elif 'covid' in query:
                covid()    



            elif 'open' in query:
                os.system('explorer c://{}'.format (query.replace('open' , '')))



            elif 'open code' in query:
                codepath = 'C:\\Users\\Rhutvik Teli\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe'    
                os.startfile(codepath)



            elif 'joke' in query:
                speak(pyjokes.get_joke())    



            elif 'screenshot' in query:
                screenshot()



            elif 'password' in query:
                passwordgen()    



            elif 'flip' in query:
                flip()    


            elif 'roll' in query:
                roll()


            elif 'cpu' in query:
                cpu()       

            elif 'offline' in query:
                quit()    



