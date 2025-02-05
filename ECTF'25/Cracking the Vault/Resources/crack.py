import hashlib

def seed_gen(text):
    secret_key = str(sum(ord(c) for c in text))[::-1]
    return int(hashlib.sha256(secret_key.encode()).hexdigest()[:16], 16)

def decrypt(encrypted_text, seed):
    return ''.join(chr((ord(c) - 67 - (i + 1) * 3) % 256) for i, c in enumerate(encrypted_text))

with open('VaultKey_encrypted.txt', 'r', encoding='utf-8', errors='ignore') as f:
    encrypted_text = f.read()

seed = seed_gen(encrypted_text)
decrypted_text = decrypt(encrypted_text, seed)

with open('flag.txt', 'w', encoding='utf-8') as f:
    f.write(decrypted_text.strip())

print("Decryption complete!")
