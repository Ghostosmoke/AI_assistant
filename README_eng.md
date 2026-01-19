# 🎙️ AI Voice Chat (Whisper + Ollama)

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![PyQt6](https://img.shields.io/badge/PyQt6-GUI-green)
![Whisper](https://img.shields.io/badge/Whisper-STT-orange)
![Ollama](https://img.shields.io/badge/Ollama-LLM-purple)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A **local desktop AI voice chat** built with **Python + PyQt6**, using **Whisper** for speech-to-text and **Ollama (LLM)** for text understanding and question answering.

✅ Works offline (after model download)
✅ Microphone recording & audio file support
✅ Local LLM, no cloud required

---

## 🚀 Features

* 🎧 **Microphone recording**
  Record audio directly from the app.

* 📂 **Audio file upload**
  Supports wav / mp3 / m4a (depends on Whisper & FFmpeg).

* 📝 **Speech-to-text**
  Audio is transcribed using **Whisper / faster-whisper**.

* 🤖 **AI Chat (LLM)**
  Transcribed text is sent to **Ollama**, where the model:

  * answers questions;
  * explains content;
  * creates summaries.

* 🖥️ **PyQt6 GUI**
  Simple desktop interface with chat and controls.

---

## 🧠 Tech Stack

* **Python 3.10+**
* **PyQt6** — GUI
* **Whisper / faster-whisper** — Speech-to-Text
* **Ollama** — Local LLM runtime
* **FFmpeg** — Audio processing

---

## 🎙️ Whisper Models: Speed, Quality & Hardware

Larger Whisper models give better accuracy but require more resources.

### ⏱️ Transcription Speed (1 minute of audio)

> Average values on **CPU (Ryzen 5 / Intel i7)** using `faster-whisper`, no GPU.

| Model      | Time per 1 min audio | Notes                    |
| ---------- | -------------------- | ------------------------ |
| **tiny**   | ~5–10 sec            | Near real-time           |
| **base**   | ~10–20 sec           | Good for notes           |
| **small**  | ~25–40 sec           | Best balance             |
| **medium** | ~60–90 sec           | High accuracy            |
| **large**  | 2–4 min              | Requires strong hardware |

---

### 📌 Whisper Model Comparison

| Model      | Size    | Pros          | Cons                 | Hardware          |
| ---------- | ------- | ------------- | -------------------- | ----------------- |
| **tiny**   | ~75 MB  | Very fast     | Low accuracy         | CPU, 2 GB RAM     |
| **base**   | ~140 MB | Lightweight   | Errors on long audio | CPU, 4 GB RAM     |
| **small**  | ~460 MB | Good accuracy | Slower               | CPU/GPU, 6 GB RAM |
| **medium** | ~1.5 GB | High accuracy | Heavy                | GPU, 8–10 GB VRAM |
| **large**  | ~3 GB   | Best accuracy | Very heavy           | GPU, 12+ GB VRAM  |

---

## 🎯 Default Presets (Recommended)

### 👶 Beginner (plug & play)

* **Whisper:** `small`
* **Ollama:** `mistral`
* **Mode:** CPU + faster-whisper

✔ Good accuracy
✔ No GPU required
✔ Laptop-friendly

---

### ⚖️ Balanced

* **Whisper:** `medium`
* **Ollama:** `llama3`
* **Mode:** GPU if available

✔ Great for lectures & interviews

---

### 🚀 Maximum Quality

* **Whisper:** `large`
* **Ollama:** `llama3`
* **Mode:** GPU (12–24 GB VRAM)

✔ Best possible accuracy

---

## 🧠 CPU vs GPU: Real Differences

| Aspect         | CPU              | GPU             |
| -------------- | ---------------- | --------------- |
| Availability   | Works everywhere | NVIDIA required |
| Speed          | Slower           | 5–10× faster    |
| Whisper models | tiny–small       | medium–large    |
| Ollama         | Uses RAM         | Uses VRAM       |
| Laptops        | Ideal            | Limited         |

**Conclusion:**

* Use `faster-whisper` on CPU
* GPU is only worth it for `medium` and `large`

---

## 💻 Laptops vs Desktop PCs

### 💼 Laptop

* CPU: 4–8 cores
* RAM: 16 GB
* Whisper: `base` / `small`
* Ollama: `phi`, `mistral`

⚠️ Avoid overheating and `large` models

---

### 🖥️ Desktop PC

* CPU: 8+ cores
* RAM: 32 GB
* GPU: RTX 3060+
* Whisper: `medium` / `large`
* Ollama: `llama3`

---

## 🖥️ Hardware Requirements

### 💻 Minimum

* CPU: 4 cores
* RAM: 8 GB
* GPU: not required
* Disk: 10 GB free

---

### ⚖️ Recommended

* CPU: 6–8 cores
* RAM: 16 GB
* GPU: optional (6–8 GB VRAM)
* Disk: SSD, 20–30 GB

---

### 🚀 Advanced

* CPU: 8+ cores
* RAM: 32 GB
* GPU: RTX 3060 (12 GB VRAM)
* Disk: NVMe SSD

---

## 🤖 Ollama Models

| Model       | Pros                 | Cons              | RAM   |
| ----------- | -------------------- | ----------------- | ----- |
| **llama3**  | Best overall quality | Heavy             | 8+ GB |
| **mistral** | Fast & compact       | Weaker reasoning  | 6 GB  |
| **gemma**   | Lightweight          | Short answers     | 6 GB  |
| **phi**     | Very small           | Limited knowledge | 4 GB  |

---

## 📦 Installation

```bash
git clone https://github.com/yourname/yourproject.git
cd yourproject
pip install -r requirements.txt
```

### FFmpeg

* **Windows:** download from ffmpeg.org and add to PATH
* **Linux:** `sudo apt install ffmpeg`
* **macOS:** `brew install ffmpeg`

---

## ▶️ Run

```bash
python main.py
```

---

## ❗ Common Issues

### Whisper crashes or fails

* Check Python 3.10+
* Make sure FFmpeg is installed
* Prefer `faster-whisper`

```bash
pip install faster-whisper
```

---

### Ollama connection refused

```bash
ollama serve
ollama list
ollama pull llama3
```

---

## 📄 License

MIT License

---

## 👤 Author

Your Name
GitHub: your-link
