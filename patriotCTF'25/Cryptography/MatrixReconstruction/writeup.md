## **Challenge Name: Matrix Reconstruction**

### **Description**

Someone's been messing with your secure communication channel… and they've left traces!

You've intercepted a mysterious ciphertext and a series of leaked internal states from a rogue pseudorandom generator. It seems the generator is powered by a secret 32×32 matrix A and an unknown 32-bit vector B.

Your mission: reverse-engineer the system! Use the leaked states to reconstruct the hidden matrix, uncover the XOR constant, and decrypt the message. Only then will the true flag reveal itself.

Remember: the keystream bytes come from the lowest byte of each internal state. Pay attention to the details.

**Challenge author**: DJ Strigel

---

### **Approach**

1. **Initial Analysis**  
   - Provided with:
     - A ciphertext file: `cipher.txt`
     - Leaked internal states: `keystream_leak.txt` (40 states)
     - A README explaining the challenge

2. **Understanding the System**  
   - The generator uses a linear recurrence relation over GF(2):
     - Model: `S[n+1] = A*S[n] XOR B`
     - Where A is a 32×32 matrix and B is a 32-bit vector
   - The keystream bytes come from the lowest byte (bits 0-7) of each internal state

3. **Recovering Matrix A and Vector B**  
   - Given consecutive state pairs `(S[i], S[i+1])`, we have: `S[i+1] = A*S[i] XOR B`
   - Over GF(2), XOR is addition, so: `S[i+1] = A*S[i] + B (mod 2)`
   - For each output bit position `j`:
     ```
     S[i+1][j] = sum_k(A[j,k] * S[i][k]) + B[j]
     ```
   - This is a linear system! Can solve for each row of A and corresponding bit of B independently

4. **Solving the Linear System**  
   - Set up 32 linear systems (one for each bit position)
   - Each system has 32 unknowns (one row of matrix A) plus 1 unknown (one bit of vector B)
   - Used Gaussian elimination over GF(2) to solve each system
   - With 40 leaked states, we have enough equations to solve the system

5. **Generating the Keystream**  
   - Starting from the first leaked state, applied the recurrence: `S[n+1] = A*S[n] XOR B`
   - Extracted the lowest byte from each state to get the keystream

6. **Decrypting the Ciphertext**  
   - XORed the ciphertext with the generated keystream
   - Recovered the plaintext flag

---

### **Flag**

```
pctf{mAtr1x_r3construct?on_!s_fu4n}
```

---

