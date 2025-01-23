## **Challenge Name: Crypto 400 - A Question of Perspective**

### **Description**

You have been hired by a tech company to assess the security of thier quantum communication system. The system uses the BB84 protocol for key distribution. During your assessment, you've intercepted some qubits and their bases during an exchange between Alice and Bob, but some of Bob's measurements are incorrect at every third qubit due to an eavesdropping scenario. Since this is a new system still in testing, the seed space is restricted to positive integers between 1 and 100.

Qubits = [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1]

Bases = ['R', 'R', 'D', 'R', 'R', 'R', 'R', 'R', 'D', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'D', 'R', 'D', 'D', 'R', 'R', 'D', 'D', 'D', 'R', 'R', 'D', 'R', 'R', 'D', 'R', 'D', 'D', 'D', 'R', 'D', 'R', 'D', 'R', 'D', 'D', 'R', 'R', 'R', 'R', 'D', 'R', 'R', 'R', 'D', 'D', 'D', 'D', 'R', 'D', 'D', 'R', 'D', 'R', 'R', 'R', 'R', 'D', 'D', 'D', 'R', 'D', 'R', 'R', 'R', 'D', 'D', 'D', 'R', 'R', 'D', 'R', 'D', 'D']

Measurements = [0, 1, ?, 1, 0, ?, 1, 1, ?, 0, 1, ?, 0, 1, ?, 0, 1, ?, 1, 0, ?, 1, 0, ?, 0, 1, ?, 0, 1, ?, 1, 0, ?, 0, 0, ?, 0, 1, ?, 0, 1, ?, 1, 1, ?, 1, 0, ?, 1, 0, ?, 0, 1, ?, 0, 1, ?, 0, 1, ?, 1, 0, ?, 1, 0, ?, 0, 1, ?, 0, 0, ?, 0, 1, ?, 1, 1, ?, 1, 1]

Encrypted Message = [0x23, 0x59, 0x86, 0x1e, 0x60, 0xcf, 0xdc, 0x4e, 0x6a, 0x0b, 0x0c, 0x50, 0xd4, 0x5a, 0x71, 0x87, 0xdb, 0x0c, 0x46, 0x1d, 0x63, 0x44, 0xba, 0x5e, 0x37, 0xd3, 0x9a, 0x4b, 0x77, 0x4b, 0x3d, 0x4b]

---

### **Approach**

#### **Step 1: Identify Known and Unknown Bits**  
We first align the known measurements with the qubits while retaining the `?` values. The `?` values correspond to every third qubit where Bob could not measure correctly.  

- Common values (with `?` retained):  
  `01?0?11?1?0?0?10?0?01?0?1????11?10?0??0?01?0?0??0?01?11?1`  

- Every third qubit (sent by Alice):  
  `[0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0]`  

#### **Step 2: Brute Force `?` Values**  
Each `?` can either:  
1. Match Alice's corresponding third qubit value.  
2. Be discarded due to different bases.  

We brute-force all possible permutations of the 26 `?` values. Each iteration substitutes the `?` with a valid or invalid value.  

For example:  
- All `?` discarded:  
  `0101110010001011110000100001111`  
- First `?` retained as Alice's value:  
  `01001110010001011110000100001111`  

#### **Step 3: Key Length Adjustment**  
The total key length (confirmed + uncertain bits) is at most 31 + 26 = 57 bits. Since the encrypted message is 256 bits, the key must repeat to match this length.  

Factors of 256 suggest a 32-bit repeated pattern, which aligns with the key length of 57 bits.  

#### **Step 4: Known Plaintext Attack**  
The encrypted ciphertext starts with the known string `poctf{uwsp_`. Converting this plaintext to binary and XORing it with the first 11 chunks of the ciphertext reveals the key bits. After 80 bits, the key begins repeating, confirming its wrapped structure.  

#### **Step 5: Final XOR**  
Once the key is extended and aligned with the ciphertext, XOR the two to retrieve the plaintext.  

---  

This process systematically reveals the plaintext while demonstrating the weaknesses in the system’s implementation of the BB84 protocol.
---

### **Flag**

`poctf{uwsp_f10w3r5_f0r_41g3rn0n}`

---