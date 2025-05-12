from src.audio_utils import record_audio, play_audio
from src.noise_gate import passthrough_stream

def main():
    print("\n🎧 Select Mode:")
    print("1. Record & Playback (Test)")
    print("2. Real-Time Mic Passthrough with Noise Gate\n")

    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        duration = 5
        sample_rate = 44100
        channels = 1

        print("🎙️ Microphone Test Starting...")
        audio = record_audio(duration=duration, sample_rate=sample_rate, channels=channels)
        print("📢 Playback Starting...")
        play_audio(audio, sample_rate=sample_rate)
        print("✅ Microphone Test Complete.")

    elif choice == "2":
        sample_rate = 44100
        blocksize = 1024
        channels = 1

        try:
            threshold = float(input("Set noise gate threshold (0.01 to 0.05 recommended): ").strip())
        except ValueError:
            threshold = 0.02
            print("⚠️ Invalid input. Using default threshold of 0.02")

        passthrough_stream(sample_rate=sample_rate, blocksize=blocksize, channels=channels, threshold=threshold)

    else:
        print("❌ Invalid input. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
