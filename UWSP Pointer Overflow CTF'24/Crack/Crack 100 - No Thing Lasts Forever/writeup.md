## **Challenge Name: Crack 100 - No Thing Lasts Forever**

### **Description**

Hold on... This can't be right...  

My notes say this is supposed to be a "normal" crack challenge? So... I spend twelve weeks throwing these oddball cracking challenges at you, and after all that time, we go back to wordlist and wait?  

Kind of a jerk move, if you ask me.

**File provided**: [Crack100-1.zip](Resources/Crack100-1.zip)

---

### **Approach**

1. **Understanding the Challenge**  
   - The description hints that this is a classic bruteforce zip challenge.  
   - Downloaded the zip file and began the process.

2. **Extracting the Password Hash**  
   - Used `zip2john` to extract the password hash from the provided zip file.

3. **Cracking the Password**  
   - Ran `john` with the `rockyou.txt` wordlist to crack the hash.  
   - The password was cracked in under 5 seconds, revealing: `lol12345`.

4. **Extracting the Flag**  
   - Entered the password to extract the zip contents, which included a `flag.txt` file.  
   - Opened the file to retrieve the flag.

---

### **Flag**

`poctf{uwsp_7h3_hum4n_c0nd1710n}`

--- 
