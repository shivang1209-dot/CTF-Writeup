## **Challenge Name: Read My Note**

### **Description**

A fun little walk in the woods! Everything you need is located within the binary! The binary was poorly obfuscated with Qengine 2.0! It can be solved either dynamically or statically. The binary has a static base! Flag format is pctf{...}

**Challenge author**: x_ref

---

### **Approach**

1. **Initial Analysis**  
   - Identified the file as a Windows PE binary (`.exe`)
   - The binary is obfuscated with Qengine 2.0
   - The challenge mentions it can be solved statically or dynamically
   - The binary has a static base address

2. **Static Analysis**  
   - Opened the binary in a hex editor or disassembler
   - Searched for strings that might indicate flag location
   - Found the string `"The note reads:"` at file offset `0xF3D8`

3. **Locating the Encrypted Flag**  
   - Immediately after the "The note reads:" string, found a blob of printable characters at offset `0xF440`:
     ```
     ufqc~LZI5S6ZR4KA5R!Z=6g3a=\`2x
     ```
   - This appeared to be encoded or encrypted data

4. **Decryption**  
   - Attempted simple XOR decryption with various keys
   - Found that XORing the blob with a single byte key `0x05` yields readable plaintext:
     ```python
     blob = b"ufqc~LZI5S6ZR4KA5R!Z=6g3a=\`2x"
     key = 0x05
     plain = bytes([b ^ key for b in blob])
     ```
   - The decrypted text revealed the flag

5. **Verification**  
   - The decrypted string matched the expected flag format: `pctf{...}`
   - Confirmed the flag is embedded directly in the binary

---

### **Flag**

```
pctf{I_L0V3_W1ND0W$_83b6d8e7}
```

---

