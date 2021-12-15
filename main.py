import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import cv2 as cv

print("initialing jarvis")
MASTER = "Rohit.........."
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# speak fuction will pronouce the  string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    # print(hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning......" + MASTER)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon....." + MASTER)
    else:
        speak("Good Evening......" + MASTER)

    speak("I am jarvis..... How may I help you")


# this function will take command from microphone
def takeCommand():
    r = sr.Recognizer()
    # r.pyaudio_module = r.get_pyaudio()
    with sr.Microphone() as source:
        print("listening....")
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said :{query}\n")
        # speak("the user said" + query)

    except Exception as e:
        print("say that again...")
        query = None
    return query


# def sendEmail(to,content):
#     server=smtplib.SMTP('smtp.gmail.com',587)
#     sever.ehlo()
#     server.starttls()
#     server.login('Yourname@gmail.com','Password')
#     server.sendmail("chandarohit.14@gmail,com",to,content)
# server.close()
# main programme start here
# speak("Initializing jarvis")
def main():
    wishMe()
    query = takeCommand()

    # logic for executing tasks as per the query
    if 'wikipedia' in query.lower():
        speak('Seacrhing wikipedia....')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)


    elif 'open youtube' in query.lower():
        # new = 2
        open_youtube = webbrowser.open('https://www.youtube.com/')

    elif 'open google' in query.lower():
        open_google = webbrowser.open('https://google.com')

    # elif 'open facbook' in query.lower():
    #     open_facebook = webbrowser.open('https://www.facebook.com/')
    elif 'open stackoverflow' in query.lower():
        open_stackoverflow = webbrowser.open('https://stackoverflow.com/')
    elif 'open reddit' in query.lower():
        open_reddit = webbrowser.open('https://www.reddit.com/')

    elif 'play music' or 'play song' in query.lower():
        songs_dir = "E:\\music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))
    elif 'open spotify' in query.lower():
        open_spotify = webbrowser.open('https://open.spotify.com/')

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"the time is {strTime}")
        speak(f"the time is {strTime}")
    elif 'open eclipse' in query.lower():
        open_eclipse = "C:\\ecilipse_neon\\eclipse\\eclipse.exe"
        os.startfile(open_eclipse)
    # elif 'send email' in query.lower():
    #     try:
    #         speak("what should I send")
    #         content=takeCommand()
    #         to=-"chanda.rohit.14@gmail.com"
    #         sendEmail(to.content)
    #         speak(":Email has been sent succerfuly")
    #     except Exception as e:
    #         print(e)    
    elif 'open camera' in query.lower():

        capture = cv.VideoCapture(0)

        while True:
            isTrue, frame = capture.read()
            cv.imshow('Video', frame)
            if cv.waitKey(20) & 0xFF == ord('d'):
                break

        capture.release()
        cv.destroyAllWindows()


main()
