## **Challenge Name: Crypto 100 - The Symmetry of Nature**

### **Description**

Consider these tales of brothers...  

You've probably heard of the constellation Gemini. Most people hear that they're identical twins, but that's actually not true. One was the son of a mortal, the other the son of Zeus. Can you imagine what it would be like to be Castor, the mortal one? If you guessed they would end up enemies, you'd be wrong.  

There was another set of brothers that went by the same names. I'm speaking, of course, of the award-winning film *Face/Off* where Castor (played by Nicolas Cage) would be considered the leader of the two, though the brother in that case is definitely the brains of the operation. Both brothers die in that film and it seems to me they were both pretty mortal.  

**Ciphertext:**  
```
84150717615789492248{688795176222681450_8273783252253178253147624750271202558794588687556525149_25153414179812378489258473}
```

---

### **Approach**

1. **Observation**  
   The challenge mentions Castor and Pollux, a reference to Morse code ciphers often associated with the Castor-Pollux cipher. This cipher maps numbers to Morse code symbols (dot, dash, or space).

2. **Breaking Down the Ciphertext**  
   - The ciphertext consists of four parts:  
     ```
     84150717615789492248
     688795176222681450
     8273783252253178253147624750271202558794588687556525149
     25153414179812378489258473
     ```
   - The first two strings form the key to solve the challenge.  

3. **Decoding the First Two Strings**  
   Using the Castor-Pollux cipher's mapping:  
   - **Space**: `0`, `6`, `9`  
   - **Dot**: `2`, `5`, `8`  
   - **Dash**: `1`, `4`, `7`  

   Applying this mapping to the first string:  
   ```
   84150717615789492248 -> .--. --- -.-. - ..-. (POCTF)
   ```
   This confirms the mapping is correct.  

4. **Decoding the Last Two Strings**  
   The third and fourth strings include an additional number (`3`) that was not used in the initial mapping. Through trial and error, the updated mapping was identified:  
   - **Space**: `0`, `6`, `9`, `3`  
   - **Dot**: `2`, `5`, `8`  
   - **Dash**: `1`, `4`, `7`  

   Using this mapping, the third and fourth strings are decoded to form the rest of the flag.  

5. **Final Decoded Flag**  
   ```
   POCTF{UWSP_UN57OPP4BL3_F0RC3}
   ```

---

### **Flag**

`poctf{uwsp_un57Opp4bl3_f0rc3}`

--- 
