import pyttsx3 as tts
import speech_recognition as sr
import keyboard
import time

speaking = False  # Global flag to track if speaking
user_cmd = ""
engine = tts.init()
close_app_path = {"opera" : "taskkill /f /im opera.exe >nul 2>&1", "vmware" : "taskkill /f /im vmplayer.exe >nul 2>&1"}

# Jarvis activation
def jarvis_activation():
    engine.setProperty('rate', 140)
    engine.say("Jarvis activating!")
    engine.say("Hey, I am Jarvis! How may I help you?")
    engine.runAndWait()

# Listen method
def Listen(r):
    with sr.Microphone(device_index=2) as source:
        r.adjust_for_ambient_noise(source)
        print("Listening!")
        audio = r.listen(source, timeout=10)
        return audio

def jarvis_turnOff():
    engine.setProperty('rate', 140)
    engine.say("Jarvis shutting down!")
    engine.say("Bye until you call me again!")
    engine.runAndWait()

def jarvis_response(text):
    global speaking
    speaking = True  # Set flag to indicate speaking
    engine.setProperty('rate', 150)
    engine.say(text)  # Queue the text to be spoken
    engine.runAndWait()  # Block until all speech has finished
    speaking = False  # Reset flag after speaking
 
# def interrupt_jarvis_response():  ###Working on ittt!!
#     print("Press 's' to stop the speech.")
#     while True:
#         if keyboard.is_pressed('s') and speaking:  # Check if speaking is true
#             engine.stop()  # Stop the current speech
#             print("Speech interrupted.")
#             break
#         time.sleep(0.1)