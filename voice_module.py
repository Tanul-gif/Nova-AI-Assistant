from vosk import Model, KaldiRecognizer
import sounddevice as sd
import pyttsx3
import os
import json

# 🔧 Initialize TTS
engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

# ✅ Load offline Vosk model
model_path = os.path.join(os.path.dirname(__file__), "vosk-model-small-en-us-0.15")  # or vosk_model_en_us_022
model = Model(model_path)
rec = KaldiRecognizer(model, 16000)

def speak(text):
    """Make Jarvis speak the given text."""
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen using offline Vosk and return recognized speech."""
    print("🎤 Listening... Speak now...")

    try:
        duration = 4  # seconds
        audio_data = sd.rec(int(16000 * duration), samplerate=16000, channels=1, dtype='int16')
        sd.wait()

        if audio_data is None or len(audio_data) == 0:
            speak("Mic input failed.")
            return ""

        audio_bytes = audio_data.tobytes()  # ✅ FIXED

        if rec.AcceptWaveform(audio_bytes):
            result = json.loads(rec.Result())
            text = result.get("text", "").strip()
            if text:
                print("✅ You said:", text)
                return text.lower()
            else:
                speak("Sorry, I didn't catch that.")
                return ""
        else:
            speak("Sorry, I didn't catch that.")
            return ""

    except Exception as e:
        speak("An error occurred while listening.")
        print("❌ ERROR:", e)
        return ""

