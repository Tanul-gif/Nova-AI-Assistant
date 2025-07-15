# import speech_recognition
# import pyttsx3
# import cv2
# import torch
import webbrowser
import os
from voice_module import speak, listen
import requests
from utils.time_utils import get_current_date,get_current_time,get_time_greeting


def smart_open_website(site_name):
    base_domains = ['.com', '.org', '.in', '.co.in', '.net']
    
    site_name_cleaned = site_name.replace(" ","")
    
    for ext in base_domains:
        url = f"https://{site_name_cleaned}{ext}"
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                webbrowser.open(url)
                return
        except:
            continue

    # Fallback to Google search
    query = site_name.replace(" ", "+")
    webbrowser.open(f"https://www.google.com/search?q={query}")
    
speak("Hello, I am Nova. how can i help you")
while True:
    command = listen()

    if "hello nova" in command or "hello" in command or "hi" in command:
        speak(get_time_greeting())
        speak("how can i help you")
    elif "your name" in command:
        speak("My name is Nova, your personal ai assistant")
    elif "exit" in command or "stop" in command or "quit" in command:
        speak("Goodbye")
        exit()
    elif "time" in command:
        speak(get_current_time())
    
    elif "date" in command:
        speak(get_current_date())
            
    # else:
    #     speak("you said: " + command)
    
    elif "open file" in command or "open folder" in command or "open florida" in command:
        speak("Please tell me the name of the file or folder you want to open.")
        target = listen().strip().lower()

        search_paths = [
            "D:\\",
            os.path.expanduser("~/Desktop"),
        ]

        found = False

        for path in search_paths:
            for root, dirs, files in os.walk(path):
                if "folder" in command:
                    for folder in dirs:
                        if target in folder.lower():
                            full_path = os.path.join(root, folder)
                            os.startfile(full_path)
                            speak(f"Opening folder {folder}")
                            found = True
                            break
                elif "file" in command:
                    for file in files:
                        if target in file.lower():
                            full_path = os.path.join(root, file)
                            os.startfile(full_path)
                            speak(f"Opening file {file}")
                            found = True
                            break
                if found:
                    break
            if found:
                break

        if not found:
            speak("Sorry, I couldn't find that.")


        