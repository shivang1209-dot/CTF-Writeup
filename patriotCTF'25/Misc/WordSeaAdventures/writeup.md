## **Challenge Name: Word Sea Adventures**

### **Description**

Our experts found this weird word document in our file share. They couldn't find anything inside. Maybe you could look more closely and find the hidden prize within!

No passphrases are needed for this challenge.

The flag format will be tctf{flag} or pctf{flag}

**Challenge author**: DJ Strigel

---

### **Approach**

1. **Initial Analysis**  
   - Provided with a Word document: `word_sea_adventures.docx`
   - Opened the document but found nothing visible
   - Need to look deeper into the file structure

2. **Understanding DOCX Format**  
   - DOCX files are ZIP archives containing XML and other files
   - Can be extracted using archive tools like `7z` or `unzip`
   - Extracted the DOCX file:
     ```bash
     7z x word_sea_adventures.docx
     ```

3. **Examining Extracted Contents**  
   - Found 3 JPEG files in the extracted contents:
     - `crab.jpg`
     - `sponge.jpg`
     - `squid.jpg`
   - These images are embedded in the Word document

4. **Steganography Analysis**  
   - Used `stegseek` to check for hidden data in each image:
     ```bash
     stegseek crab.jpg
     stegseek sponge.jpg
     stegseek squid.jpg
     ```
   - All three images contained hidden data with empty passphrase

5. **Extracting Hidden Data**  
   - Extracted hidden files from each image:
     - `crab.jpg.out` - Contains: "Mr Crabs heard that his cashier may be hiding some money and maybe a flag somewhere."
     - `sponge.jpg.out` - Contains: "Spongebob is so chill! Why would he be hiding any flags?"
     - `squid.jpg.out` - Contains the flag:
       ```
       I guess you found handsome squidward... even his looks can't hide the flag.
       tctf{w0rD_f1le5_ar3_als0_z1p}
       ```

6. **Finding the Flag**  
   - The flag was hidden in `squid.jpg` using steganography
   - Successfully extracted the flag from the hidden file

---

### **Flag**

```
tctf{w0rD_f1le5_ar3_als0_z1p}
```

---

