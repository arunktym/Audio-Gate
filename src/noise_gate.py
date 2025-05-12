import sounddevice as sd
import numpy as np
import sys

def passthrough_stream(sample_rate=44100, blocksize=1024, channels=1, threshold=0.02):
    """
    Streams mic audio to speaker with a real-time noise gate and volume meter.
    """
    def callback(indata, outdata, frames, time, status):
        if status:
            print(f"⚠️ Stream status: {status}", file=sys.stderr)

        volume = np.linalg.norm(indata)
        bar_length = int(min(volume * 100, 50))  # max 50 bars
        bar = "█" * bar_length + "-" * (50 - bar_length)

        # Print inline volume meter
        print(f"\r🎚️ Volume: [{bar}] {volume:.3f} ", end="")

        # Apply noise gate
        if volume > threshold:
            outdata[:] = indata
        else:
            outdata[:] = np.zeros_like(indata)

    try:
        print("🎤🔇🔊 Real-time mic passthrough with noise gate + volume meter")
        print(f"📉 Threshold: {threshold}")
        print("🛑 Press ENTER to stop\n")

        with sd.Stream(samplerate=sample_rate,
                       blocksize=blocksize,
                       channels=channels,
                       dtype='float32',
                       callback=callback):
            input()
        print("\n✅ Stream stopped.")

    except Exception as e:
        print(f"\n❌ Error: {e}")
