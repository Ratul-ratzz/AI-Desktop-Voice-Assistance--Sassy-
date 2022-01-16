# import audioop
from posixpath import expanduser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
from wikipedia.wikipedia import languages
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')  #voice gulo k ney
voices =engine.getProperty( 'voices')
print (voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour <= 12:
        speak ("Good Morning!") 
    elif hour >=12 and hour <18:
        speak ("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Sasssy sir, please tell me how may I help you ")

def takeCommand():    #it takes microphone er input from the user and string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    
    try: 
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")   
    
    except Exception as e:
        #print(e)
        print("Say that again please.....")
        return "None"
    return query

def sendEmail(to,content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email@gmail.com','your-password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()

if __name__=="__main__":
    #wishme()
  if 1:
    while True:
       query = takeCommand().lower()
        #logic on executing task based von query

       if 'wikipedia' in query:
           speak('searching wikipedia......')
           query = query.replace("wikipedia","")
           results = wikipedia.summary(query, sentences =2)
           speak("According to wikipedia")
           print(results)
           speak(results)
        
    
       elif 'open youtube' in query: 
           webbrowser.open("youtube.com")
            
       elif 'open google' in query:
           webbrowser.open("google.com")
        
       elif 'open stackoverflow' in query:
           webbrowser.open("stackoverflow.com")

        # elif 'play music' in query:
        #     music_dir = D:\\#song location
            #  songs = os.listdir(music_dir)
            #  print(songs)
            # os.startfile(os.path.join(music_dir,songs[0]))

       elif 'the time' in query:
            strTime = datetime.datetime.now().strtime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")

       elif 'open code' in query:
            codePath = "C:\\Users\\intel\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

       elif'email to harry' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "yourEmail@gmail.com"
                sendEmail (to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I cant send email")



        




