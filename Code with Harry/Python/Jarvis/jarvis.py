import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening !")
        
    speak("I am Christina Sir, Please tell me how may i help you")            


def takeCommand():
    #it takes microphone input from the user and returns string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("i am Listening ...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    
    try:
        print("Recognizing") 
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e :
        speak("Say that again Please ...")
        return "None"       
    return query

def sendEmail(to, content):
    server=smtplib.SMTP('smntp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('adityaroyal10@gamil.com','Aroyal10@#')
    server.sendmail('adityaroyal911@gmail.com','Aroyal10@#')
    server.close()

if __name__ == "__main__":
    speak(" How are you Aditya !")
    wishMe()
    
    while True:
        query = takeCommand().lower()
    
    #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("searching wikipedia ...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 
        
        elif 'play music' in query:
            music_dir = 'D:\\hp (Old Laptop) Documents\\AHLAWAT FOLDERS\\my folder\\c basics\\Removable Disk'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'time' in query :
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , the time is {strTime}") 
            
        elif 'email to aditya 911' in query:
            try:
                speak("What should I say ?")
                content = takeCommand()
                to = "adityaroyal911@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent !")
            except Exception as e :
                print(e)
                speak("Sorry my friend aditya bhai . I am not able to send this email")           
