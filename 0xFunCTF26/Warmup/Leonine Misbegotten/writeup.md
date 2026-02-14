# Challenge Name: Leonine Misbegotten

## Description

**Category:** Crypto (50 pts)

We are given an **output** file (encoded data) and a Python script **[Resources/chall.py](Resources/chall.py)** describing how the output was generated.

```python
from base64 import b16encode, b32encode, b64encode, b85encode
from hashlib import sha1
from random import choice
from secret import flag

SCHEMES = [b16encode, b32encode, b64encode, b85encode]

ROUNDS = 16
current = flag.encode()
for _ in range(ROUNDS):
    checksum = sha1(current).digest() # this is to help you check the integrity of your decryption
    current = choice(SCHEMES)(current) 
    current += checksum

with open("output", "wb") as f:
    f.write(current)
```

The challenge description hints:

> *His attacks come fast, feel random, yet follow a careful rhythm.*

This suggests randomness with structure — exactly what the code implements.

**Flag format:** `0xfun{...}`

---

## Writeup

### Step 1: Understanding the encryption

Starting from the original flag:

1. The flag is encoded using **one random scheme** from:

   * Base16
   * Base32
   * Base64
   * Base85

2. A SHA-1 checksum of the *pre-encoded* data is appended.

So each round produces:

```
ENCODE(previous_data) || SHA1(previous_data)
```

This process repeats **16 times**.

Important observations:

* SHA-1 digest length is **always 20 bytes**.
* Although the encoding choice is random, the checksum allows us to **verify correctness** during decryption.
* Therefore, each layer can be reversed deterministically.

### Step 2: Decryption strategy

We reverse the process layer-by-layer.

For each round:

1. Split the data into:

   * `payload = current[:-20]`
   * `checksum = current[-20:]`

2. Try decoding `payload` using **all four base decoders**.

3. For each decoded candidate:

   * Compute `sha1(decoded)`
   * Compare with the extracted checksum.

4. The decoder that matches is guaranteed to be the correct one.

5. Replace `current` with the decoded data and repeat.

Because the checksum uniquely validates each step, only **one decoder works per round**.

This effectively “peels” the encodings one at a time — like an onion.

---

## Solver Script

```python
from base64 import b16decode, b32decode, b64decode, b85decode
from hashlib import sha1

DECODERS = [
    ("b16", b16decode),
    ("b32", b32decode),
    ("b64", b64decode),
    ("b85", b85decode),
]

ROUNDS = 16

with open("Resources/output", "rb") as f:
    current = f.read()

for r in range(ROUNDS):
    print(f"[+] Round {r+1}")

    payload = current[:-20]
    checksum = current[-20:]

    for name, dec in DECODERS:
        try:
            decoded = dec(payload)
        except Exception:
            continue

        if sha1(decoded).digest() == checksum:
            print(f"    -> matched {name}")
            current = decoded
            break
    else:
        raise Exception("No valid decoder found!")

print("\n[+] Final result:")
print(current)
```

Run: `python3 Resources/solve.py` (or from the folder containing `output`).

### Step 4: Execution

```
python3 Resources/solve.py
```

Produces:

```
[+] Round 1  -> matched b32
[+] Round 2  -> matched b16
[+] Round 3  -> matched b85
[+] Round 4  -> matched b32
[+] Round 5  -> matched b85
[+] Round 6  -> matched b64
[+] Round 7  -> matched b32
[+] Round 8  -> matched b32
[+] Round 9  -> matched b16
[+] Round 10 -> matched b16
[+] Round 11 -> matched b85
[+] Round 12 -> matched b64
[+] Round 13 -> matched b85
[+] Round 14 -> matched b64
[+] Round 15 -> matched b16
[+] Round 16 -> matched b16
```

Final output:

```
b'0xfun{p33l1ng_l4y3rs_l1k3_an_0n10n}'
```

---

## Resources

- **[Resources/chall.py](Resources/chall.py)** — Challenge encoding script.
- **[Resources/output](Resources/output)** — Encoded output.
- **[Resources/solve.py](Resources/solve.py)** — Decryption script.

---

## Flag

```
0xfun{p33l1ng_l4y3rs_l1k3_an_0n10n}
```

---

## Key takeaway

Whenever you see:

* Random encodings or transformations
* Followed by hashes or checksums

…it usually enables **deterministic reversal** by validating each layer.

This challenge demonstrates a classic crypto CTF pattern:

> **Integrity checks turn guessing into certainty.**

---

