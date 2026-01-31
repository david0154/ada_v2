"""
Dayna AI - Offline Agent
Bilingual (Hindi + English) with Mistral-7B
"""

import asyncio
from typing import Tuple
from llama_cpp import Llama
from faster_whisper import WhisperModel
import tempfile
import os


class OfflineAgent:
    def __init__(
        self,
        model_path: str = "backend/models/mistral-7b-instruct-v0.2.Q4_K_M.gguf",
        whisper_model: str = "base",
        hindi_voice: str = "backend/models/hi_IN-pratham-medium.onnx",
        english_voice: str = "backend/models/en_US-lessac-medium.onnx",
        n_threads: int = 8,
        n_gpu_layers: int = 35
    ):
        print("[DAYNA] Loading Mistral-7B...")
        self.llm = Llama(
            model_path=model_path,
            n_ctx=4096,
            n_threads=n_threads,
            n_gpu_layers=n_gpu_layers,
            verbose=False
        )
        
        self.whisper = WhisperModel(whisper_model, device="cpu")
        self.hindi_voice = hindi_voice
        self.english_voice = english_voice
        print("[DAYNA] Ready!")
    
    def _detect_language(self, text: str) -> str:
        if not text:
            return "en"
        devanagari = sum(1 for c in text if '\u0900' <= c <= '\u097F')
        total = len([c for c in text if c.isalpha()])
        return "hi" if total > 0 and (devanagari / total) > 0.3 else "en"
    
    async def generate_response(self, prompt: str) -> Tuple[str, str]:
        lang = self._detect_language(prompt)
        sys = "आप Dayna हैं।" if lang == "hi" else "You are Dayna."
        formatted = f"<s>[INST] {sys}\n\n{prompt} [/INST]"
        
        response = await asyncio.to_thread(
            self.llm, formatted, max_tokens=512, temperature=0.7
        )
        
        text = response['choices'][0]['text'].strip()
        return text, lang


if __name__ == "__main__":
    async def test():
        agent = OfflineAgent()
        resp, lang = await agent.generate_response("Hello!")
        print(f"{lang}: {resp}")
    
    asyncio.run(test())
