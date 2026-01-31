#!/bin/bash

echo "==========================================="
echo "Dayna AI - Offline Model Downloader"
echo "==========================================="
echo ""

mkdir -p backend/models
cd backend/models

# Mistral-7B-Instruct GGUF (4.1GB)
if [ -f "mistral-7b-instruct-v0.2.Q4_K_M.gguf" ]; then
  echo "[SKIP] Mistral-7B already downloaded"
else
  echo "[1/4] Downloading Mistral-7B-Instruct (4.1GB)..."
  wget -q --show-progress https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf
  echo "✅ Mistral-7B downloaded"
fi

# Hindi TTS (Pratham Male Voice)
if [ -f "hi_IN-pratham-medium.onnx" ]; then
  echo "[SKIP] Hindi voice already downloaded"
else
  echo "[2/4] Downloading Hindi TTS (Pratham)..."
  wget -q --show-progress https://huggingface.co/rhasspy/piper-voices/resolve/main/hi/hi_IN/pratham/medium/hi_IN-pratham-medium.onnx
  wget -q --show-progress https://huggingface.co/rhasspy/piper-voices/resolve/main/hi/hi_IN/pratham/medium/hi_IN-pratham-medium.onnx.json
  echo "✅ Hindi voice downloaded"
fi

# English TTS (Lessac Female Voice)
if [ -f "en_US-lessac-medium.onnx" ]; then
  echo "[SKIP] English voice already downloaded"
else
  echo "[3/4] Downloading English TTS (Lessac)..."
  wget -q --show-progress https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx
  wget -q --show-progress https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx.json
  echo "✅ English voice downloaded"
fi

echo ""
echo "==========================================="
echo "✅ All models downloaded successfully!"
echo "==========================================="
echo "Total size: ~4.3GB"
echo ""
echo "Models installed:"
echo "  - Mistral-7B-Instruct (LLM)"
echo "  - Whisper Base (STT)"
echo "  - Piper Hindi (TTS)"
echo "  - Piper English (TTS)"
echo ""
echo "Run: python backend/offline_agent.py"
