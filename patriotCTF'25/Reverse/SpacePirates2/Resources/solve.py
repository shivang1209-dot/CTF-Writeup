#!/usr/bin/env python3
"""
Reverse engineering solution for Space Pirates 2 challenge
Reverses the 6 encryption operations to find the original input
"""

FLAG_LEN = 32
TARGET = [
    0x15, 0x5A, 0xAC, 0xF6, 0x36, 0x22, 0x3B, 0x52, 0x6C, 0x4F, 0x90, 0xD9, 0x35, 0x63, 0xF8, 0x0E, 
    0x02, 0x33, 0xB0, 0xF1, 0xB7, 0x69, 0x42, 0x67, 0x25, 0xEA, 0x96, 0x63, 0x1B, 0xA7, 0x03, 0x0B
]

XOR_KEY = [0x7E, 0x33, 0x91, 0x4C, 0xA5]
ROTATION_PATTERN = [1, 3, 5, 7, 2, 4, 6]
MAGIC_SUB = 0x5D

def rotate_right(byte, n):
    """Rotate a byte right by n positions (inverse of rotate_left)"""
    return ((byte >> (n % 8)) | (byte << (8 - (n % 8)))) & 0xFF

def reverse_encryption():
    """
    Reverse the encryption operations in reverse order:
    1. Start with TARGET
    2. Reverse op 6: XOR with position squared
    3. Reverse op 5: Reverse chunks of 5
    4. Reverse op 4: Add MAGIC_SUB (inverse of subtraction)
    5. Reverse op 3: Swap adjacent pairs
    6. Reverse op 2: Rotate right by rotation amounts
    7. Reverse op 1: XOR with rotating key
    """
    buffer = list(TARGET)
    
    print("Starting with TARGET:")
    print(f"  {[hex(b) for b in buffer]}\n")
    
    # Reverse operation 6: XOR with position squared (XOR is its own inverse)
    print("[Reverse 6/6] Reversing coordinate calibration (XOR with position squared)...")
    for i in range(FLAG_LEN):
        position_squared = ((i * i) % 256) & 0xFF
        buffer[i] ^= position_squared
    print(f"  After reverse op 6: {[hex(b) for b in buffer[:10]]}...\n")
    
    # Reverse operation 5: Reverse chunks of 5 (reversal is its own inverse)
    print("[Reverse 5/6] Reversing temporal inversion (reverse chunks of 5)...")
    CHUNK_SIZE = 5
    for chunk_start in range(0, FLAG_LEN, CHUNK_SIZE):
        chunk_end = min(chunk_start + CHUNK_SIZE, FLAG_LEN)
        buffer[chunk_start:chunk_end] = reversed(buffer[chunk_start:chunk_end])
    print(f"  After reverse op 5: {[hex(b) for b in buffer[:10]]}...\n")
    
    # Reverse operation 4: Add MAGIC_SUB (inverse of subtraction, with wrapping)
    print("[Reverse 4/6] Reversing gravitational shift (add 0x5D)...")
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
        rotation = ROTATION_PATTERN[i % 7]
        buffer[i] = rotate_right(buffer[i], rotation)
    print(f"  After reverse op 2: {[hex(b) for b in buffer[:10]]}...\n")
    
    # Reverse operation 1: XOR with rotating key (XOR is its own inverse)
    print("[Reverse 1/6] Reversing quantum entanglement cipher (XOR with key)...")
    for i in range(FLAG_LEN):
        buffer[i] ^= XOR_KEY[i % 5]
    print(f"  After reverse op 1: {[hex(b) for b in buffer[:10]]}...\n")
    
    # Convert to string
    result = ''.join(chr(b) for b in buffer)
    
    print("=" * 50)
    print("DECRYPTED TREASURE MAP:")
    print(f"  {result}")
    print("=" * 50)
    
    return result

if __name__ == "__main__":
    flag = reverse_encryption()
    print(f"\nFlag: {flag}")
    print(f"\nTo verify, run: cargo run --release '{flag}'")

