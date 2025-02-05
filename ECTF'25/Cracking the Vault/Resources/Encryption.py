import secrets
import hashlib

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

with open('VaultKey.txt', 'r') as f:
    text = f.read()

encrypted_text, seed = encryption(text)

with open('VaultKey_encrypted.txt', 'w') as f:
    f.write(encrypted_text)

print("The file has been successfully encrypted!")
