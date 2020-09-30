import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests
import smtplib
import datetime





engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
rate=engine.getProperty('rate')
# print(rate)
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning Master!")
    elif hour>=12 and hour<18:
        speak("Good Aftrnoon Master!")
    else:
        speak("Good Evening master!")
    speak("Hi This is Luna. Please tell me how may i help you")

 # it takes microphone input from user and returm string output
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)

        try:
            print("Recognizing....")
            quary=r.recognize_google(audio,language='en-in')
            # quary=input("enter your quary\n")
            print(f"User said:{quary}\n")

        except Exception as e:
            print(e)
            print("say that again please i did not recognize...")
            speak("say that again please i did not recognize your voice..")
            return "None"
        return quary

def sendEmail(to,content):
    server=smtplib.SMTP('smpt.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()


def givenews():
    apiKey = '528d8984821147139e3ea2b7a9d191bf'
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={apiKey}"
    r = requests.get(url)
    data = r.json()
    data = data["articles"]
    flag = True
    count = 0
    for items in data:
        count += 1
        if count > 10:
            break
        print(items["title"])
        to_speak = items["title"].split(" - ")[0]
        if flag:
            speak("Today's top ten Headline are : ")
            flag = False
        else:
            speak("Next news :")
        speak(to_speak)


if __name__ == '__main__':
    wishMe()
    while(True):
        quary=takeCommand().lower()

        if 'wikipedia' in quary:
            speak('Searching wikipedia..')
            quary=quary.replace("wikipedia","")
            results=wikipedia.summary(quary,sentences=2)
            speak('Accroding to Wikipedia')
            print(f"Luna said:{results}")
            speak(results)
        elif 'how are you' in quary:
            speak("i am fine sir, tell me how can i help you?")


        elif 'open youtube' in quary:
            webbrowser.open('youtube.com')

        elif 'open google' in quary:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in quary:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in quary:
            mus_dir='C:\\Users\\ABHAY RAJ\\Documents\\Sound recordings'
            songs=os.listdir(mus_dir)
            print(songs)
            os.startfile(os.path.join(mus_dir,songs[0]))

        elif 'the time' in quary:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"sir, the time is{strTime}")

        elif 'open code' in quary:
           codePath="C:\\Program Files\\JetBrains\PyCharm Community Edition 2020.1\\bin\\pycharm64.exe"
           os.startfile(codePath)

        elif 'email to abhay' in quary:
            try:
                speak("What should i say?")
                content=takeCommand()
                to="Youremail@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry master i am not able to send this email right now..please try after sometime")
        elif ' who are you' in quary:
            print("I am your AI assistant Luna made by Mr. Abhay" )
            speak("I am your assistant Luna  made by Mr Abhay")


        elif 'news' in quary or 'headlines' in quary:
            givenews()
        elif 'what' in quary or 'who' in quary or 'where' in quary or 'can you' in quary:
            webbrowser.open(f"https://www.google.com/search?&q={quary}")
            speak(wikipedia.summary(quary, sentences=2))
        elif 'awesome' in quary or 'wow' in quary or 'amazing' in quary or 'wonderful' in quary:
            speak("Thank you sir, i am here for you")
        else:
            speak("Command unknpwn not programmed for this command")

        if 'quit' in quary or 'exit' in quary or 'close' in quary:
            speak("Thank you,have a good day ahead..")
            exit()


