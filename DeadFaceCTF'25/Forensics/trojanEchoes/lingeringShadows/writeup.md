## **Challenge Name: lingeringShadows**

### **Description**

Using the artifacts from Trojan Echoes: What is the Password?, find the flag labeled flag 02.

Submit the flag as deadface{here-is-the-answer}.

**Note**: Use the artifacts from Trojan Echoes: What is the Password?

---

### **Approach**

1. **Binary Analysis**  
   - Used Binary Ninja (or similar reverse engineering tool) to analyze the binary
   - Examined the decompiled code and strings

2. **Finding Base64 Blocks**  
   - Located Base64-encoded blocks in the strings, found right after the first flag
   - Found multiple Base64 segments:
     ```
     aWxl
     bl9h
     dHNf
     LSBk
     ZmFj
     ZXtJ
     ZWFk
     YmVl
     X3do
     MDIg
     fQ==
     ```

3. **Assembling the Flag**  
   - After several attempts, successfully assembled the Base64 string in the correct order
   - Decoded the complete Base64 string to get: `02 - deadface{Its_been_a_while}`

4. **Source Code Analysis**  
   - Found the source code that constructs this flag:
     ```c
     char const* const _Source_43 = "aWxl"
     char const* const _Source_42 = "bl9h"
     char const* const _Source_41 = "dHNf"
     char const* const _Source_40 = "LSBk"
     char const* const _Source_39 = "ZmFj"
     char const* const _Source_38 = "ZXtJ"
     char const* const _Source_37 = "ZWFk"
     char const* const _Source_36 = "YmVl"
     char const* const _Source_35 = "X3do"
     char const* const _Source_34 = "MDIg"
     char const* const _Source_33 = "fQ=="
     ```
   - The program uses `strcat` to concatenate these strings in a specific order

---

### **Flag**

```
deadface{Its_been_a_while}
```

---

