# **Challenge Name: Cracking the Vault**

## Challenge Overview
The vault is locked with a key, but we've managed to access a security computer. Unfortunately, the key is encrypted, and the owner forgot to remove the file that encrypts it. It appears to be some sort of homemade encryption, but don’t worry, this should be a piece of cake for you, right?

[Crypto_3_-_Cracking_the_Vault.zip](Resources/Crypto_3_-_Cracking_the_Vault.zip)

## Solution

Unzipping the archive gives us two files:

```bash
┌──(root㉿kali)-[/home/kali/Desktop/tmp]
└─# unzip Crypto_3_-_Cracking_the_Vault.zip         
Archive:  Crypto_3_-_Cracking_the_Vault.zip
  inflating: Encryption.py           
 extracting: VaultKey_encrypted.txt
```

Let's first examine the encryption script.

```python
with open('VaultKey.txt', 'r') as f:
    text = f.read()

encrypted_text, seed = encryption(text)

with open('VaultKey_encrypted.txt', 'w') as f:
    f.write(encrypted_text)

print("The file has been successfully encrypted!")
```

The script reads from `VaultKey.txt` and encrypts it using a function, storing the result in `VaultKey_encrypted.txt`, which we have been provided.

### Encryption Function Analysis

```python
def encryption(text):
    encrypted = []
    random = secrets.SystemRandom()

    padding_length = 256 - len(text) % 256
    raw_padding = [chr(random.randint(32, 126)) for _ in range(padding_length)]

    scrambled_padding = [chr((ord(c) * 3 + 7) % 94 + 32) for c in raw_padding]
    shifted_padding = scrambled_padding[::-1]

    padded_text = ''.join(shifted_padding) + text

    final_padded_text = ''.join(
        chr((ord(c) ^ 42) % 94 + 32) if i % 2 == 0 else c
        for i, c in enumerate(padded_text)
    )

    secret_key = str(sum(ord(c) for c in text))
    secret_key = secret_key[::-1]

    hashed_key = hashlib.sha256(secret_key.encode()).hexdigest()

    seed = int(hashed_key[:16], 16)

    random = secrets.SystemRandom(seed)

    for i, char in enumerate(text):
        char_code = ord(char)
        shift = (i + 1) * 3
        transformed = (char_code + shift + 67) % 256
        encrypted.append(chr(transformed))

    return ''.join(encrypted), seed
```

### Key Observations

1. The padding consists of random printable ASCII characters (32-126), which are scrambled and prepended to the original text.
2. A transformation is applied using XOR and modular arithmetic.
3. The sum of the ASCII values of the plaintext is computed and reversed.
4. This sum is hashed using SHA-256, and the first 16 hex characters are used as a seed.
5. Each character is transformed based on its position.

### Decryption Approach

By reversing these transformations, we can recover the original VaultKey. The following script does just that:

Use [script.py](Resources/crack.py) to retrieve the flag.

```
Well done! I bet you're great at math. Here's your flag, buddy: ectf{1t_W45_ju5T_4_m1nu5}
```

### Flag
```
ectf{1t_W45_ju5T_4_m1nu5}
```

