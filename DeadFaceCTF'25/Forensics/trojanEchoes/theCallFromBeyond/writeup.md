## **Challenge Name: theCallFromBeyond**

### **Description**

Using the artifacts from Trojan Echoes: What is the Password?, find the flag labeled flag 03.

Submit the flag as deadface{here-is-the-answer}.

**Note**: Use the artifacts from Trojan Echoes: What is the Password?

---

### **Approach**

1. **Binary Analysis**  
   - Used Binary Ninja (or similar reverse engineering tool) to analyze the binary
   - Examined the decompiled code for Base64-encoded strings

2. **Finding Base64 Blocks**  
   - Located Base64-encoded blocks in the source code
   - Found multiple Base64 segments that need to be assembled:
     ```c
     char const* const _Source_32 = "aG91"
     char const* const _Source_31 = "aGVy"
     char const* const _Source_30 = "LSBk"
     char const* const _Source_29 = "ZmFj"
     char const* const _Source_28 = "ZXtX"
     char const* const _Source_27 = "ZWFk"
     char const* const _Source_26 = "ZV9z"
     char const* const _Source_25 = "d2Vf"
     char const* const _Source_24 = "YmVn"
     char const* const _Source_23 = "bGRf"
     char const* const _Source_22 = "MDMg"
     char const* const _Source_21 = "aW59"
     ```

3. **Assembling the Flag**  
   - Analyzed the source code to understand the order of concatenation:
     ```c
     strcat(&var_318, _Source_22)  // "MDMg"
     strcat(&var_318, _Source_30)  // "LSBk"
     strcat(&var_318, _Source_27)  // "ZWFk"
     strcat(&var_318, _Source_29)  // "ZmFj"
     strcat(&var_318, _Source_28)  // "ZXtX"
     strcat(&var_318, _Source_31)  // "aGVy"
     strcat(&var_318, _Source_26)  // "ZV9z"
     strcat(&var_318, _Source_32)  // "aG91"
     strcat(&var_318, _Source_23)  // "bGRf"
     strcat(&var_318, _Source_25)  // "d2Vf"
     strcat(&var_318, _Source_24)  // "YmVn"
     strcat(&var_318, _Source_21)  // "aW59"
     ```
   - Assembled the Base64 string in the correct order
   - Decoded the Base64 to get: `03 - deadface{Where_should_we_begin}`

---

### **Flag**

```
deadface{Where_should_we_begin}
```

---

