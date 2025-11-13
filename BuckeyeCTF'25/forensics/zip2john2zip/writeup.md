# Challenge Name: zip2john2zip

## Description

Shoot, I forgot the password to our flag archive.. can you try cracking it for me? Here's the hash. Since you don't have the archive that means you can't steal all our flags!

**Files:**
- `hash.txt` - Contains the ZIP file hash
- `solve.py` - Solution script

---

## Writeup

### Step 1: Understanding the Hash Format

The hash file contains a `$pkzip2$` hash, which is the format used by John the Ripper for ZIP file password hashes. The format looks like:

```
flag.zip/flag.txt:$pkzip2$1*1*2*0*34*28*64ac0ae2*0*26*0*34*64ac*...
```

### Step 2: Cracking the Hash

We can use `john` (John the Ripper) to crack the ZIP password:

```bash
john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
```

This will attempt to crack the password using the rockyou wordlist.

### Step 3: Extracting the Password

After running john, we get the password:
```
factfinder
```

### Step 4: Reconstructing the ZIP File

Since we don't have the original ZIP file, we need to reconstruct it from the hash. The `solve.py` script:
1. Parses the `$pkzip2$` hash format
2. Extracts encrypted data, CRC32, and other metadata
3. Reconstructs candidate ZIP files with different compression methods and sizes
4. Attempts to extract the flag using the cracked password

### Step 5: Extracting the Flag

Once we have a valid ZIP file and the password, we can extract `flag.txt`:

```python
import zipfile

with zipfile.ZipFile("reconstructed_flag_c0_u52.zip") as zf:
    data = zf.read("flag.txt", pwd=b"factfinder")
    print(data.decode())
```

---

## Flag

```
bctf{not_all_hashes_are_hashed_equally}
```

---

