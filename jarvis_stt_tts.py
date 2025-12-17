import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import time


# -------- TEXT TO SPEECH (SAFE FIX) --------
def speak(text):
    engine = pyttsx3.init('sapi5')   # re-init every time (IMPORTANT)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 210)
    engine.setProperty('rate', 200)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


# -------- SPEECH TO TEXT --------
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source, phrase_time_limit=5)

    try:
        text = r.recognize_google(audio)
        print("📝 You said:", text)
        return text.lower()

    except sr.UnknownValueError:
        print("❌ Could not understand")
        return None

    except sr.RequestError:
        print("❌ Internet error")
        return None


# -------- COMMAND PROCESSOR --------
def handle_command(command):

    # 🧠 Name
    if "your name" in command:
        speak("My name is Jarvis. I am your assistant.")

    # 🕒 Time
    elif "time" in command:
        time_now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time_now}")

    # 📅 Date
    elif "date" in command:
        date_today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {date_today}")

    # 🌐 Open Google
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    # 🌐 Open YouTube
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    # 💻 Open Notepad
    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    # Open Chatgpt
    elif "open gpt" in command:
        speak("Opening gpt")
        webbrowser.open("https://chatgpt.com")


    # Open Whatsapp
    elif "open whatsapp" in command:
        speak("Opening Whatsapp")
        #os.system("WhatsApp")
        webbrowser.open("https://whatsapp.com")


    # ❌ Exit
    elif "exit" in command or "stop" in command or "quit" in command:
        speak("Goodbye. Program stopped.")
        print("🛑 Program stopped")
        return False

    # 🔁 Default repeat
    else:
        speak(command)

    return True


# -------- MAIN --------
print("✅ Jarvis Started")
speak("Hello, I am Jarvis. How can I help you?")

while True:
    command = listen()

    if command is None:
        continue

    if not handle_command(command):
        break

    time.sleep(0.5)