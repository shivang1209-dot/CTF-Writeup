Here's a full and detailed write-up for the challenge:

---

## **Challenge Name: Reverse 200 - We Do It Live**  

---

### **Description**  

You know what I really hate? Challenges where you need to break down a function and then script your own solution. Who has time for that?? Anyway, let's do that! Luckily this should be a pretty quick one because I have got so much TV to catch up on.  

#### **File Provided**  
- [Reverse200-2](Resources/Reverse200-2)  

---

### **Approach**  

#### **Step 1: Analyzing the Decompiled Code**  

The provided decompiled function `check_input` contains several key operations:  
1. It sets `var_28` to `"TUaP^IOM"`.  
   - This looks like part of the expected transformed input.  
2. It defines `var_20`, a sequence of encoded bytes:  
   ```
   \x51\x54\x65\x0d\x5c\x11\x65\x56\x13\x0e\x5c\x0d\x65\x13\x0f\x65\x60\x10\x52\x59\x47
   ```  
3. It uses the `transform` function to modify the user-provided input.  
4. It compares the transformed input to the value in `var_28`.  

This implies the goal is to reverse the transformation logic in order to find the correct input that produces the desired transformed result.

---

#### **Step 2: Reversing the Transformation Logic**

The `transform` function applies a series of XOR and addition operations to the input string based on the encoded bytes in `var_20`.  
For each character in the input:
- The character is XORed with a corresponding byte from `var_20`.  
- The result is added to another constant, producing the final transformed value.  

---

#### **Step 3: Writing the Python Script**

To reverse the transformation and find the original input, the following [Python script](Resources/script.py) is used:  

```python
import struct

def reverse_transform(v2):
    original_chars = []
    for char in v2:
        # Apply the reverse transformation
        original_char = (ord(char) - 5) ^ 63
        original_chars.append(chr(original_char))
    return ''.join(original_chars)

def ulong_to_ascii_values(value):
    # Pack the unsigned long integer into bytes (little-endian format)
    packed_value = struct.pack('<Q', value)  # '<Q' for little-endian unsigned long long
    # Convert bytes to their ASCII integer values
    return [b for b in packed_value]

def transform_ascii_values(ascii_values):
    original_chars = []
    for value in ascii_values:
        # Subtract 5 and then apply XOR with 63
        transformed_value = (value - 5) ^ 63
        # Convert back to character and add to the list
        original_chars.append(chr(transformed_value))
    return ''.join(original_chars)

# Process the first part
v2 = "TUaP^IOM"
flag_part_1 = reverse_transform(v2)

# Process the second part
v3 = 6225401146968986705
v4 = 7281577388051686673
v5 = 5141230679910321939
ascii_values_v3 = ulong_to_ascii_values(v3)
ascii_values_v4 = ulong_to_ascii_values(v4)
ascii_values_v5 = ulong_to_ascii_values(v5)
all_ascii_values = ascii_values_v3 + ascii_values_v4 + ascii_values_v5
flag_part_2 = transform_ascii_values(all_ascii_values)

# Combine the results to get the full flag
flag = flag_part_1 + flag_part_2
print("Flag:", flag)
```

---

#### **Step 4: Executing the Script**

Running the above script outputs the original input string, which matches the criteria in `check_input`.
Though, the output it produced was - `poctf{uwsp_7h3_n3_n16h7_15_d4rk}` which was incorrect. After removing the `n3_` part we get the actual flag which also matches the quote - `The Night Is Dark`.

---

### **Flag**  

`poctf{uwsp_7h3_n16h7_15_d4rk}`  

---