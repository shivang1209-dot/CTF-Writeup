# Challenge Name: Leonine Misbegotten

## Description

**Category:** Crypto
**Points:** 50

> *His attacks come fast, feel random, yet follow a careful rhythm.*

We are given an **output** file (encoded data) and a Python script **[chall.py](Resources/chall.py)** describing how the output was generated.

**Provided files:** [chall.py](Resources/chall.py), [output](Resources/output)

**Flag format:** `0xfun{...}`

---

## Writeup

### Step 1: Understanding the Encryption

Starting from the original flag, the script runs **16 rounds**. Each round:

1. Encodes the data using one random scheme from: Base16, Base32, Base64, Base85.
2. Appends a **SHA-1 checksum** of the pre-encoded data.

So each round produces: `ENCODE(previous_data) || SHA1(previous_data)`

Key observations:

- SHA-1 digest is **always 20 bytes**.
- The checksum allows us to **verify correctness** during decryption.
- Each layer can be reversed deterministically.

### Step 2: Decryption Strategy

Reverse the process layer-by-layer. For each round:

1. Split: `payload = current[:-20]`, `checksum = current[-20:]`
2. Try decoding `payload` with all four base decoders.
3. The decoder whose output has `sha1(decoded) == checksum` is the correct one.
4. Replace `current` with the decoded data and repeat.

### Step 3: Solver Script

```python
from base64 import b16decode, b32decode, b64decode, b85decode
from hashlib import sha1

DECODERS = [
    ("b16", b16decode),
    ("b32", b32decode),
    ("b64", b64decode),
    ("b85", b85decode),
]

with open("Resources/output", "rb") as f:
    current = f.read()

for r in range(16):
    payload, checksum = current[:-20], current[-20:]
    for name, dec in DECODERS:
        try:
            decoded = dec(payload)
        except Exception:
            continue
        if sha1(decoded).digest() == checksum:
            print(f"[+] Round {r+1} -> {name}")
            current = decoded
            break

print(f"\n[+] Flag: {current}")
```

### Step 4: Execution

```bash
python3 Resources/solve.py
```

Output peels all 16 layers and reveals the flag.

---

## Resources

- **[Resources/chall.py](Resources/chall.py)** — Challenge encoding script.
- **[Resources/output](Resources/output)** — Encoded output (add the file here).

---

## Flag

```
0xfun{p33l1ng_l4y3rs_l1k3_an_0n10n}
```

---

## Key Takeaway

Whenever you see random encodings followed by hashes/checksums, it usually enables **deterministic reversal** by validating each layer. Integrity checks turn guessing into certainty.
