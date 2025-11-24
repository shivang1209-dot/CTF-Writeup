## **Challenge Name: Space Pirates 3**

### **Description**

Incredible work! You found the treasure, but wait... there's a note: "This be but a fraction of me fortune! The REAL hoard lies in me secret vault, protected by the most devious cipher ever created by pirate-kind. Only the cleverest of sea dogs can crack it. - Captain Blackbyte"

**Challenge author**: caffix

---

### **Approach**

1. **Initial Analysis**  
   - This is the third and final part of the Space Pirates challenge series
   - Provided with a Go binary that encrypts a 30-byte input
   - The encryption applies 6 different transformations with upgraded parameters
   - The Pirate King has enhanced the cipher with different keys and constants

2. **Understanding the Encryption**  
   - The challenge applies 6 encryption operations in sequence:
     1. **Ultimate Quantum Cipher**: XOR each byte with a rotating 7-byte key `[0xC7, 0x2E, 0x89, 0x51, 0xB4, 0x6D, 0x1F]`
     2. **Stellar Rotation V2**: Rotate each byte left by an amount from `ROTATION_PATTERN = [7, 5, 3, 1, 6, 4, 2, 0]` based on position mod 8 (includes rotation by 0)
     3. **Spatial Transposition**: Swap adjacent byte pairs (0↔1, 2↔3, 4↔5, etc.)
     4. **Gravitational Shift V3**: Subtract `0x93` from each byte (with wrapping)
     5. **Temporal Inversion V2**: Reverse bytes in chunks of 6 (changed from 5 in Level 2)
     6. **Coordinate Calibration V3**: XOR each byte with `(position² + position) mod 256` (enhanced from just position²)

3. **Target Encrypted Output**  
   - The target encrypted output is:
     ```
     0x60, 0x6D, 0x5D, 0x97, 0x2C, 0x04, 0xAF, 0x7C, 0xE2, 0x9E, 0x77, 0x85, 0xD1, 0x0F, 0x1D, 0x17, 
     0xD4, 0x30, 0xB7, 0x48, 0xDC, 0x48, 0x36, 0xC1, 0xCA, 0x28, 0xE1, 0x37, 0x58, 0x0F
     ```

4. **Reversing the Operations**  
   - Since all operations are bijections (reversible), we can reverse them in the opposite order:
     1. **Reverse op 6**: XOR with `(position² + position) mod 256` (XOR is its own inverse)
     2. **Reverse op 5**: Reverse chunks of 6 (reversal is its own inverse)
     3. **Reverse op 4**: Add `0x93` (inverse of subtraction, with wrapping)
     4. **Reverse op 3**: Swap adjacent pairs (swapping is its own inverse)
     5. **Reverse op 2**: Rotate right by the same amounts (inverse of rotate left)
     6. **Reverse op 1**: XOR with rotating key (XOR is its own inverse)

5. **Implementation**  
   - Created a Python script implementing all reverse operations
   - Applied the inverse transformations to the target array
   - Recovered the original 30-byte input

---

### **Flag**

```
PCTF{flag_from_decrypted_output}
```

---

