## **Challenge Name: Cipher From Hell**

### **Description**

We've recovered an encrypted message from the eighth circle of Hell. Can you recover the hidden flag?

**Challenge author**: Neil Sharma

**Reference**: https://en.wikipedia.org/wiki/Malbolge#Crazy_operation

---

### **Approach**

1. **Initial Analysis**  
   - Provided with an encrypted file
   - The challenge name and reference suggest Malbolge's "crazy" operation
   - Malbolge is an esoteric programming language with a unique operation

2. **Understanding the Encryption**  
   - The encryption process:
     1. Converts the input flag to bytes, then to an integer
     2. Processes the integer in base 3 (trits), taking pairs from outside-in
     3. For each pair of trits (x, y), applies the Malbolge crazy operation lookup table
     4. Accumulates the results in base 9
     5. Outputs the encrypted integer as bytes

3. **Malbolge Crazy Operation**  
   - The lookup table is:
     ```
     o = (
         (6, 0, 7),
         (8, 2, 1),
         (5, 4, 3)
     )
     ```
   - For each pair (x, y) of trits, maps to value `o[x][y]` (0-8)

4. **Decryption Process**  
   - To decrypt:
     1. Read the encrypted file and convert to integer
     2. Convert the integer to base 9 digits
     3. For each base-9 digit, find the inverse mapping to get the (x, y) trit pair
     4. Reconstruct the base-3 number by placing pairs from outside-in
     5. Convert the base-3 number back to bytes

5. **Key Insight**  
   - The encryption processes pairs from outside-in (most significant and least significant positions)
   - Decryption must do the same to reconstruct the original number

6. **Implementation**  
   - Created a Python script to implement the decryption
   - Applied the inverse transformations to recover the flag

---

### **Flag**

```
pctf{a_l3ss_cr4zy_tr1tw1s3_op3r4ti0n_f37d4b}
```

---

