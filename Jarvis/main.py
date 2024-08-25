#My Jarvis Project!
import openai #While integrating openai! Not required as of now!
import speech_recognition as sr
import methods as meth
import time
import webbrowser as wb
import pyautogui

r = sr.Recognizer()

# Speech to text function
def speech_2_text(recognizer):
    try:
        audio = meth.Listen(recognizer)  # Gets the audio from meth.Listen
        user_cmd = recognizer.recognize_google(audio)  # Recognizes the speech
        print("Arjun - " + user_cmd)
        return user_cmd
    except sr.UnknownValueError:
        print("Could not understand the audio. Please speak clearly.")
        return ""
    except sr.RequestError as e:
        print(f"Google Speech Recognizer error; {e}")
        return ""

def start():
    time.sleep(1)  # Wait for 2 seconds
    return speech_2_text(r)

def init():
    return speech_2_text(r)

def main():# Main loop
    # openai.api_key = "api-key"
    # model = "gpt-3.5-turbo"

    user_cmd = init()  # Starting 
    if user_cmd.lower() in ["jarvis", "hey jarvis", "bro"]:
        meth.jarvis_activation()
        while (True):
            user_cmd = start()
            if (user_cmd):
                if (user_cmd.lower() == "jarvis turn off"):
                    meth.jarvis_turnOff()
                    break
                
                if ("jarvis open google" in user_cmd.lower()):
                    if ("jarvis open google" in user_cmd.lower()):
                        user_cmd = user_cmd.lower()
                        user_cmd = user_cmd.replace("jarvis open google ", "")
                    wb.open_new_tab('http://www.google.com')
                    time.sleep(2)
                    pyautogui.click(714, 513)  # Move the mouse to XY coordinates and click it.
                    pyautogui.write(user_cmd, interval=0)
                    pyautogui.press('enter')
                
                if ("jarvis open youtube" in user_cmd.lower()):
                    if ("jarvis open youtube" in user_cmd.lower()):
                        user_cmd = user_cmd.lower()
                        user_cmd = user_cmd.replace("jarvis open youtube ", "")
                    wb.open_new_tab('https://www.youtube.com')
                    time.sleep(4)
                    pyautogui.click(706, 140)  # Move the mouse to XY coordinates and click it.
                    pyautogui.write(user_cmd, interval=0)
                    pyautogui.press('enter')

                # try:   #openai integration! #No Money No API Key so could'nt try!
                #     response = openai.Completion.create(engine=model, prompt=user_cmd, max_tokens=50)
                #     generated_text = response.choices[0].text.strip()
                #     print(generated_text)
                #     meth.jarvis_response(generated_text)
                # except openai.error.OpenAIError as e:
                #     print(f"OpenAI API error: {e}")

            else:
                print("No command detected. Waiting for a valid command.")
                time.sleep(1)

if (__name__ == "__main__"):
    main()
