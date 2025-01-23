Here's the detailed write-up for the **Crack 300 - Whodah Thunkit** challenge:

---

## **Challenge Name: Crack 300 - Whodah Thunkit**

### **Description**

Time to dust off rockyou! For this challenge, you will be taking on a little application I'm considering selling to a major security firm. I'm thinking about pitching it to CrowdStrike, but Fortinet might also be interested. Test it out for yourself, and you'll see how it's going to revolutionize the cybersecurity industry! Well, at least it might if I can ever get it to work. For now, it's just an idea.

Your target system is running my app. When you connect to it, it will prompt you for a password. While it may sound like an exploit challenge, there’s another path: **follow the rules, crack the password, and the program will reveal the flag.**

The target is available at:  
**IP**: `34.123.210.162`  
**Port**: `32320`

---

### **Approach**

1. **Understanding the Application Feedback**  
   - The program provides hints based on the user-provided password:
     - **Correct Characters**: The number of characters that are part of the target hash.  
     - **Correct Positions**: The number of characters in their exact positions.  
   - This feedback mechanism allows for a systematic brute-force approach to determine the target hash.

2. **Analysis of the Target Hash**  
   - The final hash contains **32 characters**, with the following hexadecimal distribution:
     ```
     a: 6 occurrences
     b: 1 occurrence
     c: 5 occurrences
     d: 2 occurrences
     f: 2 occurrences
     0: 2 occurrences
     1: 1 occurrence
     2: 1 occurrence
     3: 1 occurrence
     4: 2 occurrences
     5: 3 occurrences
     6: 1 occurrence
     7: 3 occurrences
     8: 1 occurrence
     9: 1 occurrence
     ```
   - **Character positions** were deduced by iteratively submitting guesses to the program and analyzing its feedback. The character `e` has no occurence and can be used as padding when we want to test out for other characters.

3. **Step-by-Step Solution**  
   - Write a script to:
     - Test one character at a time across all positions.
     - Use the feedback to narrow down possible positions and counts of each character.
   - Using the feedback, the final target hash was reconstructed:
     ```
     aac56acc457c9cf0f15ad8d20347b7aa
     ```
   - Once the hash was identified, it was submitted to the program. Use [script.py](Resources/script.py) to automate some of it.

4. **Flag Retrieval**  
   - Sending the correct hash (`aac56acc457c9cf0f15ad8d20347b7aa`) resulted in the program revealing the flag.

---

### **Flag**

`poctf{uwsp_l0n3ly_4nd_f0r70rn}`

--- 
