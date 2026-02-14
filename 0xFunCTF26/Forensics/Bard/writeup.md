# Challenge Name: Bard

## Description

**Category:** Steganography / Forensics (Beginner)  
**Author:** x03e  

*The Simpsons is an old show, and Bard comes across as a bit strange.*

**Provided file:** [Resources/bard.jpg](Resources/bard.jpg) (or Bart.jpg)

**Flag format:** `0xfun{...}`

---

## Writeup

### Step 1: Steganography with StegSeek

Extract hidden content using **stegseek** with a wordlist (e.g. `rockyou.txt`):

```bash
stegseek Resources/bard.jpg rockyou.txt
# or via Docker:
# docker run --rm -v "$PWD:/ctf" rickdejager/stegseek /ctf/bard.jpg /ctf/rockyou.txt
```

Output shows a passphrase (e.g. `simple`) and an extracted file (e.g. `bits.txt` / `bard.jpg.out`).

### Step 2: Inspecting the Extracted File

```bash
cat bard.jpg.out
```

The content is a URL (e.g. `https://cybersharing.net/s/86180ebc480657ad`). Download the file from that URL; it is named `bits.txt` and contains Base64.

### Step 3: Base64 Decode

Decode the content (CyberChef or `base64 -d`). The decoded data contains PNG chunk markers (`IDAT`, `IEND`) but the **PNG signature and IHDR** are missing, so the file does not open as an image.

### Step 4: Fixing the PNG Header

A valid PNG starts with signature `89 50 4E 47 0D 0A 1A 0A` then the IHDR chunk (`00 00 00 0D 49 48 44 52` plus dimensions and CRC). Prepend the correct header to the decoded bytes.

**Quick method** (if decoded data is in `broken.png`):

```bash
printf '\x89PNG\r\n\x1a\n\x00\x00\x00\x0dIHDR' | cat - broken.png > fixed.png
```

Adjust width/height/CRC if needed to match the decoded IHDR data.

### Step 5: Open the Image

Open `fixed.png`. The image contains the flag.

---

## Resources

- **[Resources/bard.jpg](Resources/bard.jpg)** — Challenge image (stegseek source).
- Extracted `bits.txt` from the URL and decoded/fixed PNG can be kept in **Resources/** for reference.

---

## Flag

```
0xfun{secret_image_found!}
```

---
