## **Challenge Name: ghostInTheShell**

### **Description**

We went to one of the meetup spots DEADFACE often uses, and found an old floppy disk lying next to one of the older public computers… given the theme, we think spookyboi may have left it there intentionally. We managed to scrape this program off of it, and expect it will give us info on the next meetup location. I can't seem to get anything useful out of it, and to be honest, the whole program gives me the ick!

**File provided**: [C64](C64)

---

### **Approach**

1. **Initial Analysis**  
   - The file appears to be a Commodore 64 (C64) program based on the filename
   - Attempted to analyze or execute the program to understand its behavior

2. **Finding the Password**  
   - Discovered that the program requires a password to proceed
   - Found Password 1: `I_1NVIT3_Y0U_1N`

3. **Finding the Answer**  
   - After entering the password, the program asked a question
   - Found Answer 2: `kali`

4. **Finding the Flag Question**  
   - The program asked: "what is the flag?"
   - Found the source code logic:
     ```c
     strcpy(arg1, "wh"); strcat(arg1, "at "); strcat(arg1, "is t"); strcat(arg1, "he f"); return strcat(arg1, "lag");
     ```
   - This constructs the string "what is the flag"

5. **Getting the Flag**  
   - Answered the question: "what is the flag?"
   - The program responded:
     ```
     I AM ZODD. I WILL ANSWER ONE QUESTION, MORTAL... 
     
     what is the flag?
     
     VERY WELL... 
     
     deadface{C0D3D_1N_BL00D_THE_GH05T_4W4K3N5}
     ```

---

### **Flag**

```
deadface{C0D3D_1N_BL00D_THE_GH05T_4W4K3N5}
```

---

