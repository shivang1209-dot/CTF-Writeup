## **Challenge Name: Reverse 100 - Understanding Nonsense**  

---

### **Description**  

Oh, boy... Only Wave 2 and I'm already exhausted. Whatever the issue, I just can't be bothered to finish putting this challenge together. Here, this what I have so far. Started working on the decode function and gave up. You go ahead and do the rest and the flag is yours! And if Prof. Johnson asks, tell him this was really well done or I'll get in trouble.  

#### **File Provided**  
- [Reverse100-3](Resources/Reverse100-3)  
- [Reverse100-3.c](Resources/Reverse100-3.c)  

---

### **Approach**  

1. **Analyze the Files**  
   - After downloading the provided files, we notice that the source code (`Reverse100-3.c`) contains an encoding and decoding implementation that is incomplete.  
   - The compiled executable (`Reverse100-3`) requires the encoded flag to be correctly decoded.  

2. **Fix the Source Code**  
   - The decoding function is incomplete, so the following changes are made to `Reverse100-3.c`:  
     - **Add Iteration for Reversing:**  
       To properly decode the flag, the reversal process must be repeated 10 times. Add a loop to iterate the `print_flag_hex` function 10 times.  
     - **Fix Length Calculation:**  
       Update the length calculation to determine the correct number of elements in the array:  
       ```c  
       int length = sizeof(encoded_flag) / sizeof(encoded_flag[0]);  
       ```  
     - **Seed Value:**  
       The decryption requires a specific seed value of `88974713` to match the logic in the reverse function. Pass this as a parameter where needed.

3. **Compile and Execute**  
   - Save the changes in a new file, such as `decode.c`, and compile it:  
     ```bash  
     gcc decode.c -o decode  
     ```  
   - Run the executable, which prints all intermediate flags for each reversal step.  

4. **Decode the Final Flag**  
   - The decoded flag after step 10 is:  
     ```  
     706f6374667b757773705f627233763137795f31355f3768335f353075317d  
     ```  
   - This appears to be in hexadecimal format. Convert it to plain text using a tool like CyberChef or Python:  
     ```python  
     bytes.fromhex("706f6374667b757773705f627233763137795f31355f3768335f353075317d").decode()  
     ```  

---

### **Flag**  

`poctf{uwsp_br3v17y_15_7h3_50u1}`  

---  