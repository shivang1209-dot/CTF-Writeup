## **Challenge Name: whatsThePassword**

### **Description**

Using the artifacts from Trojan Echoes, find the password for the ZIP file.

Submit the flag as deadface{password}.

**Note**: Use the artifacts from Trojan Echoes

---

### **Approach**

1. **Accessing the ZIP File**  
   - The challenge references a ZIP file from the Trojan Echoes artifacts
   - The ZIP file contains `sample_01E9.exe.exe` and `flag.txt`

2. **Extracting the Hash**  
   - Found the ZIP file hash in the `zip_hash` file
   - The hash format indicates it's a ZIP2 hash that needs to be cracked

3. **Cracking the Hash**  
   - Used hash cracking tools (like `hashcat` or `john`) to crack the ZIP2 hash
   - The hash was successfully cracked to reveal the password

4. **Extracting the Flag**  
   - Used the cracked password to extract the ZIP file
   - Opened `flag.txt` to retrieve the flag

---

### **Flag**

```
deadface{Hello_my_friend}
```

---

