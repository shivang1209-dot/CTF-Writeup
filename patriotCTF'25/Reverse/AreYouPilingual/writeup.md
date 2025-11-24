## **Challenge Name: Are You Pilingual?**

### **Description**

I found this weird binary in my mom's computer. I'm not sure what it even is or why it was there. I heard it was put there from a past member of MasonCC. He did some obfuscation to make his Python code unreadable.

Reverse engineer the program and see if anything of interest lies in the output.

The flag format will be pctf{flag}

**Challenge author**: DJ Strigel

---

### **Approach**

1. **Initial Analysis**  
   - Identified the file as a Python bytecode file (`.pyc`)
   - The challenge mentions obfuscation to make Python code unreadable
   - Used PyLingual decompiler to decompile the bytecode

2. **Decompiling the Bytecode**  
   - Decompiled the Python bytecode using PyLingual
   - Recovered the source code which revealed the obfuscation mechanism

3. **Understanding the Obfuscation**  
   - The program:
     - Opens and reads a flag from `flag.txt`
     - Uses `pyfiglet` to create ASCII art from the text "MASONCC IS THE BEST CLUB EVER"
     - Embeds the flag characters into the ASCII art at specific positions
     - Splits the art string in half
     - Applies bitwise operations to each half:
       - First half: `~ord(char) ^ 5` for each character
       - Second half: `~ord(char) ^ 6` for each character
     - Concatenates the second half with the first half
     - Prints the obfuscated output

4. **Reversing the Obfuscation**  
   - Created a reversal script to:
     - Split the output back into second and first halves
     - Reverse the bitwise operations:
       - For first half: `chr(~(val ^ 5))`
       - For second half: `chr(~(val ^ 6))`
     - Reconstruct the ASCII art string
     - Extract flag characters from positions: `i, i+28, i+56, ...` where `i = len(art) % 10`

5. **Extracting the Flag**  
   - Ran the reversal script on the program output
   - Successfully extracted the flag from the obfuscated data

---

### **Flag**

```
pctf{obFusc4ti0n_i5n't_EncRypt1oN}
```

---

