# import speech_recognition
# import pyttsx3
# import cv2
# import torch

# print("All libraries installed")
from voice_module import speak, listen

speak("Hello, I am Jarvis. how can i help you")
while True:
    command = listen()

    if "hello" in command:
        speak("Hi there! I'm always ready.")
    elif "your name" in command:
        speak("My name is jarvis, your personal ai assistant")
    elif "exit" in command or "stop" in command or "quit" in command:
        speak("Goodbye")
        exit()
    else:
        speak("you said: " + command)