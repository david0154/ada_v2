#!/usr/bin/env python3
"""
Check if all required dependencies are installed
"""

import sys
import importlib
from pathlib import Path

def check_package(package_name, import_name=None):
    """Check if a package is installed"""
    if import_name is None:
        import_name = package_name
    
    try:
        importlib.import_module(import_name)
        print(f"✅ {package_name}")
        return True
    except ImportError:
        print(f"❌ {package_name} - NOT INSTALLED")
        return False

print("\n" + "="*50)
print("Dayna AI - Dependency Check")
print("="*50 + "\n")

print("Core Dependencies:")
core_packages = [
    ("google-generativeai", "google.genai"),
    ("python-dotenv", "dotenv"),
    ("fastapi", "fastapi"),
    ("uvicorn", "uvicorn"),
    ("python-socketio", "socketio"),
    ("opencv-python", "cv2"),
    ("pyaudio", "pyaudio"),
    ("pillow", "PIL"),
    ("numpy", "numpy"),
]

core_ok = all(check_package(pkg, imp) for pkg, imp in core_packages)

print("\nOffline Dependencies:")
offline_packages = [
    ("llama-cpp-python", "llama_cpp"),
    ("faster-whisper", "faster_whisper"),
]

offline_ok = all(check_package(pkg, imp) for pkg, imp in offline_packages)

print("\nAdvanced Features:")
advanced_packages = [
    ("build123d", "build123d"),
    ("playwright", "playwright"),
    ("python-kasa", "kasa"),
    ("mediapipe", "mediapipe"),
]

advanced_ok = all(check_package(pkg, imp) for pkg, imp in advanced_packages)

print("\n" + "="*50)
if core_ok:
    print("✅ Core dependencies: OK")
else:
    print("❌ Core dependencies: MISSING")
    print("   Run: pip install -r requirements.txt")

if offline_ok:
    print("✅ Offline mode: Ready")
else:
    print("⚠️  Offline mode: Not available")
    print("   Run: pip install llama-cpp-python faster-whisper")

if advanced_ok:
    print("✅ Advanced features: Ready")
else:
    print("⚠️  Some advanced features unavailable")

print("="*50)

# Check models
print("\nOffline Models:")
model_path = Path("backend/models/mistral-7b-instruct-v0.2.Q4_K_M.gguf")
if model_path.exists():
    size_gb = model_path.stat().st_size / (1024**3)
    print(f"✅ Mistral-7B found ({size_gb:.1f} GB)")
else:
    print("❌ Mistral-7B not found")
    print("   Run: ./download_models.sh")

print("\n" + "="*50 + "\n")

if not core_ok:
    sys.exit(1)
