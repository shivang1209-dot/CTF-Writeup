# Challenge Name: Augury

## Description

This is a good crypto challenge to start with. Use the help button to ask for a hint if you get stuck.

This file storage uses only the most secure encryption techniques.

**Connection:**
- `ncat --ssl augury.challs.pwnoh.io 1337`
- Or using pwntools: `remote("augury.pwnoh.io", 1337, ssl=True)`

---

## Writeup

### Step 1: Understanding the Service

The service provides a secure file storage system with three options:
1. Upload File
2. View Files
3. Exit

When uploading a file, you provide:
- A filename
- A password
- File contents in hexadecimal

The service encrypts files using a key stream cipher.

### Step 2: Analyzing the Encryption

When viewing files, the service returns encrypted data in hexadecimal format. There's a file named `secret_pic.png` that we need to decrypt.

The encryption appears to be a linear congruential generator (LCG) based key stream:
- Constants: `A = 3404970675`, `B = 3553295105`, `MOD = 2**32`
- The key stream is generated using: `k = (k * A + B) % MOD`
- The initial key is derived from the first 4 bytes of ciphertext XORed with PNG header

### Step 3: Exploiting Known Plaintext

Since we know the file is a PNG, we know the first 8 bytes are the PNG magic bytes: `89504e470d0a1a0a`.

We can:
1. Extract the initial key from the first 4 bytes of ciphertext XORed with PNG header
2. Use the LCG to generate the key stream
3. XOR the ciphertext with the key stream to recover the plaintext

### Step 4: Solution Script

The solution script:
1. Connects to the service
2. Lists available files and selects `secret_pic.png`
3. Extracts the hex-encoded ciphertext
4. Decrypts using the known PNG header and LCG key stream
5. Saves the decrypted PNG file

---

## Flag

```
bctf{pr3d1c7_7h47_k3y57r34m}
```

---

