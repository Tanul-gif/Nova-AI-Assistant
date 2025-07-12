# import speech_recognition
# import pyttsx3
# import cv2
# import torch
import webbrowser
import os
# print("All libraries installed")
from voice_module import speak, listen
import requests

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

    if "hello" in command:
        speak("Hi there! I'm always ready.")
    elif "your name" in command:
        speak("My name is Nova, your personal ai assistant")
    elif "exit" in command or "stop" in command or "quit" in command:
        speak("Goodbye")
        exit()
    # else:
    #     speak("you said: " + command)
    
    elif "open" in command and "website" in command or "web site" in command:
        speak("Which website you want to open")
        site = listen()
        smart_open_website(site)
        # if site:
        #     base_site = site.replace(" ","").lower()
            
        #     # try common domains
        #     for ext in [".com",".org",".in",".co.in"]:
        #         url = f"https://{base_site}{exit}"
        #         try:
        #             webbrowser.open(url)
        #             speak(f"opening {site}")
        #             break
        #         except:
        #             continue
        #     else:
        #         # Fallback to google search
        #         webbrowser.open(f"https://www.google.com/search?q={site}")
        #         speak("couldn't find exact domaain, searching on google")
    
    elif "open file" in command or "open folder" in command:
        speak("Please tell me which file or folder you want to open")
        target = listen()
        
        search_paths = [
            os.path.expanduser("../Desktop"),
            os.path.expanduser("Desktop"),
            os.path.expanduser("D:\downloads"),
            "D:\photos",
            "D:"
        ]
        found = False
        
        for path in search_paths:
            for root,dirs,files in os.walk(path):
                if "file" in command:
                    for file in files:
                        if target.lower() in file.lower():
                            full_path = os.path.join(root, folder)
                            os.startfile(full_path)
                            speak(f"opening file{file}")
                            found = True
                            break
                
                elif "folder" in command:
                    for folder in dirs:
                        if target.lower() in folder.lower():
                            full_path = os.path.join(root, folder)
                            os.startfile(full_path)
                            speak(f"opening folder{folder}")
                            found = True
                            break
            
            if found:
                break
        
        if not found:
            speak("sorry not found")
        