import sounddevice as sd
import numpy as np
from src.deepfilternet_wrapper import DeepFilterWrapper

# Initialize the model
dfn = DeepFilterWrapper(use_gpu=False)
SAMPLE_RATE = dfn.get_sample_rate()
BLOCK_SIZE = 512  # Must match model block size (can also try 1024)

print(f"[INFO] Starting stream at {SAMPLE_RATE}Hz with block size {BLOCK_SIZE}")

def audio_callback(indata, outdata, frames, time, status):
    if status:
        print("[WARN]", status)

    # Flatten input to mono float32
    input_audio = indata[:, 0]

    # Process with DeepFilterNet
    denoised_audio = dfn.process_frame(input_audio)

    # Write back to output buffer
    outdata[:, 0] = denoised_audio
    if outdata.shape[1] > 1:
        outdata[:, 1] = denoised_audio  # Duplicate to stereo if needed

try:
    with sd.Stream(
        samplerate=SAMPLE_RATE,
        blocksize=BLOCK_SIZE,
        dtype='float32',
        channels=1,
        callback=audio_callback
    ):
        print("[INFO] Streaming... Press Ctrl+C to stop.")
        while True:
            pass

except KeyboardInterrupt:
    print("\n[INFO] Stream stopped by user.")
