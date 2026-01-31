#!/usr/bin/env python3
"""
Dayna AI - Main Entry Point
Bilingual Voice Assistant (Hindi + English)

Author: David (Nexuzy Tech)
Original: Ada V2 by Nazir Louis
License: MIT
"""

import sys
import argparse

print("""
==========================================
Dayna AI - Bilingual Voice Assistant
==========================================
Hindi + English | Offline Capable
Based on Ada V2 by Nazir Louis
Modified by: David (Nexuzy Tech)
==========================================
""")

# Parse arguments first to determine mode
parser = argparse.ArgumentParser(description="Dayna AI - Bilingual Voice Assistant")
parser.add_argument(
    "--mode",
    type=str,
    default="online",
    help="Operation mode: 'online' (Gemini API) or 'offline' (Mistral-7B local)",
    choices=["online", "offline"],
)
parser.add_argument(
    "--video",
    type=str,
    default="camera",
    help="Video source for online mode",
    choices=["camera", "screen", "none"],
)

args = parser.parse_args()

if args.mode == "offline":
    print("\n[DAYNA] Starting in OFFLINE mode (Mistral-7B)...\n")
    from offline_agent import OfflineAgent
    import asyncio
    
    async def run_offline():
        agent = OfflineAgent()
        
        print("\nDayna AI is ready! Type your messages below.")
        print("Type 'exit' to quit.\n")
        
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    print("Dayna: Goodbye!")
                    break
                
                response, lang = await agent.generate_response(user_input)
                print(f"Dayna ({lang}): {response}\n")
                
            except KeyboardInterrupt:
                print("\n\nDayna: Goodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
    
    import asyncio
    asyncio.run(run_offline())
    
else:
    print("\n[DAYNA] Starting in ONLINE mode (Gemini API)...\n")
    # Import and run Ada (online mode with Gemini)
    from ada import AudioLoop
    import asyncio
    
    # Override system instruction to say "Dayna"
    # This requires modifying the config in ada.py, but for now we'll just run it
    print("[INFO] Online mode uses Gemini API with Ada backend.")
    print("[INFO] For full Dayna branding, modify backend/ada.py config.")
    print("[INFO] Alternatively, use --mode offline for complete offline experience.\n")
    
    main = AudioLoop(video_mode=args.video)
    asyncio.run(main.run(start_message="Hello! I'm Dayna, your bilingual AI assistant. I can help you in both Hindi and English. How can I assist you today?"))
