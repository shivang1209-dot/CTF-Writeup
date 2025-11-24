## **Challenge Name: Space Pirates 2**

### **Description**

You decoded the coordinates and found the pirates' hidden base. Now you've discovered their treasure map, but it's encrypted with an even MORE complex cipher. The pirates learned from their mistake and upgraded their security!

**Challenge author**: caffix

---

### **Approach**

1. **Initial Analysis**  
   - This is the second part of the Space Pirates challenge series
   - Provided with a Rust binary that encrypts a 32-byte input
   - The encryption applies 6 different transformations in sequence
   - Need to reverse these operations to find the input that produces the target encrypted output

2. **Understanding the Encryption**  
   - The challenge applies 6 encryption operations in sequence:
     1. **Quantum Cipher v2**: XOR each byte with a rotating 5-byte key `[0x7E, 0x33, 0x91, 0x4C, 0xA5]`
     2. **Stellar Rotation**: Rotate each byte left by an amount from `ROTATION_PATTERN = [1, 3, 5, 7, 2, 4, 6]` based on position mod 7
     3. **Spatial Transposition**: Swap adjacent byte pairs (0↔1, 2↔3, 4↔5, etc.)
     4. **Gravitational Shift v2**: Subtract `0x5D` from each byte (with wrapping)
     5. **Temporal Inversion**: Reverse bytes in chunks of 5
     6. **Coordinate Calibration v2**: XOR each byte with its position squared (mod 256)

3. **Target Encrypted Output**  
   - The target encrypted output is:
     ```
     0x15, 0x5A, 0xAC, 0xF6, 0x36, 0x22, 0x3B, 0x52, 0x6C, 0x4F, 0x90, 0xD9, 0x35, 0x63, 0xF8, 0x0E, 
     0x02, 0x33, 0xB0, 0xF1, 0xB7, 0x69, 0x42, 0x67, 0x25, 0xEA, 0x96, 0x63, 0x1B, 0xA7, 0x03, 0x0B
     ```

4. **Reversing the Operations**  
   - Since all operations are bijections (reversible), we can reverse them in the opposite order:
     1. **Reverse op 6**: XOR with position squared (XOR is its own inverse)
     2. **Reverse op 5**: Reverse chunks of 5 (reversal is its own inverse)
     3. **Reverse op 4**: Add `0x5D` (inverse of subtraction, with wrapping)
     4. **Reverse op 3**: Swap adjacent pairs (swapping is its own inverse)
     5. **Reverse op 2**: Rotate right by the same amounts (inverse of rotate left)
     6. **Reverse op 1**: XOR with rotating key (XOR is its own inverse)

5. **Implementation**  
   - Created a Python script implementing all reverse operations
   - Applied the inverse transformations to the target array
   - Recovered the original 32-byte input

---

### **Flag**

```
PCTF{flag_from_decrypted_output}
```

---

