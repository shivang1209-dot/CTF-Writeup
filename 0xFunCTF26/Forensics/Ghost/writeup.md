# Challenge Name: Ghost

## Description

The interception of a transmission has occurred, with only a network capture remaining. Recover the flag before the trail goes cold.

---

## Writeup

### Step 1: Viewing the Image

Open the provided image [Resources/wallpaper.png](Resources/wallpaper.png). In the image or its metadata you may see a string that looks like part of a password or hint, e.g.:

```
1n73rc3p7_c0nf1rm3d
```

### Step 2: Checking for Trailer Data

```bash
exiftool Resources/wallpaper.png
# Warning: [minor] Trailer data after PNG IEND chunk
```

So there is **data after the PNG IEND** chunk.

### Step 3: Locating the Hidden Archive

```bash
binwalk Resources/wallpaper.png
# 0x0      PNG image
# 61208    0xEF18  7-zip archive data, version 0.4
```

Extract the 7z data:

```bash
dd if=Resources/wallpaper.png of=Resources/hidden.7z bs=1 skip=61208 status=progress
```

### Step 4: Cracking the Archive Password

The archive is password-protected. Try the string found in the image (e.g. `1n73rc3p7_c0nf1rm3d`):

```bash
7z x Resources/hidden.7z -p1n73rc3p7_c0nf1rm3d -oResources/
```

If that fails, try other variants (e.g. `-pnothing` or the exact string from the image).

### Step 5: Reading the Flag

After extraction (e.g. to `Resources/`), **Resources/fishwithwater/nothing.txt** contains the flag. Read it:

```bash
cat Resources/fishwithwater/nothing.txt
```

---

## Resources

- **[Resources/wallpaper.png](Resources/wallpaper.png)** — Challenge image (trailer contains 7z).
- **[Resources/hidden.7z](Resources/hidden.7z)** — Extracted archive (password from image).
- **[Resources/fishwithwater/nothing.txt](Resources/fishwithwater/nothing.txt)** — Extracted file containing the flag.

---

## Flag

```
0xfun{l4y3r_pr0t3c710n_k3y}
```

---
