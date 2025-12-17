#pip install pyttsx3
#import pyttsx3
#text_speech = pyttsx3.init()

#answer = input("What you want to convert to speech :")
#text_speech.say(answer)
#text_speech.runAndWait()

import pyttsx3
import threading

def speak(text):
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()

print("Text to Speech started...")
print("Type 'exit' to stop")

while True:
    text = input("Enter text: ")

    if text.lower() == "exit":
        t = threading.Thread(target=speak, args=("Goodbye",))
        t.start()
        break

    t = threading.Thread(target=speak, args=(text,))
    t.start()