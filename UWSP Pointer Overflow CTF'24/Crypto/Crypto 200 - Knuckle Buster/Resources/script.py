from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key, load_pem_parameters
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

# Load DH parameters
dh_parameters_pem = b"""-----BEGIN DH PARAMETERS-----
MEYCQQCIEH8WULdbxo8snFgZfMqyekSY8ogpHgl62UDWTL5MpNih9dQpIW5wbG2uZaVUWOctlSokWOPRtUMpKJg5+h3XAgEC
-----END DH PARAMETERS-----"""
dh_parameters = load_pem_parameters(dh_parameters_pem, backend=default_backend())

# Load Alice's public key
public_key_pem = b"""-----BEGIN PUBLIC KEY-----
MIGaMFMGCSqGSIb3DQEDATBGAkEAiBB/FlC3W8aPLJxYGXzKsnpEmPKIKR4JetlA1ky+TKTYofXUKSFucGxtrmWlVFjnLZUqJFjj0bVDKSiYOfod1wIBAgNDAAJAN3YrjXtIssyugO9tQ3BRy2TN92Qkhkp/VP5zfLEMQg1AE/YofkCIc/KSZOBpuroiQoCK0qTNkD4HzCzDa7ap5Q==
-----END PUBLIC KEY-----"""
public_key = load_pem_public_key(public_key_pem, backend=default_backend())

# Load Bob's private key
private_key_pem = b"""-----BEGIN PRIVATE KEY-----
MIGcAgEAMFMGCSqGSIb3DQEDATBGAkEAiBB/FlC3W8aPLJxYGXzKsnpEmPKIKR4JetlA1ky+TKTYofXUKSFucGxtrmWlVFjnLZUqJFjj0bVDKSiYOfod1wIBAgRCAkBSsgvp3xivPK6Wp2X+SIjGllg1MT4zJdEoyUjV6iDLGytdeLpokYOO6xsGIiVb8b6A/5onnopra2iXBb0dS5rn
-----END PRIVATE KEY-----"""
private_key = load_pem_private_key(private_key_pem, password=None, backend=default_backend())

# Generate the shared secret using Diffie-Hellman
shared_secret = private_key.exchange(public_key)

# Derive the AES key from the shared secret using SHA-256
digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
digest.update(shared_secret)
aes_key = digest.finalize()

# Load the encrypted file
with open("Crypto200-1_flag.txt.enc", "rb") as file:
    file_content = file.read()

# Extract the IV (first 16 bytes) and the encrypted message (remaining bytes)
iv = file_content[:16]
encrypted_flag = file_content[16:]

# Decrypt the message using AES-256-CBC
cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
decryptor = cipher.decryptor()
decrypted_message = decryptor.update(encrypted_flag) + decryptor.finalize()

# Print the decrypted flag
print(decrypted_message.decode('utf-8'))
