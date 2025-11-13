# Challenge Name: 1985

## Description

This is uuencoded data — a common format used in the 1980s and 1990s to send binary files over email, before attachments were standardized.

**Files:**
- `flagprinter.uue` - UUencoded file
- `FLGPRNTR.COM` - Decoded binary file

---

## Writeup

### Step 1: Decoding UUencoded Data

The challenge provides a UUencoded file. UUencoding was commonly used in the 1980s and 1990s to send binary files over email.

```bash
uudecode flagprinter.uue
```

This gives us `FLGPRNTR.COM`, a binary file.

### Step 2: Analyzing the Binary

Let's examine the file:

```bash
file FLGPRNTR.COM
strings FLGPRNTR.COM
```

The file appears to be encoded or obfuscated. The strings output doesn't reveal readable text, suggesting the data is XOR-encrypted.

### Step 3: XOR Decryption

Since the file appears to be XOR-encrypted, we can try XORing with different keys. The solution uses XOR with key `0x2A`:

```python
data = open("FLGPRNTR.COM","rb").read()
dec = bytes(b ^ 0x2A for b in data)
print(dec.decode("latin1",errors="ignore"))
```

This reveals the flag.

---

## Flag

```
bctf{D1d_y0u_Us3_An_3mul4t0r_Or_d3c0mp1lEr}
```

---

