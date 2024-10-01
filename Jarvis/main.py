#My Jarvis Project!
import openai
import speech_recognition as sr
import methods as meth
import time
import webbrowser as wb
import os
import pyautogui
import pyperclip
# import threading  ##For interupting jarvis response!

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
        return 1
    except sr.RequestError as e:
        print(f"Google Speech Recognizer error; {e}")
        return 1

def start():
    time.sleep(1)  # Wait for 2 seconds
    user_cmd = speech_2_text(r)
    while user_cmd == 1:
        user_cmd = speech_2_text(r)
    return user_cmd

def init():
    user_cmd = speech_2_text(r)
    while user_cmd == 1:
        user_cmd = speech_2_text(r)
    return user_cmd

def main():# Main loop
    openai.api_key = "api_key"
    model = "gpt-4o-mini"

    user_cmd = init()  # Starting 
    if user_cmd.lower() in ["jarvis", "hey jarvis", "bro"]:
        meth.jarvis_activation()
        while (True):
            flag = 0
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
                    time.sleep(2)
                    if("weather" in user_cmd): # Gets weather
                        pyautogui.doubleClick(x=361, y=418)
                        pyautogui.hotkey('ctrl', 'c')
                        pyautogui.click(x=1893, y=20)
                        time.sleep(1)
                        weather_info = pyperclip.paste()
                        weather_text = f"Now the weather is {weather_info} degree celcius"
                        meth.jarvis_response(weather_text)
                        os.system("taskkill /f /im opera.exe >nul 2>&1")
                    flag = 1

                if ("jarvis open youtube" in user_cmd.lower()):
                    if ("jarvis open youtube" in user_cmd.lower()):
                        user_cmd = user_cmd.lower()
                        user_cmd = user_cmd.replace("jarvis open youtube ", "")
                    wb.open_new_tab('https://www.youtube.com')
                    time.sleep(4)
                    pyautogui.click(706, 140)  # Move the mouse to XY coordinates and click it.
                    pyautogui.write(user_cmd, interval=0)
                    pyautogui.press('enter')
                    flag = 1
                
                if ("jarvis open opera browser" in user_cmd.lower()):
                    os.startfile("C:\\Users\\arjun\\AppData\\Local\\Programs\\Opera\\opera.exe")
                    flag = 1

                if ("jarvis open vmware" in user_cmd.lower()):
                    os.startfile("C:\\Program Files (x86)\\VMware\\VMware Player\\vmplayer.exe")
                    flag = 1

                if ("jarvis close" in user_cmd.lower() and "application" in user_cmd.lower()):
                     text_list = user_cmd.lower().split()
                     word_to_keep = ["opera","vmware"]
                     app = [word for word in text_list if word in word_to_keep]
                     if app[0] in ["opera", "vmware"]:
                         os.system(meth.close_app_path[app[0]])
                     else:
                         print("No path for application available!")
                     flag = 1

                if flag == 0:
                    try:#openAI API integration!
                            response = openai.ChatCompletion.create(model=model,messages=[{"role": "system", "content": "You are Jarvis, Arjun's helpful assistant."},{"role": "user", "content": user_cmd}],max_tokens=350)
                    # "choices": [{"index": 0,"message": {"role": "assistant","content": "\n\nHello there, how may I assist you today?",},"logprobs": null,"finish_reason": "stop"}],
                            generated_text = response['choices'][0]['message']['content'].strip()
                            print(f"\nJarvis - {generated_text}")
                            ## Working on itt!!
                            # stop_thread = threading.Thread(target=meth.interrupt_jarvis_response)
                            # stop_thread.start()  #If you want to interrupt jarvis!  
                            meth.jarvis_response(generated_text)
                            # stop_thread.join()

                    except openai.error.OpenAIError as e:
                        print(f"OpenAI API error: {e}")

            else:
                print("No command detected. Waiting for a valid command.")
                time.sleep(1)

if (__name__ == "__main__"):
    main()