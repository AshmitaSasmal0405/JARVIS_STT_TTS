import speech_recognition as sr

def record_text():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("🎤 Listening... Speak now")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=5, phrase_time_limit=5)

            text = r.recognize_google(audio)
            return text

    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        return None

    except sr.RequestError as e:
        print("❌ Internet error:", e)
        return None

    except Exception as e:
        print("❌ Error:", e)
        return None


def output_text(text):
    with open("output.txt", "a") as f:
        f.write(text + "\n")


print("✅ Speech to Text program started")

while True:
    text = record_text()

    if text is None:
        print("🔁 Trying again...\n")
        continue

    print("📝 You said:", text)

    if text.lower() in ["stop", "exit", "quit"]:
        print("🛑 Program stopped by user")
        break
    output_text(text)