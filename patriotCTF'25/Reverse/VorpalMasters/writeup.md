## **Challenge Name: Vorpal Masters**

### **Description**

I'm excited to announce the launch of my brand new video game Vorpal Masters. In light of recent pirating attacks, I've implemented a copy protection by requiring a license key when you launch the game. Before I publish the game to Steam, I just want to have someone test it to make sure it's as uncrackable as I think it is.

The flag is the license key, put into the format CACI{Key}

**Challenge author**: Matthew Johnson (CACI)

---

### **Approach**

1. **Initial Analysis**  
   - Ran the binary and found it asks for a license key
   - The format is `xxxx-xxxx-xxxx` (4 characters, integer, 10 characters)
   - Example: `1234-1234-1234`

2. **Reverse Engineering the Validation**  
   - Analyzed the binary using a disassembler or decompiler
   - Found the validation logic that checks the license key

3. **Understanding the Validation Checks**  
   - **First 4 characters check:**
     - The program uses `scanf` with format `"%4s-%d-%10s"`
     - Memory layout check: `var_11 == 'C'`, `var_10 == 'A'`, `var_f == 'C'`, `var_e == 'I'`
     - So the first part must be **"CACI"**
   
   - **Integer range check:**
     - The integer must be between `-5000` (0xffffec78) and `10000` (0x2710)
   
   - **Complex calculation check:**
     - Checks: `(n + 22) % 1738 == ((n * 2) % 2000) * 6 + 9`
     - This is a compiler-optimized modulo operation
   
   - **Last 10 characters check:**
     - Must be **"PatriotCTF"**

4. **Finding the Valid Integer**  
   - Brute-forced integers in the range [-5000, 10000]
   - Found that `2025` satisfies the modulo equation:
     - `(2025 + 22) % 1738 = 2047 % 1738 = 309`
     - `((2025 * 2) % 2000) * 6 + 9 = 50 * 6 + 9 = 309` ✓

5. **Constructing the License Key**  
   - Format: `CACI-2025-PatriotCTF`
   - Verified this key passes all validation checks

---

### **Flag**

```
CACI{CACI-2025-PatriotCTF}
```

---

