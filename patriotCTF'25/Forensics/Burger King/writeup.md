## **Challenge Name: Burger King**

### **Description**

I just got around to starting up my own forensics team. We're calling our selves the Burger King Crackers for our exceptional skills at getting information out of encrypted systems left by cyber criminals. Our first big case has finally arrived but there is just one file we can't seem to solve. The cyber criminals left over this encrypted zip file containing their plans. We were able to recover the first part of a file, but thats it. Can you recover their evil plans?

The flag format is CACI{flag}

**Challenge author**: Matthew Johnson (CACI)

---

### **Approach**

1. **Initial Analysis**  
   - Provided with:
     - An encrypted ZIP file: `BurgerKing.zip`
     - A partial file: `partial.svg` (the first 39 bytes of one of the encrypted files)
   - This is a **known plaintext attack** scenario

2. **Understanding Known Plaintext Attack**  
   - ZIP encryption can be broken if we know part of the plaintext
   - We have the first 39 bytes of `Space.svg` from the encrypted ZIP
   - Can use this to recover the encryption keys

3. **Using bkcrack**  
   - Installed bkcrack tool:
     ```bash
     git clone https://github.com/kimci86/bkcrack.git
     cd bkcrack
     mkdir build && cd build
     cmake ..
     make
     ```
   - Performed the known plaintext attack:
     ```bash
     bkcrack -C BurgerKing.zip -c Space.svg -p partial.svg
     ```
   - Successfully recovered the encryption keys:
     ```
     Keys: b9540c69 069a11f9 fd31648f
     ```

4. **Decrypting the ZIP File**  
   - Used the recovered keys to create a new unlocked ZIP file:
     ```bash
     bkcrack -C BurgerKing.zip -k b9540c69 069a11f9 fd31648f -U BurgerKing_decrypted.zip password
     ```
   - Created `BurgerKing_decrypted.zip` with password "password"

5. **Extracting Files**  
   - Extracted the decrypted ZIP:
     ```bash
     unzip -P password BurgerKing_decrypted.zip -d extracted/
     ```
   - The ZIP contains 5 SVG files:
     - `Hole.svg`
     - `LockAndKey.svg`
     - `Space.svg`
     - `SVGsSuck.svg`
     - `Webs.svg`

6. **Finding the Flag**  
   - Opened each SVG file in an image viewer
   - The flag text is rendered as part of one of the SVG images
   - Found the flag in the image content

---

### **Flag**

```
CACI{Y0U_F0UND_M3!}
```

---

