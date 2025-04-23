import os
import numpy as np
import soundfile as sf
import speech_recognition as sr
import ollama
from pathlib import Path

from encoder import inference as encoder
from synthesizer.inference import Synthesizer
from vocoder import inference as vocoder
from utils.audio_utils import preprocess_audio

# Initialize mic recognizer
recognizer = sr.Recognizer()

# Paths to models
encoder_path = Path("encoder/saved_models/encoder.pt")
synthesizer_path = Path("synthesizer/saved_models/synthesizer.pt")
vocoder_path = Path("vocoder/saved_models/vocoder.pt")

# Load models
print("🔁 Loading models...")
encoder.load_model(encoder_path)
synthesizer = Synthesizer(synthesizer_path)
vocoder.load_model(vocoder_path)
print("✅ Models loaded successfully.")

# Clone your own voice with generated reply
def clone_voice(source_wav_path, text, output_path="output.wav"):
    print("🎤 Cloning voice...")
    preprocessed_wav = preprocess_audio(source_wav_path)
    embed = encoder.embed_utterance(preprocessed_wav)

    specs = synthesizer.synthesize_spectrograms([text], [embed])
    generated_wav = vocoder.infer_waveform(specs[0])

    # Dynamically pad a small portion (avoid hardcoded long tail)
    pad_length = int(0.15 * 22050)  # 150ms
    generated_wav = np.pad(generated_wav, (0, pad_length), mode="constant")

    # Apply optional fade-out
    fade_duration = int(0.3 * 22050)  # 300ms
    fade_curve = np.linspace(1.0, 0.0, fade_duration)
    generated_wav[-fade_duration:] *= fade_curve

    sf.write(output_path, generated_wav.astype(np.float32), 22050)
    os.system(f"start {output_path}")
    print(f"📁 Audio saved to: {output_path}")

# Listen from mic
def listen():
    with sr.Microphone() as source:
        print("\n🎙️ Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("🧍 You said:", text)
            return text
        except sr.UnknownValueError:
            print("❌ Couldn't understand.")
            return ""
        except sr.RequestError:
            print("❌ Speech service error.")
            return ""

# Get AI response
def get_response(prompt):
    print("🤖 Thinking...")
    response = ollama.chat(
        model='llama3',
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']

# Main loop
if __name__ == "__main__":
    voice_sample_path = "my_voice.wav"  # Your recorded sample for cloning

    while True:
        user_text = listen().strip()
        if user_text.lower() in ["exit", "quit", "bye"]:
            print("👋 Exiting. Goodbye Akshat!")
            break
        if not user_text:
            continue

        ai_reply = get_response(user_text)
        print("🗣️ Assistant:", ai_reply)
        clone_voice(voice_sample_path, ai_reply)
