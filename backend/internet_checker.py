#!/usr/bin/env python3
"""
Internet Connection Checker
Auto-detect online/offline status
"""

import socket
import requests
from typing import Literal


def check_internet(timeout: float = 3.0) -> bool:
    """
    Check if internet connection is available.
    
    Args:
        timeout: Timeout in seconds for connection test
        
    Returns:
        True if internet is available, False otherwise
    """
    # Method 1: Try to connect to Google DNS
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=timeout)
        print("[INTERNET] ✅ Connected (DNS test passed)")
        return True
    except OSError:
        pass
    
    # Method 2: Try HTTP request to reliable sites
    test_urls = [
        "https://www.google.com",
        "https://www.cloudflare.com",
        "https://1.1.1.1"
    ]
    
    for url in test_urls:
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                print(f"[INTERNET] ✅ Connected (HTTP test passed: {url})")
                return True
        except:
            continue
    
    print("[INTERNET] ❌ No connection detected")
    return False


def get_mode(force_offline: bool = False) -> Literal["online", "offline"]:
    """
    Determine operation mode based on internet availability.
    
    Args:
        force_offline: Force offline mode even if internet is available
        
    Returns:
        "online" or "offline"
    """
    if force_offline:
        print("[MODE] 🔒 Forced offline mode")
        return "offline"
    
    if check_internet():
        print("[MODE] 🌐 Online mode selected")
        return "online"
    else:
        print("[MODE] 🔒 Offline mode (no internet)")
        return "offline"


if __name__ == "__main__":
    mode = get_mode()
    print(f"\nRecommended mode: {mode}")
