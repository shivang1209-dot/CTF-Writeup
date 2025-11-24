#!/usr/bin/env python3
"""
Reverse engineering solution for Space Pirates 3 challenge
Reverses the 6 encryption operations to find the original input
"""

FLAG_LEN = 30
TARGET = [
    0x60, 0x6D, 0x5D, 0x97, 0x2C, 0x04, 0xAF, 0x7C, 0xE2, 0x9E, 0x77, 0x85, 0xD1, 0x0F, 0x1D, 0x17, 
    0xD4, 0x30, 0xB7, 0x48, 0xDC, 0x48, 0x36, 0xC1, 0xCA, 0x28, 0xE1, 0x37, 0x58, 0x0F
]

XOR_KEY = [0xC7, 0x2E, 0x89, 0x51, 0xB4, 0x6D, 0x1F]
ROTATION_PATTERN = [7, 5, 3, 1, 6, 4, 2, 0]
MAGIC_SUB = 0x93
CHUNK_SIZE = 6

def rotate_right(byte, n):
    """Rotate a byte right by n positions (inverse of rotate_left)"""
    n = n % 8
    return ((byte >> n) | (byte << (8 - n))) & 0xFF

def reverse_encryption():
    """
    Reverse the encryption operations in reverse order:
    1. Start with TARGET
    2. Reverse op 6: XOR with (position² + position) mod 256
    3. Reverse op 5: Reverse chunks of 6
    4. Reverse op 4: Add MAGIC_SUB (inverse of subtraction)
    5. Reverse op 3: Swap adjacent pairs
    6. Reverse op 2: Rotate right by rotation amounts
    7. Reverse op 1: XOR with rotating key
    """
    buffer = list(TARGET)
    
    print("Starting with TARGET:")
    print(f"  {[hex(b) for b in buffer]}\n")
    
    # Reverse operation 6: XOR with (position² + position) mod 256 (XOR is its own inverse)
    print("[Reverse 6/6] Reversing coordinate calibration (XOR with position² + position)...")
    for i in range(FLAG_LEN):
        position_value = ((i * i) + i) % 256
        buffer[i] ^= position_value
    print(f"  After reverse op 6: {[hex(b) for b in buffer[:10]]}...\n")
    
    # Reverse operation 5: Reverse chunks of 6 (reversal is its own inverse)
    print("[Reverse 5/6] Reversing temporal inversion (reverse chunks of 6)...")
    for chunk_start in range(0, FLAG_LEN, CHUNK_SIZE):
        chunk_end = min(chunk_start + CHUNK_SIZE, FLAG_LEN)
        buffer[chunk_start:chunk_end] = reversed(buffer[chunk_start:chunk_end])
    print(f"  After reverse op 5: {[hex(b) for b in buffer[:10]]}...\n")
    
    # Reverse operation 4: Add MAGIC_SUB (inverse of subtraction, with wrapping)
    print("[Reverse 4/6] Reversing gravitational shift (add 0x93)...")
    for i in range(FLAG_LEN):
        buffer[i] = (buffer[i] + MAGIC_SUB) & 0xFF
    print(f"  After reverse op 4: {[hex(b) for b in buffer[:10]]}...\n")
    
    # Reverse operation 3: Swap adjacent pairs (swapping is its own inverse)
    print("[Reverse 3/6] Reversing spatial transposition (swap pairs)...")
    for i in range(0, FLAG_LEN, 2):
        if i + 1 < FLAG_LEN:
            buffer[i], buffer[i + 1] = buffer[i + 1], buffer[i]
    print(f"  After reverse op 3: {[hex(b) for b in buffer[:10]]}...\n")
    
    # Reverse operation 2: Rotate right by rotation amounts (inverse of rotate left)
    print("[Reverse 2/6] Reversing stellar rotation (rotate right)...")
    for i in range(FLAG_LEN):
        rotation = ROTATION_PATTERN[i % len(ROTATION_PATTERN)]
        buffer[i] = rotate_right(buffer[i], rotation)
    print(f"  After reverse op 2: {[hex(b) for b in buffer[:10]]}...\n")
    
    # Reverse operation 1: XOR with rotating key (XOR is its own inverse)
    print("[Reverse 1/6] Reversing quantum entanglement cipher (XOR with key)...")
    for i in range(FLAG_LEN):
        buffer[i] ^= XOR_KEY[i % len(XOR_KEY)]
    print(f"  After reverse op 1: {[hex(b) for b in buffer[:10]]}...\n")
    
    # Convert to string
    result = ''.join(chr(b) for b in buffer)
    
    print("=" * 50)
    print("DECRYPTED VAULT COMBINATION:")
    print(f"  {result}")
    print("=" * 50)
    
    return result

if __name__ == "__main__":
    flag = reverse_encryption()
    print(f"\nFlag: {flag}")
    print(f"\nTo verify, run: go run space_pirates3.go '{flag}'")

