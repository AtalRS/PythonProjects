import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5') #To acces voices in windows
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishME():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good AfterNoon")
    elif hour>=18 and hour<24:
        speak("Good Evening")

    speak("I am Jarvis Sir. How may I help you?")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        speak("User Said")
        speak(query)
        #print(f"User said: {query}\n")

    except Exception :
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__=="__main__":
    wishME()
    while True:
        query = takeCommand().lower()


        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "play music" in query:
            music_dir = "E:\\music\\workout"
            songs = os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "time" in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")   
             speak(f"Sir the time is {strTime}")

        elif "quit" in query:
            speak("Thankyou Sir, Have a Good day!")
            exit()