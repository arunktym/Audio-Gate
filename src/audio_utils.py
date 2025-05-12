import sounddevice as sd
import numpy as np

def record_audio(duration=5, sample_rate=44100, channels=1):
    """
    Records audio from the default input device (microphone).
    
    Args:
        duration (int): Duration in seconds to record.
        sample_rate (int): Sample rate in Hz.
        channels (int): Number of audio channels (1 = mono, 2 = stereo).
    
    Returns:
        np.ndarray: Recorded audio as a NumPy array.
    """
    try:
        print(f"🔴 Recording for {duration} seconds...")
        audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, dtype='float32')
        sd.wait()
        print("✅ Done recording.")
        return audio
    except Exception as e:
        print(f"❌ Error during recording: {e}")
        return None

def play_audio(audio, sample_rate=44100):
    """
    Plays the given audio array through the default output device (speaker).
    
    Args:
        audio (np.ndarray): Audio data to play.
        sample_rate (int): Sample rate in Hz.
    """
    try:
        if audio is None:
            print("⚠️ No audio data to play.")
            return
        print("🔊 Playing audio...")
        sd.play(audio, samplerate=sample_rate)
        sd.wait()
        print("✅ Done playing.")
    except Exception as e:
        print(f"❌ Error during playback: {e}")
