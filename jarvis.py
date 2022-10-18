# JUST A RATHER VERY INTELLIGENT SYSTEM 
import datetime
import pyttsx3 # text to speech library
import wikipedia
import webbrowser
import os
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("good morning sir")
    
    if hour>=12 and hour<18:
        speak("good afternoon sir")
    
    else:
        speak("good evening sir")

    speak("I am jarvis, how may I help you?")

    
def takecommand():
    ''' it takes microphone input from user and returns string output '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
        
    except Exception as e:
        # print(e)
        print("please say that again! \n")
        return "None"
    return query



if __name__ == "__main__":
    wishme()
    query = takecommand().lower()
    
    if 'wikipedia' in query:
        speak("searching wikipedia")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 2)
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    
    elif 'open google' in query:
        webbrowser.open("google.com")
    
    elif 'open chess.com' in query:
        webbrowser.open("chess.com")
    
    elif 'time' in query:
        strtime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir, the time is {strtime}")
        
    elif 'open code' in query:
        codepath = "C:\\Users\\PARTH SARDA\\Desktop\\parth\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)

