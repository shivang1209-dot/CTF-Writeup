# Challenge Name: Shell

## Description

This simple web app lets you upload images to inspect their EXIF metadata. But something feels off… maybe your uploads are being examined more closely than you realize. Can you get the server to execute a command of your choosing and expose the hidden flag.txt file?

**Note:** Only image uploads are allowed. No brute force needed — just the right approach and format.

**Challenge URL:** `http://chall.0xfun.org:39286`

**Flag Format:** `0xfun{.*}`

---

## Writeup

### Step 1: Identifying the Vulnerability

The application uses ExifTool to process uploaded images. ExifTool can execute Perl code via the `-eval` option when reading/writing metadata. This is a known RCE vector when user-controlled input is passed to ExifTool.

### Step 2: Using JPEG_RCE PoC

Using the [JPEG_RCE](https://github.com/OneSecCyber/JPEG_RCE) proof-of-concept:

1. Use the config and assets in this challenge's **Resources** folder (see [Resources/eval.config](Resources/eval.config) and [Resources/README.md](Resources/README.md)).
2. Create a JPEG and inject a command via ExifTool:

```bash
exiftool -config Resources/eval.config runme.jpg -eval='system("ls -la")'
```

Upload the modified image. The server runs ExifTool on it and executes the injected command. The output appears in the ExifTool response (e.g. directory listing).

### Step 3: Confirming RCE

Command output (e.g. `ls -la /`) shows the filesystem, including `/flag.txt` in the root directory.

### Step 4: Reading the Flag

Inject a command to read the flag:

```bash
exiftool -config Resources/eval.config runme.jpg -eval='system("cat /flag.txt")'
```

Upload the image; the response includes the flag.

---

## Resources

- **[Resources/eval.config](Resources/eval.config)** — ExifTool config for RCE (from [JPEG_RCE](https://github.com/OneSecCyber/JPEG_RCE)).
- **[Resources/README.md](Resources/README.md)** — Usage notes. Place a JPEG as `runme.jpg` in the challenge folder when running exiftool.

---

## Flag

```
0xfun{h1dd3n_p4yl04d_1n_pl41n_51gh7}
```

---
