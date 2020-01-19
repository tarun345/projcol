

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

user="sir"

# required codes for speak function
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# speak function will pronounce string passed in argument
def speak(text):
    engine.say(text)
    engine.runAndWait()

# wishme function is for greetings acording to the time
def wishme():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        print("good morning "+user)
        speak("good morning "+user)

    elif hour>12 and hour<18:
        print("good afternoon "+user) 
        speak("good afternoon "+user)

    else :
        print("good evening "+user)
        speak("good evening "+user)

# takeCommand function is used to take the command from user by microhone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("listning...")
        r.pause_threshold=1
        audio = r.listen(source)
      
         
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(user+f" said :{query}\n")

    except Exception as e:
        print("did not get it, say that again")
        speak("did not get it, say that again")
        query = "None"

    return query


def initial():
    # will be desplayed when app starts
    print("initializing viras")
    speak("initializing viras")


    print("hello, my name is viras")
    speak("hello, my name is viras")

    wishme()

# this function is used for changing user name
def callWithName(name):
    print("you want me to call you '"+name+"'?")
    speak("you want me to call you '"+name+"'?")
    takeCommand()
    if 'yes' in query:
        global user
        user = name
        print("hello "+user)
        speak("hello"+user)
    
if __name__ == "__main__":

    initial()

    while True:

        print("how can i help you sir!")
        speak("how can i help you sir!")

        speak("press 1 for speak and 2 for type:")
        inType = input("press 1:for speak \n 2: for type:")

        if inType=="1":
            query = takeCommand().lower()

        elif inType=="2":
            query = input("type here:")

        else:
            print("invalid input")
            speak("invalid input")

        if 'wikipedia' in query:
            print("searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play songs' in query:
            music_dir = 'F:\\songs\\Mp3'
            songs = os.listdir(music_dir)
            print(songs)
            print("which song you want to play ?")
            speak("which song you want to play ?")

            speak("press 1 for speak and 2 for type:")
            songType = input("press 1:for speak \n 2: for type:")

            if songType=="1":
                vs = takeCommand().lower()

            elif songType=="2":
                vs = input("type here:")

            else:
                print("invalid input")
                speak("invalid input")
                continue

            if "number" in vs:
                num = int(vs.replace("number", ""))
                os.startfile(os.path.join(music_dir, songs[num]))
                input()

            else :
                print("try like this,\n number 5")    
                    
        elif 'play video songs' in query or 'play video' in query:
            music_dir = 'F:\\songs\\Mp4'
            songs = os.listdir(music_dir)
            print(songs)
            print("which video you want to play ?")
            speak("which video you want to play ?")

            speak("press 1 for speak and 2 for type:")
            songType = input("press 1:for speak \n 2: for type:")

            if songType=="1":
                vs = takeCommand().lower()

            elif songType=="2":
                vs = input("type here:")

            else:
                print("invalid input")
                speak("invalid input")
                continue
            

            if "number" in vs:
                num = int(vs.replace("number", ""))
                os.startfile(os.path.join(music_dir, songs[num]))

                input()

            else :
                print("try like this,\n number 5")   
                
        elif 'good bye' in query or 'goodbye' in query:
            input("are you sure, you want to quite")
            speak("are you sure, you want to quite")
            print("good bye, "+user)
            speak("good bye, "+user)
            exit()

        elif "call me" in query:
            name = query.replace("call me", "")
            callWithName(name)

        else:
            print("did not get it, try again!!!")
            speak("did not get it, try again!!!")
        
  