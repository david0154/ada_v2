# Dayna AI - Complete Installation Guide

## Prerequisites

### 1. Install Anaconda/Miniconda
- Download from: https://docs.conda.io/en/latest/miniconda.html
- Install and verify: `conda --version`

### 2. Install Node.js 18+
- Download from: https://nodejs.org/
- Verify: `node --version`

### 3. Install Git
- Download from: https://git-scm.com/
- Verify: `git --version`

---

## Step-by-Step Installation

### 1. Clone Repository
```bash
git clone https://github.com/david0154/ada_v2.git dayna-ai
cd dayna-ai
```

### 2. Create Python Environment
```bash
conda create -n dayna python=3.11 -y
conda activate dayna
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
playwright install chromium
```

### 4. Download Offline Models (Optional)
**Required for offline mode** - Downloads ~4.3GB

```bash
chmod +x download_models.sh
./download_models.sh
```

This downloads:
- Mistral-7B-Instruct (4.1GB)
- Whisper Base STT (74MB)
- Piper Hindi TTS (63MB)
- Piper English TTS (63MB)

### 5. Install Frontend Dependencies
```bash
npm install
```

### 6. Setup Environment (Optional - for Online Mode)
Create `.env` file in root directory:
```bash
GEMINI_API_KEY=your_api_key_here
```

Get API key from: https://aistudio.google.com/app/apikey

### 7. Setup Face Authentication (Optional)
1. Take a clear photo of your face
2. Save as `backend/reference.jpg`
3. Or disable in `backend/settings.json`: `"face_auth_enabled": false`

---

## Running Dayna AI

### Offline Mode (No Internet Required)
```bash
# Terminal 1 - Backend
conda activate dayna
python backend/offline_agent.py

# Terminal 2 - Frontend (optional)
npm run dev
```

### Online Mode (Gemini API)
```bash
# Terminal 1 - Backend
conda activate dayna
python backend/ada.py

# Terminal 2 - Frontend
npm run dev
```

### With Electron Desktop App
```bash
conda activate dayna
npm run dev
```

---

## Testing Installation

### Test Offline Agent
```bash
python backend/offline_agent.py
```

Should output:
```
[DAYNA] Loading Mistral-7B...
[DAYNA] Ready!
```

### Test Frontend
Open browser to: `http://localhost:5173`

---

## Troubleshooting

### Error: "llama-cpp-python not found"
```bash
pip install llama-cpp-python
```

### Error: "faster-whisper not found"
```bash
pip install faster-whisper
```

### Error: "piper not found"
```bash
pip install piper-tts
```

### Camera not working (macOS)
1. Go to System Preferences > Privacy & Security > Camera
2. Enable camera access for Terminal/VS Code
3. Restart the app

### Port already in use
```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9

# Kill process on port 5173
lsof -ti:5173 | xargs kill -9
```

---

## System Requirements

### Minimum
- CPU: Quad-core
- RAM: 8GB
- Storage: 10GB free
- OS: Windows 10/macOS 12/Linux

### Recommended
- CPU: 8-core
- RAM: 16GB
- GPU: NVIDIA GTX 1060+ (6GB VRAM)
- Storage: 20GB SSD

---

## Next Steps

1. Read the main [README.md](README.md) for features
2. Check [original Ada V2 docs](https://github.com/hash-anmol/ada_v2) for advanced usage
3. Run test commands to verify everything works

---

**Need help?** Open an issue at: https://github.com/david0154/ada_v2/issues
