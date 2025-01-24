### **Challenge Name: DF 200 - Hooper Hollar**

---

### **Description**

Memory forensics can be a challenging yet rewarding process. The challenge involves analyzing a memory dump file. Sometimes the solution is straightforward and just requires taking a step back to examine the big picture before diving into detailed analysis.

#### **File Provided**  
- [DF200-1.mem](https://pointeroverflowctf.com/static/DF200-1.mem)

---

### **Approach**

#### **Step 1: Initial Analysis**
1. Ran tools like `foremost` and `exiftool` to extract and analyze files from the memory dump.
   ```bash
   foremost -i DF200-1.mem
   exiftool DF200-1.mem
   ```
2. Found several JPEGs that seemed suspicious but couldn’t extract meaningful information from them.

#### **Step 2: Searching for Strings**
1. Decided to take a simpler approach by extracting all strings from the memory dump:
   ```bash
   strings DF200-1.mem | grep "uwsp"
   ```
2. Located the flag directly within the extracted strings:
   ```
   poctf{uwsp_l3553r_b31ng5}
   ```

#### **Reflection**
The flag was hiding in plain sight. This emphasizes the importance of starting with simpler methods before diving into deeper analysis.

---

### **Flag**

`poctf{uwsp_l3553r_b31ng5}`

--- 