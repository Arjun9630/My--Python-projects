import pyttsx3 as tts
import speech_recognition as sr

user_cmd = ""

# Jarvis activation
def jarvis_activation():
    engine = tts.init()
    engine.setProperty('rate', 140)
    engine.say("Jarvis activating!")
    engine.say("Hey, I am Jarvis! How may I help you?")
    engine.runAndWait()

# Listen method
def Listen(r):
    with sr.Microphone(device_index=2) as source:
        r.adjust_for_ambient_noise(source)
        print("Listening!")
        audio = r.listen(source, timeout=5)
        return audio

def jarvis_turnOff():
    engine = tts.init()
    engine.setProperty('rate', 140)
    engine.say("Jarvis shutting down!")
    engine.say("Bye until you call me again!")
    engine.runAndWait()

def jarvis_response(text):
    engine = tts.init()
    engine.setProperty('rate', 140)
    engine.say(text)
    engine.runAndWait()