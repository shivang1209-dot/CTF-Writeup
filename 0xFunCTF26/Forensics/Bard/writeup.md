# Challenge Name: Bard

## Description

**Category:** Steganography / Forensics (Beginner)
**Author:** x03e

> *The Simpsons is an old show, and Bard comes across as a bit strange.*

**Provided file:** [Bart.jpg](Resources/Bart.jpg)

**Flag format:** `0xfun{...}`

---

## Writeup

### Step 1: Steganography with StegSeek

Extract hidden content using **stegseek** with a wordlist (e.g. `rockyou.txt`):

```bash
stegseek Resources/Bart.jpg rockyou.txt
```

Output shows a passphrase (e.g. `simple`) and an extracted file (`Bart.jpg.out`).

### Step 2: Inspecting the Extracted File

```bash
cat Bart.jpg.out
```

The content is a URL:

```
https://cybersharing.net/s/86180ebc480657ad
```

Download the file from that URL — it is named `bits.txt` and contains Base64-encoded data.

### Step 3: Base64 Decode

Decode the content using CyberChef or `base64 -d`:

```bash
base64 -d bits.txt > broken.png
```

The decoded data contains PNG chunk markers (`IDAT`, `IEND`) but the **PNG signature and IHDR** are missing/corrupted (the file starts with null bytes instead of the PNG magic bytes), so the file does not open as an image.

### Step 4: Fixing the PNG Header

A valid PNG starts with the signature `89 50 4E 47 0D 0A 1A 0A` followed by the IHDR chunk. The corrupted file ([download.png](Resources/download.png)) is missing this header.

Prepend the correct header to the decoded bytes:

```bash
printf '\x89PNG\r\n\x1a\n' | cat - broken.png > fixed.png
```

The repaired file is saved as [fixed.png](Resources/fixed.png).

### Step 5: Open the Image

Open `fixed.png`. The image (698 x 527, RGBA) contains the flag.

![Fixed image with flag](Resources/fixed.png)

---

## Resources

- **[Resources/Bart.jpg](Resources/Bart.jpg)** — Challenge image (stegseek source).
- **[Resources/Bart.jpg.out](Resources/Bart.jpg.out)** — Extracted URL from steghide.
- **[Resources/bits.txt](Resources/bits.txt)** — Base64-encoded data downloaded from the URL.
- **[Resources/download.png](Resources/download.png)** — Corrupted PNG (missing header).
- **[Resources/fixed.png](Resources/fixed.png)** — Repaired PNG containing the flag.

---

## Flag

```
0xfun{secret_image_found!}
```
