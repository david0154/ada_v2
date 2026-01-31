# Dayna AI - Bilingual Offline Voice Assistant 🇮🇳

![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11-blue?logo=python)
![Hindi](https://img.shields.io/badge/Language-Hindi%20%7C%20English-orange)
![Offline](https://img.shields.io/badge/Mode-Offline%20Capable-green)
![License](https://img.shields.io/badge/License-MIT-green)

> **D.A.Y.N.A** = **D**esign **A**ssistant with **Y**our **N**eural **A**rchitecture

**Dayna AI** is India's first fully offline bilingual (Hindi + English) voice assistant. Built on top of Ada V2, it adds complete offline capabilities with Mistral-7B and maintains all advanced features like CAD generation, gesture control, and smart home integration.

---

## 🌟 Key Features

### 🇮🇳 Bilingual Support
- ✅ **Hindi (हिंदी)**: Native Devanagari script with Indian TTS voices
- ✅ **English**: Full English language support
- 🤖 **Auto-detect**: Automatically responds in user's language

### 🔒 100% Offline Capable
- ✅ **Mistral-7B-Instruct**: Runs locally (4.1GB GGUF model)
- ✅ **Whisper STT**: Multilingual speech recognition
- ✅ **Piper TTS**: Hindi and English voices
- ⚡ **No Internet Required**: Complete privacy after model download

### 🎯 Advanced AI Capabilities
| Feature | Description | Technology |
|---------|-------------|------------|
| **🗣️ Voice Control** | Low-latency conversation | Gemini 2.5 / Mistral-7B |
| **🧊 3D CAD** | Generate models from voice | build123d |
| **🖨️ 3D Printing** | Wireless print jobs | OrcaSlicer + Moonraker |
| **🖐️ Gestures** | Minority Report UI | MediaPipe |
| **👁️ Face Auth** | Biometric security | MediaPipe |
| **🌐 Web Agent** | Browser automation | Playwright |
| **🏠 Smart Home** | Control Kasa devices | python-kasa |

---

## ⚡ Quick Start

### Installation

```bash
# 1. Clone repository
git clone https://github.com/david0154/ada_v2.git dayna-ai
cd dayna-ai

# 2. Create Python environment
conda create -n dayna python=3.11 -y
conda activate dayna

# 3. Install dependencies
pip install -r requirements.txt
playwright install chromium

# 4. Download offline models (~4.5GB)
chmod +x download_models.sh
./download_models.sh

# 5. Install frontend
npm install

# 6. Setup environment
cp .env.example .env
# Add your GEMINI_API_KEY (optional for offline mode)
```

### Running

#### Offline Mode (No Internet)
```bash
conda activate dayna
python backend/dayna.py --mode offline
npm run dev
```

#### Online Mode (Gemini API)
```bash
# Add GEMINI_API_KEY to .env first
python backend/dayna.py --mode online
npm run dev
```

---

## 🚀 What's New in Dayna AI

### Added Features
- ✅ **Offline Agent**: Complete Mistral-7B integration
- ✅ **Hindi Support**: Native Hindi TTS and STT
- ✅ **Bilingual Mode**: Auto-detect Hindi/English
- ✅ **Model Manager**: Easy download script for AI models
- ✅ **Privacy Mode**: 100% local processing option

### Original Ada V2 Features (Maintained)
- ✅ All CAD generation capabilities
- ✅ Gesture control system
- ✅ Face authentication
- ✅ 3D printer integration
- ✅ Smart home control
- ✅ Web automation agent

---

## 📦 Offline Models

Dayna AI uses these models for offline operation:

| Model | Size | Purpose |
|-------|------|----------|
| **Mistral-7B-Instruct** (Q4_K_M) | 4.1GB | LLM for responses |
| **Whisper Base** | 74MB | Speech-to-text (multilingual) |
| **Piper Hindi (Pratham)** | 63MB | Hindi TTS (Male) |
| **Piper English (Lessac)** | 63MB | English TTS (Female) |

**Total**: ~4.3GB

---

## 🎙️ Voice Commands

### English Examples
```
"Hello Dayna, create a 3D model of a coffee mug"
"Turn on the living room lights"
"What's the weather like?"
"Make this design 20% larger"
```

### Hindi Examples
```
"नमस्ते Dayna, एक प्याला का 3D model बनाओ"
"लिविंग रूम की लाइट चालू करो"
"आज मौसम कैसा है?"
"इस design को 20% बड़ा करो"
```

---

## ⚙️ System Requirements

### Minimum
- **CPU**: Quad-core processor
- **RAM**: 8GB
- **Storage**: 10GB free
- **OS**: Windows 10/macOS 12/Linux

### Recommended
- **CPU**: 8-core processor  
- **RAM**: 16GB
- **GPU**: NVIDIA GTX 1060+ (6GB VRAM) for faster offline mode
- **Storage**: 20GB SSD

---

## 📚 Documentation

For complete documentation, see the original [Ada V2 README](https://github.com/hash-anmol/ada_v2#readme) — all features remain compatible.

### Key Differences
| Aspect | Ada V2 | Dayna AI |
|--------|--------|----------|
| **Language** | English only | Hindi + English |
| **Offline** | Requires internet | Fully offline capable |
| **LLM** | Gemini only | Gemini + Mistral-7B |
| **Privacy** | Cloud-based | Local processing |

---

## 🙏 Credits

### Original Project
- **Ada V2** by [Nazir Louis](https://github.com/hash-anmol/ada_v2)
- Licensed under MIT

### AI Models
- **Mistral-7B** by [Mistral AI](https://mistral.ai)
- **Whisper** by [OpenAI](https://github.com/openai/whisper)
- **Piper TTS** by [Rhasspy](https://github.com/rhasspy/piper)
- **Hindi Voices** from [Piper Voices](https://huggingface.co/rhasspy/piper-voices)

### Modified By
- **David** ([Nexuzy Tech](https://nexuzy.com))
- Added offline capabilities and Hindi support

---

## 📄 License

MIT License (same as original Ada V2)

---

<p align="center">
  <strong>🇮🇳 Made in India with ❤️ by David (Nexuzy Tech)</strong><br>
  <em>India's First Offline Bilingual AI Assistant</em>
</p>
