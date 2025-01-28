## **Challenge Name: Reverse 200 - Planned Obsequence**  

---

### **Description**  

In the lower-level RE challenges, I typically leave the flag or an encoded version in the code for participants to extract. This time, I've redacted the flag in the original code. If you look, you'll see it there. But don't worry, the obfuscated flag is there, buried in a variable somewhere. If you want to get it back, find the encoded flag and reverse the encoding process. It's a two-step process before you convert it back to ASCII so you will know if you're on the right track after just a few characters.  

#### **File Provided**  
- [Reverse200-1](Resources/Reverse200-1)  

---

### **Approach**  

1. **Extract the Obfuscated Flag**  
   - The obfuscated flag is found in the code:  
     ```
     2d383c313f2432302c2d08710870356e376f086d3f083b6c713270262a
     ```

2. **Analyze the Encoding Scheme**  
   - The encoded flag follows a two-step obfuscation process:  
     - Subtract 3 from each hexadecimal byte.  
     - XOR the result with `0x5A`.  

3. **Write a Decoding Script**  
   - Here's the provided [Python script](Resources/script.py) that successfully reverses the obfuscation:  
     ```python  
     # Hexadecimal representation of the obfuscated flag  
     hex_obfuscated_flag = "2d383c313f2432302c2d08710870356e376f086d3f083b6c713270262a"  

     # Convert hex to ASCII characters  
     obfuscated_flag = bytes.fromhex(hex_obfuscated_flag)  

     def deobfuscate(flag):  
         deobfuscated_flag = ""  
         for char in flag:  
             # Reverse the obfuscation steps: subtract 3, then XOR with 0x5A  
             original_char = (char - 3) ^ 0x5A  
             deobfuscated_flag += chr(original_char)  
         return deobfuscated_flag  

     # Run deobfuscation  
     flag = deobfuscate(obfuscated_flag)  
     print("Deobfuscated Flag:", flag)  
     ```

4. **Run the Script**  
   - The script decodes the obfuscated flag into the final flag:  
     ```
     poctf{uwsp_4_7h1n6_0f_b34u7y}
     ```

---

### **Flag**  

`poctf{uwsp_4_7h1n6_0f_b34u7y}`  

---