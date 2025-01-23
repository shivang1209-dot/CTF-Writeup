## **Challenge Name: Crypto 200 - Everyone's Friend**

### **Description**

iykyk, amirite? rsa af. gl, hf. poctf2024.  

```
p = 61  
q = 53  
n = 3233  
e = 17  
c = 264,889,119,374,559,357,870,453,4ce,264,77,a5d,87a,170,77,87a,b5a,a5d,119,87a,87a,b5a,2b2,170,96c,70a,77,7aa,870,b5a,6ed,170,5ec
```

---

### **Approach**

Given the challenge text, it's evident that the problem involves RSA encryption. All the necessary values for decryption are provided:  
- \( p = 61 \)  
- \( q = 53 \)  
- \( n = 3233 \)  
- \( e = 17 \)  
- Encrypted message \( c \).  

#### Step 1: Calculate Private Key (d)  
To decrypt the ciphertext, we first calculate \( d \), the modular multiplicative inverse of \( e \) modulo \( \phi(n) \).  
\[
\phi(n) = (p-1) \times (q-1) = 3120
\]  

Using the Extended Euclidean Algorithm, we find:
\[
d = e^{-1} \mod \phi(n)
\]

#### Step 2: Verify Encryption  
I created an encryption script, [encrypt.py](Resources/encrypt.py), to test the provided values by encrypting a known plaintext (`poctf{uwsp_`). The script correctly reproduced the provided hexadecimal values, confirming the setup.

#### Step 3: Decrypt the Ciphertext  
Using \( d \), I created a decryption script, [decrypt.py](Resources/decrypt.py), to decrypt the provided ciphertext. The script successfully revealed the flag.

**Decryption Result:**  
`poctf{uwsp_7h3_h17chh1k3r5_6u1d3}`  

---

### **Flag**

`poctf{uwsp_7h3_h17chh1k3r5_6u1d3}`

---