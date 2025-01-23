def ksa(key):
    """
    Key Scheduling Algorithm (KSA)
    Initializes the permutation (S) based on the provided key.
    """
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + ord(key[i % key_length])) % 256
        S[i], S[j] = S[j], S[i]  
    return S


def prga(S, ciphertext_length):
    """
    Pseudo-Random Generation Algorithm (PRGA)
    Generates the keystream to XOR with the ciphertext.
    """
    i = 0
    j = 0
    keystream = []
    for _ in range(ciphertext_length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        keystream.append(K)
    return keystream


def rc4_decrypt(ciphertext, key):
    S = ksa(key)
    keystream = prga(S, len(ciphertext))
    # XOR each byte of ciphertext with the keystream to get plaintext
    plaintext = ''.join(chr(c ^ k) for c, k in zip(ciphertext, keystream))
    return plaintext


# Ciphertext in hexadecimal form
hex_ciphertext = "71 81 13 f7 f7 b2 87 bd c6 77 68 67 25 ae fd 99 00 6e 2e 53 e6 60 50 50 ae a8 0f 9b 0a"
# Convert hex string to bytes
ciphertext = bytes.fromhex(hex_ciphertext.replace(" ", ""))

wordlist_path = "wordlist.txt"

# Bruteforce through each word in the wordlist
with open(wordlist_path, "r") as wordlist:
    for word in wordlist:
        key = word.strip().upper()  # Remove any newline characters and convert to Uppercase
        decrypted_text = rc4_decrypt(ciphertext, key)
        # Print or check if the decrypted text contains known flag format
        if "poctf" in decrypted_text:
            print(f"Possible key: {key}")
            print(f"Decrypted text: {decrypted_text}")
            break