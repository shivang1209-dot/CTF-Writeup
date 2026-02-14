# Challenge Name: Tesla

## Description

Flipper Zero, often referred to as a hacking device, is designed to capture frequencies and execute commands. It's considered a risky tool to have, as it is illegal in some countries.

---

## Writeup

### Step 1: Inspecting the Binary

The challenge provides **Tesla.sub** (Flipper SubGhz / binary data). Convert the binary to ASCII (e.g. in CyberChef). The result is **batch-style** script with variable substitution: a string variable (e.g. `IlÃc`) and many `%IlÃc:~offset,1%` segments that select single characters. There is also a PowerShell/Base64 fragment.

### Step 2: Extracting the Message with a Script

Run the provided **[Resources/solve.py](Resources/solve.py)** (or equivalent) to interpret the batch logic and extract the character sequence. Run from the challenge folder with `Resources/decoded_payload.txt` present, or run from `Resources/` so the script finds `decoded_payload.txt` there. The script output may look like:

```
... i could be something to this 5958051a1b170013520746265a0e51435b36165752470b7f03591d1b364b501608616e ive been encrypted many in ways ...
```

The hex string is the **ciphertext**. Direct hex decoding does not give plaintext.

### Step 3: Known Plaintext XOR

We know the flag starts with `0xfun{` → hex `307866756e7b`.

XOR the first 6 bytes of the ciphertext with this known plaintext:

- `307866756e7b` ⊕ `5958051a1b17` → yields something like `i coul` in ASCII, matching the phrase "i could be something to this".

So the **XOR key** is the repeating phrase (e.g. "i could be something to this"). Extend the key to the ciphertext length by repetition.

### Step 4: Decrypting

XOR the full ciphertext with the repeated key:

```
6920636f756c6420626520736f6d657468696e6720746f207468697320...  (key stream)
^
5958051a1b170013520746265a0e51435b36165752470b7f03591d1b364b501608616e  (ciphertext)
```

The result is the flag.

---

## Resources

- **[Resources/Tesla.sub](Resources/Tesla.sub)** — Challenge file (Flipper SubGhz).
- **[Resources/solve.py](Resources/solve.py)** — Extracts message and/or performs XOR. Expects `decoded_payload.txt` in the same directory (or run from `Resources/`).
- **[Resources/decoded_payload.txt](Resources/decoded_payload.txt)** — Optional intermediate output from decoding the batch script.

---

## Flag

```
0xfun{d30bfU5c473_x0r3d_w1th_k3y}
```

---
