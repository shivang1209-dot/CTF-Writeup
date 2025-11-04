## **Challenge Name: stringTheory**

### **Description**

Using the artifacts from Trojan Echoes: What is the Password?, find the flag labeled flag 01.

Submit the flag as deadface{here-is-the-answer}.

**Note**: Use the artifacts from Trojan Echoes: What is the Password?

---

### **Approach**

1. **Extracting Strings**  
   - Used the `strings` command to extract all strings from the binary file:
     ```bash
     strings ../sample_01E9.exe.exe > strings.txt
     ```
   - This extracted all printable strings from the binary

2. **Searching for Flag References**  
   - Attempted to search for "flag" in the strings:
     ```bash
     cat strings.txt | grep 'flag'
     ```
   - Found references to `\flag.txt` and `__loader_flags__`, but no direct flag

3. **Manual String Analysis**  
   - Examined the strings file manually
   - Found the flag in parts scattered throughout the strings:
     ```
     01 - deadface{
     We_meet
     _again}
     ```
   - Combined these parts to form the complete flag

---

### **Flag**

```
deadface{We_meet_again}
```

---

