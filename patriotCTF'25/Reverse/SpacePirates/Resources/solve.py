#!/usr/bin/env python3
"""
Reverse engineering solution for Space Pirates challenge
Reverses the 4 encryption operations to find the original input
"""

FLAG_LEN = 30
TARGET = [
    0x5A,0x3D,0x5B,0x9C,0x98,0x73,0xAE,0x32,0x25,0x47,0x48,0x51,0x6C,0x71,0x3A,0x62,0xB8,0x7B,0x63,0x57,0x25,0x89,0x58,0xBF,0x78,0x34,0x98,0x71,0x68,0x59
]

XOR_KEY = [0x42, 0x73, 0x21, 0x69, 0x37]
MAGIC_ADD = 0x2A

def reverse_encryption():
    """
    Reverse the encryption operations:
    1. Start with TARGET
    2. Reverse op 4: XOR with position
    3. Reverse op 3: Subtract MAGIC_ADD (mod 256)
    4. Reverse op 2: Swap adjacent pairs
    5. Reverse op 1: XOR with rotating key
    """
    buffer = list(TARGET)
    
    print("Starting with TARGET:")
    print(f"  {[hex(b) for b in buffer]}\n")
    
    # Reverse operation 4: XOR with position (XOR is its own inverse)
    print("[Reverse 4/4] Reversing coordinate calibration (XOR with position)...")
    for i in range(FLAG_LEN):
        buffer[i] ^= i
    print(f"  After reverse op 4: {[hex(b) for b in buffer[:10]]}...\n")
    
    # Reverse operation 3: Subtract MAGIC_ADD (mod 256)
    print("[Reverse 3/4] Reversing gravitational shift (subtract 0x2A)...")
    for i in range(FLAG_LEN):
        buffer[i] = (buffer[i] - MAGIC_ADD) % 256
    print(f"  After reverse op 3: {[hex(b) for b in buffer[:10]]}...\n")
    
    # Reverse operation 2: Swap adjacent pairs (swapping is its own inverse)
    print("[Reverse 2/4] Reversing spatial transposition (swap pairs)...")
    for i in range(0, FLAG_LEN, 2):
        temp = buffer[i]
        buffer[i] = buffer[i + 1]
        buffer[i + 1] = temp
    print(f"  After reverse op 2: {[hex(b) for b in buffer[:10]]}...\n")
    
    # Reverse operation 1: XOR with rotating key (XOR is its own inverse)
    print("[Reverse 1/4] Reversing quantum entanglement cipher (XOR with key)...")
    for i in range(FLAG_LEN):
        buffer[i] ^= XOR_KEY[i % 5]
    print(f"  After reverse op 1: {[hex(b) for b in buffer[:10]]}...\n")
    
    # Convert to string
    result = ''.join(chr(b) for b in buffer)
    
    print("=" * 50)
    print("DECRYPTED COORDINATES:")
    print(f"  {result}")
    print("=" * 50)
    
    return result

if __name__ == "__main__":
    flag = reverse_encryption()
    print(f"\nFlag: {flag}")
    print(f"\nTo verify, run: ./challenge '{flag}'")

