## **Challenge Name: watchTheBirdies**

### **Description**

Using the artifacts from Trojan Echoes: What is the Password?, find the flag labeled flag 04.

Submit the flag as deadface{here-is-the-answer}.

**Note**: Use the artifacts from Trojan Echoes: What is the Password?

---

### **Approach**

1. **Binary Analysis**  
   - Used Binary Ninja (or similar reverse engineering tool) to analyze the binary
   - Examined the decompiled code for encoded strings

2. **Finding Encoded Strings**  
   - Found a relevant source code section with hex strings:
     ```c
     __builtin_strcpy(&var_2e8, "78 65 78 73 63 32 116 104 101 32 102 108 97 103 32 104 97 115 32 100 105 115 97 112 112 101 97 114 " "100 33")
     ```
   - Also found another set of hex strings:
     ```c
     char const* const _Source_20 = "/4c/53"
     char const* const _Source_19 = "/5a/58"
     // ... more source strings
     ```

3. **Decoding the First String**  
   - Decoded the first hex string:
     ```python
     nums = [78,65,78,73,63,32,116,104,101,32,102,108,97,103,32,104,97,115,32,100,105,115,97,112,112,101,97,114,100,33]
     "".join(chr(n) for n in nums)
     # Result: 'NANI? the flag has disappeard!'
     ```
   - This was a misdirection

4. **Assembling the Hex String**  
   - Found the source code that constructs a hex string from multiple segments:
     ```c
     strcat(&var_3c8, "/4d/44")
     strcat(&var_3c8, _Source_15)  // "/51/67"
     strcat(&var_3c8, _Source_20)  // "/4c/53"
     // ... continues with all sources in order
     ```
   - Assembled the complete hex string: `/4d/44/51/67/4c/53/42/6b/5a/57/46/6b/5a/6d/46/6a/5a/58/74/47/5a/57/56/73/63/31/39/73/61/57/74/6c/58/32/5a/76/63/6d/56/32/5a/58/4a/39`

5. **Decoding the Flag**  
   - Removed the `/` characters and decoded the hex string
   - Result: `MDQgLSBkZWFkZmFjZXtGZWVsc19saWtlX2ZvcmV2ZXJ9`
   - Decoded the Base64: `04 - deadface{Feels_like_forever}`

---

### **Flag**

```
deadface{Feels_like_forever}
```

---

