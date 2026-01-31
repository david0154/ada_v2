#!/usr/bin/env python3
"""
Dayna AI - Complete System with Auto Internet Detection
All features work both online (Gemini) and offline (Mistral-7B)

Author: David (Nexuzy Tech)
Based on: Ada V2 by Nazir Louis
License: MIT
"""

import sys
import os
import asyncio
import argparse
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent))

from internet_checker import get_mode

print("""
==========================================
   Dayna AI - Bilingual Voice Assistant
==========================================
🇮🇳 Hindi + English
🔒 Offline Capable
🌐 Auto-detects Internet
==========================================
""")

# Parse arguments
parser = argparse.ArgumentParser(description="Dayna AI - Complete System")
parser.add_argument(
    "--mode",
    type=str,
    default="auto",
    help="Mode: 'auto' (detect), 'online' (force Gemini), 'offline' (force Mistral)",
    choices=["auto", "online", "offline"],
)
parser.add_argument(
    "--video",
    type=str,
    default="camera",
    help="Video source (online mode only)",
    choices=["camera", "screen", "none"],
)
parser.add_argument(
    "--voice-only",
    action="store_true",
    help="Run in voice-only mode (no GUI)"
)

args = parser.parse_args()

# Determine mode
if args.mode == "auto":
    mode = get_mode()
elif args.mode == "offline":
    mode = get_mode(force_offline=True)
else:
    mode = "online"

print(f"\n[DAYNA] Starting in {mode.upper()} mode...\n")

if mode == "offline":
    print("[INFO] Offline mode: Using Mistral-7B (local)")
    print("[INFO] Features available: Voice chat, basic CAD, file operations")
    print("[INFO] Features unavailable: Web browsing, advanced vision\n")
    
    # Check if models are downloaded
    model_path = Path("backend/models/mistral-7b-instruct-v0.2.Q4_K_M.gguf")
    if not model_path.exists():
        print("❌ ERROR: Offline models not found!")
        print("\nPlease download models first:")
        print("  chmod +x download_models.sh")
        print("  ./download_models.sh\n")
        sys.exit(1)
    
    from offline_agent import OfflineAgent
    
    async def run_offline():
        agent = OfflineAgent()
        
        print("\n" + "="*50)
        print("Dayna AI is ready!")
        print("Type your messages in Hindi or English.")
        print("Type 'exit' to quit.")
        print("="*50 + "\n")
        
        while True:
            try:
                user_input = input("\n💬 You: ")
                
                if user_input.lower().strip() in ['exit', 'quit', 'bye', 'goodbye']:
                    print("\n👋 Dayna: अलविदा! Goodbye!\n")
                    break
                
                if not user_input.strip():
                    continue
                
                print("\n🤖 Dayna: ", end="", flush=True)
                response, lang = await agent.generate_response(user_input)
                print(f"{response}")
                
            except KeyboardInterrupt:
                print("\n\n👋 Dayna: Goodbye!\n")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}\n")
    
    asyncio.run(run_offline())

else:  # online mode
    print("[INFO] Online mode: Using Gemini 2.5 (cloud)")
    print("[INFO] All features available: CAD, Web, Vision, Smart Home, 3D Printing\n")
    
    # Check for API key
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ ERROR: GEMINI_API_KEY not found in .env file!")
        print("\nGet your API key from: https://aistudio.google.com/app/apikey")
        print("Then create a .env file with:")
        print("  GEMINI_API_KEY=your_key_here\n")
        sys.exit(1)
    
    from ada import AudioLoop
    
    # Customize system instruction for Dayna
    print("[INFO] Initializing Dayna AI with Gemini backend...\n")
    
    main = AudioLoop(video_mode=args.video)
    
    # Custom start message
    start_msg = (
        "Hello! I'm Dayna, your bilingual AI assistant. "
        "I can speak both Hindi (हिंदी) and English. "
        "I can help you with 3D CAD design, web browsing, smart home control, "
        "and much more. How can I assist you today?"
    )
    
    asyncio.run(main.run(start_message=start_msg))
