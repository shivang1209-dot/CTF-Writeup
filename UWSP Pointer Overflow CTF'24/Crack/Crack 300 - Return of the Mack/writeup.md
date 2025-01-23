## **Challenge Name: Crack 300 - Return of the Mack**

### **Description**

Sterling Archer. Code name: Duchess. Known from Berlin to Bangkok as the world's most dangerous spy. So, for us, this is... How you say? A good get. But not so good for you, Mr. Archer. Because you have information that I want. And this may be an old cliché but... We have ways of making you talk.

The message below was recovered from Sealab's master computer in 2021. We know that it is a secret transmission between Mr. Reed and Dr. P. Haze. We also know that you know the code to this private key to decrypt it. You will give us that code. No games, Archer, 6 characters, A-Z and 0-9 only.

---

### **Approach**

1. **Background Information**  
   - References to Sealab 2021, Sterling Archer (aka Duchess), and Dr. P Haze give clues that this challenge may involve **RSA encryption** with a private key protected by a password.

2. **Key Decryption**  
   - A private RSA key (`keyfile.pem`) was provided, which was protected by a 6-character password.  
   - Using the hint about the password format (`A-Z` and `0-9`), brute-forcing was a potential solution, but the password was found to be `934TXS`.

3. **Decrypting the RSA Key**  
   - The RSA key was decrypted using the following OpenSSL command:  
     ```bash
     openssl rsa -in keyfile.pem -out decrypted_key.pem
     ```
   - The password `934TXS` was used successfully to decrypt and output the usable private key to `decrypted_key.pem`.

4. **Decrypting the Flag**  
   - With the decrypted private key, the next step was to decrypt the provided ciphertext file (`Crack300-2_flag.txt.enc`) using RSA decryption:  
     ```bash
     openssl rsautl -decrypt -inkey decrypted_key.pem -in Crack300-2_flag.txt.enc -out decrypted_message.txt
     ```
   - This yielded the final decrypted message containing the flag.

---

### **Flag**

`poctf{uwsp_h34r7_0f_7h3_m4773r}`

--- 
