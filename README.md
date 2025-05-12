# 🎷 AI Noise Gate - Real-Time Audio Filtering with DeepFilterNet

A cross-platform, real-time audio noise gate powered by **DeepFilterNet**.
This tool filters out background noise from microphone input and outputs a cleaner version—perfect for use in **live streaming, meetings, or noisy environments** like call centers.

---

## 🚀 Features

* ✅ **Real-time noise suppression** using DeepFilterNet v2
* ✅ **Cross-platform**: works on macOS, Linux, and Windows (Python-based)
* ✅ Lightweight and fast (runs on CPU)
* ✅ Modular structure for easy extension
* ✅ Works with any standard microphone/audio device

---

## 🧠 Tech Stack

* Python 3.10+
* [DeepFilterNet](https://github.com/Rikorose/DeepFilterNet)
* NumPy, PyTorch
* SoundDevice (PortAudio backend)

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-noise-gate.git
cd ai-noise-gate
```

### 2. Set Up the Python Environment

#### ✅ Using Conda (Recommended for Apple Silicon)

```bash
conda create -n ai-noise-gate python=3.10
conda activate ai-noise-gate
conda install numpy scipy -c conda-forge
pip install -r requirements.txt
```

> 💡 Note: If `sounddevice` fails via Conda on Apple Silicon, use pip instead.

#### ✅ Or Using Virtualenv (If Not Using Conda)

```bash
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 3. Clone DeepFilterNet Inside This Project

```bash
git clone https://github.com/Rikorose/DeepFilterNet.git
```

---

## 4. Download the Pretrained Model

```bash
cd DeepFilterNet
python -m df.enhance download_model
cd ..
```

---

## ▶️ Usage

Simply run the main script:

```bash
python main.py
```

You'll hear your microphone input filtered in real-time.

> 🎧 **Tip**: Use headphones to avoid audio feedback.

---

## 🧪 Testing

To verify DeepFilterNet works outside real-time:

```bash
cd DeepFilterNet
python demo.py ./test_files/noisy_sample.wav
```

---

## 📁 Project Structure

```plaintext
ai-noise-gate/
├── DeepFilterNet/              # Cloned from official repo
├── src/
│   └── deepfilternet_wrapper.py  # Model wrapper for real-time inference
├── main.py                     # Entry point for real-time filtering
├── requirements.txt            # Python dependencies
└── README.md
```

---

## 🔧 Roadmap

* 🎙 Voice print recognition (suppress other voices)
* 🎚 Adjustable dB limiter
* 🖥️ Simple GUI interface
* 📆 Packaged desktop app (.exe, .app)

---

## 📜 License

MIT License.
DeepFilterNet is licensed under Apache 2.0 by @Rikorose.

---

## 🧓‍♂️ Author

Built by **Arun Sojan** for fun, learning, and open-source contribution.
Pull requests and feedback are welcome!
