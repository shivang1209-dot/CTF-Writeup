## **Challenge Name: Crypto 300 - Put Down Thy Wrath**

### **Description**

In this challenge, a public key and an encrypted message are provided. The message was encrypted using a flawed implementation of homomorphic encryption. The task is to analyze the encryption script, identify its weaknesses, and decrypt the message to reveal the flag.

**Provided Data**:  
- Ciphertext (C):  
  ```
  79,74,3f,0f,5a,27,21,3a,36,48,64,51,64,0f,79,7e,1a,64,64,03,33,0f,64,64,57,21,27,3f,0f,2c,4a,3a,3f,24,27,3f,0f,7e,64,79,1a,64,2c
  ```
- Public Key: `3233`  

**File Provided**:  
- [Crypto300-3_homomorphic_encryption.py](Resources/Crypto300-3_homomorphic_encryption.py)

---

### **Approach**

1. **Examining the Script**:  
   After inspecting the provided encryption script, it became evident that the challenge implementation contained a critical error. The author unintentionally left the flag directly embedded in the script.

2. **Extracting the Flag**:  
   No cryptanalysis or decryption was required since the flag was exposed within the script.

---

### **Flag**

`poctf{uwsp_T3mp357_4nd_7urnm01l}`

---