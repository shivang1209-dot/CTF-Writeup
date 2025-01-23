## **Challenge Name: Crypto 100 - Fortune and Failure**

### **Description**

Normally in a situation like this, you'd receive a clue about the key. However, this time, no such clue is needed for three reasons:  
1) The key is short.  
2) You know part of the message.  
3) 

**Cipher text**:  
```
hottx{unsh_4_w4ck_7zrfuyh_7y3_h1dl5}
```

---

### **Approach**

1. **Observation**  
   - The ciphertext resembles the format of a flag: `{}` containing readable patterns with underscores and numbers.
   - The problem indicates that part of the plaintext is already known, and the transformation alternates between two patterns for letters.

2. **Decoding Logic**  
   - Alternate characters are shifted using a **rotation cipher (ROT)**:  
     - Every **odd-positioned letter** is shifted by **+18**.  
     - Every **even-positioned letter** is shifted by **+17**.  
   - Non-alphabetic characters (e.g., numbers, underscores, and braces) remain unchanged.

3. **Step-by-Step Decryption**  
   - Apply reverse shifts to decode the flag:
     - Odd positions (apply `-18` shift).  
     - Even positions (apply `-17` shift).

   - Manual decoding example:  
     ```
     Ciphertext: hottx{unsh_4_w4ck_7zrfuyh_7y3_h1dl5}
     Decryption:
       h -> p (-18)
       o -> o (unchanged)
       t -> c (-17)
       t -> t (unchanged)
       x -> f (-18)
       { -> { (unchanged)
       u -> u (unchanged)
       n -> w (-17)
       s -> s (unchanged)
       h -> p (-18)
       _ -> _ (unchanged)
       ...
     ```

   - Continuing this process yields:  
     ```
     poctf{uwsp_4_w4lk_7hrough_7h3_h1ll5}
     ```

---

### **Flag**

`poctf{uwsp_4_w4lk_7hrough_7h3_h1ll5}`

--- 
