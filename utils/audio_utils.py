
import librosa
import numpy as np

def preprocess_audio(audio_path, sampling_rate=16000):
    wav, _ = librosa.load(audio_path, sr=sampling_rate)
    return wav
