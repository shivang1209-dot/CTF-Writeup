## **Challenge Name: Space Pirates**

### **Description**

You've intercepted an encrypted transmission from space pirates! Decode their secret coordinates to find their hidden treasure.

**Challenge author**: caffix

---

### **Approach**

1. **Initial Analysis**  
   - Provided with a C program that encrypts an input string
   - The program compares the encrypted output against a target array
   - Need to reverse the encryption operations to find the original input

2. **Understanding the Encryption**  
   - The encryption applies 4 operations in sequence:
     1. **XOR with rotating key**: Each byte is XORed with one of 5 key bytes (cycling: `0x42, 0x73, 0x21, 0x69, 0x37`)
     2. **Swap adjacent byte pairs**: Bytes at positions (0,1), (2,3), (4,5), etc. are swapped
     3. **Add magic constant**: Each byte has `0x2A` added to it (mod 256)
     4. **XOR with position**: Each byte is XORed with its position index

3. **Target Array**  
   - The target encrypted output is:
     ```
     0x5A,0x3D,0x5B,0x9C,0x98,0x73,0xAE,0x32,0x25,0x47,0x48,0x51,0x6C,0x71,0x3A,0x62,0xB8,0x7B,0x63,0x57,0x25,0x89,0x58,0xBF,0x78,0x34,0x98,0x71,0x68,0x59
     ```

4. **Reversing the Operations**  
   - To decrypt, apply the inverse operations in reverse order:
     1. **Reverse op 4**: XOR with position (XOR is its own inverse)
     2. **Reverse op 3**: Subtract `0x2A` (mod 256) - handle underflow with modulo
     3. **Reverse op 2**: Swap adjacent pairs again (swapping is its own inverse)
     4. **Reverse op 1**: XOR with rotating key (XOR is its own inverse)

5. **Implementation**  
   - Created a Python script to reverse all operations
   - Applied the inverse transformations to the target array
   - Recovered the original input string

6. **Verification**  
   - Ran the challenge binary with the decrypted flag
   - Verified it successfully decrypts and displays the treasure

---

### **Flag**

```
PCTF{0x_M4rks_tH3_sp0t_M4t3ys}
```

---

