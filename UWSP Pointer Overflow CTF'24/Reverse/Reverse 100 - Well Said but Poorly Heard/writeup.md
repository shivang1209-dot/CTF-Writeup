## **Challenge Name: Reverse 100 - Well Said but Poorly Heard**  

---

### **Description**  

So there I was, knee-deep in wet newspaper, a puppy under each arm, and a lion hovering over me on the back of a giant dragonfly. Only one thing separating me from certain death at the hands of the President of Murder was the Sphinx and its riddle.  

"Ask your riddle, Peptopotamus!" The puppy under my right arm commanded. Its stone face moved, kicking off ancient dust, turning its glowing eyes to us. It spoke its riddle.  

"True to false and false to true  
What you did before, now undone,  
And when you're wrong, reverse your sight.  
What am I?"  

The lion laughed, but he did not know what I knew. He did not know that I created the attached program when I was only 18 months old, and not only did I know the answer to his riddle - I was its master. Now, I give the program to you, so you too can be prepared if you find yourself in a similar situation.  

#### **File Provided**  
- [Reverse100-1](Resources/Reverse100-1)  

---

### **Approach**  

1. **Download and Analyze the File**  
   - After downloading, the `file` command reveals it is an **ELF executable**.  
   - Grant execution permissions with:  
     ```bash  
     chmod +x Reverse100-1  
     ```  
   - Running the file (`./Reverse100-1`) outputs an encoded flag.  

2. **Hexdump Investigation**  
   - Using `xxd` to view the hexdump, parts of the flag (`poctf{uw...`) are visible amidst encoded data.  

3. **Static Analysis**  
   - Opening the ELF in **Decompiler Explorer** and **Binary Ninja**, the encoded logic becomes clear, revealing the complete flag.  

    ```bash
    00401171        int64_t var_38
    00401171        __builtin_strcpy(dest: &var_38, src: "poctf{uwsp_1n_w1n3_7h3r3_15_7ru7h}")
    004011a3        obfuscate(&var_38)
    004011be        printf(format: "Encoded flag: %s\n", &var_38)
    004011c9        return 0
    ```

---

### **Flag**  

`poctf{uwsp_1n_w1n3_7h3r3_15_7ru7h}`  

---  