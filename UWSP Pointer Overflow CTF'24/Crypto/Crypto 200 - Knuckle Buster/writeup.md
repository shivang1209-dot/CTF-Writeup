## **Challenge Name: Crypto 200 - Knuckle Buster**

### **Description**

In this challenge, two individuals—Alice and Bob—are communicating in secret. They use the Diffie-Hellman key exchange protocol to protect their communication. I will provide you with enough information to decrypt a message intercepted between them. All you need to do is calculate the shared secret and decrypt it to get the flag.

Here is the encrypted flag. It was encrypted using AES-256-CBC, with SHA-256 for key derivation and a prepended 16 byte IV.

publicA
-----BEGIN PUBLIC KEY-----
MIGaMFMGCSqGSIb3DQEDATBGAkEAiBB/FlC3W8aPLJxYGXzKsnpEmPKIKR4JetlA1ky+TKTYofXUKSFucGxtrmWlVFjnLZUqJFjj0bVDKSiYOfod1wIBAgNDAAJAN3YrjXtIssyugO9tQ3BRy2TN92Qkhkp/VP5zfLEMQg1AE/YofkCIc/KSZOBpuroiQoCK0qTNkD4HzCzDa7ap5Q==
-----END PUBLIC KEY-----

privateB
-----BEGIN PRIVATE KEY-----
MIGcAgEAMFMGCSqGSIb3DQEDATBGAkEAiBB/FlC3W8aPLJxYGXzKsnpEmPKIKR4JetlA1ky+TKTYofXUKSFucGxtrmWlVFjnLZUqJFjj0bVDKSiYOfod1wIBAgRCAkBSsgvp3xivPK6Wp2X+SIjGllg1MT4zJdEoyUjV6iDLGytdeLpokYOO6xsGIiVb8b6A/5onnopra2iXBb0dS5rn
-----END PRIVATE KEY-----

dhparam
-----BEGIN DH PARAMETERS-----
MEYCQQCIEH8WULdbxo8snFgZfMqyekSY8ogpHgl62UDWTL5MpNih9dQpIW5wbG2uZaVUWOctlSokWOPRtUMpKJg5+h3XAgEC
-----END DH PARAMETERS-----

**File provided**: [Crypto200-1_flag.txt.enc](Resources/Crypto200-1_flag.txt.enc)

---

### **Approach**

1. **Load Cryptographic Keys**  
   - Load the Diffie-Hellman parameters, Alice's public key, and Bob's private key from the provided PEM format.

2. **Generate Shared Secret**  
   - Use Bob's private key and Alice's public key to compute the shared secret through the Diffie-Hellman key exchange protocol.

3. **Derive AES Key**  
   - Derive the AES-256 key from the shared secret by hashing it with SHA-256.

4. **Read Encrypted File**  
   - Read the provided encrypted file to extract the initialization vector (IV) and the encrypted message.

5. **Decrypt Message**  
   - Use the derived AES-256 key and the extracted IV to decrypt the message using the AES-256-CBC encryption mode, which will reveal the original plaintext (flag).

---

I used the [script.py](Resources/script.py) to solve this challenge.

---

### **Flag**

`poctf{uwsp_f1r3_4nd_br1m570n3}`

--- 
