from vosk import Model, KaldiRecognizer
import sounddevice as sd
import os
import json

model_path = os.path.join(os.path.dirname(__file__), "vosk-model-small-en-us-0.15")
model = Model(model_path)
rec = KaldiRecognizer(model, 16000)

print("🎤 Speak something...")

# Open the stream correctly
with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1) as stream:
    audio_bytes, overflowed = stream.read(4000)  # raw audio as bytes

    # ✅ Convert to bytes explicitly
    audio_bytes = bytes(audio_bytes)

    if rec.AcceptWaveform(audio_bytes):
        result = json.loads(rec.Result())
        print("✅ You said:", result.get("text", ""))
    else:
        print("❌ Could not understand.")
