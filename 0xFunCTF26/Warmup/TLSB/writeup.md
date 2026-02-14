# Challenge Name: TLSB

## Description

You might know about Least Significant Bit (LSB) steganography, but have you ever heard of Third Least Significant Bit (TLSB) steganography? (Probably not, I invented it for this challenge).

**Flag Format:** `0xfun{.*}`

---

## Writeup

### Step 1: Understanding TLSB

**TLSB** = Third Least Significant Bit = **bit 2** (0-indexed) of each byte.

The file is a 16×16 24-bit BMP. Pixel data starts at offset 54.

### Step 2: Extracting the Hidden Data

1. **Extract bit 2** from every byte of the pixel data: `(byte >> 2) & 1`.
2. **Pack bits into bytes** using **MSB first** (the first bit of each group of 8 becomes the high bit of the byte). LSB-first packing yields garbage; MSB first yields readable text.

### Step 3: Decoding the Message

The extracted message is:

`Hope you had fun :). The Flag is: \`MHhmdW57VGg0dDVfbjB0X0wzNDV0X1MxZ24xZjFjNG50X2IxdF81dDNnfQ==\``

### Step 4: Base64 Decode

Base64-decode the string between the backticks to get the flag.

---

## Flag

```
0xfun{Th4t5_n0t_L345t_S1gn1f1c4nt_b1t_5t3g}
```

---
