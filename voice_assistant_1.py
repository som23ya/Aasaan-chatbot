import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import chatbox


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello ! I am Aasaan- your interactive help!. what do you want to do?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aasaan listening...")

        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Aasaan recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")


    except Exception as e:
        # print(e)
        print("Once more please! ")

        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia-")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("https://www.youtube.com/watch?v=")

        elif 'google' in query:
            webbrowser.open("google.com")
        elif 'stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com/")
        elif 'search for' in query:
            print("You asked : {}".format(query))
            url = 'https://www.google.co.in/search?q='
            search_url = url + query
            webbrowser.open(search_url)

        elif 'what is' in query or 'kya' in query or 'kyon' in query:

            print("You asked : {}".format(query))
            url = 'https://www.google.co.in/search?q='
            search_url = url + query
            webbrowser.open(search_url)

        elif 'who is' in query:

            print("You asked : {}".format(query))
            url = 'https://www.google.co.in/search?q='
            search_url = url + query
            webbrowser.open(search_url)


        elif 'what is' in query or 'why' in query or 'how ' in query:

            print("You said : {}".format(query))
            url = 'https://www.google.co.in/search?q='
            search_url = url + query
            webbrowser.open(search_url)


        elif 'play music' in query:
            music_dir = 'D:\machine learning\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'quit' in query or 'bye' in query:
            speak("Aasaan out! It was nice helping you. Come again soon. Bye")
            exit()

        elif 'notes' in query:
            codePath = ""
            os.startfile(codePath)

