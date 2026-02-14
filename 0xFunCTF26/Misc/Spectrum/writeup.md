# Challenge Name: Spectrum

## Description

It appears too simple to be a real challenge. Increasing the difficulty is essential.

---

## Writeup

### Step 1: Inspecting the Audio

We are given `audio.wav` (e.g. Microsoft PCM, 16 bit, mono 44100 Hz). Viewing the **spectrogram** in a tool (e.g. Audacity, Sonic Visualiser) shows a first message: `0xfun{50_345y_1_b3l13v3}`. That is a decoy; the real flag is hidden elsewhere.

### Step 2: Extracting Hidden Data from the WAV

Use **Deepsound** (or similar) to extract a file hidden in the WAV. The extracted file might be named e.g. `si.txt` and contain a URL such as:

```
https://cybersharing.net/s/33864416ca80f2c5
```

### Step 3: Downloading the Next File

Visit the URL and download the file (e.g. `seccat.png`).

### Step 4: Fixing the PNG

The downloaded file may be a corrupted PNG (e.g. `pngcheck` reports "first chunk must be IHDR"). Use the provided [Resources/fix.py](Resources/fix.py) to repair the file (place `seccat.png` in the same folder or adjust paths in the script):

```bash
python3 Resources/fix.py
# Produces e.g. seccat_fixed.png
```

### Step 5: Reading the Flag

Open the fixed PNG (e.g. in an image viewer or with `strings`). The image or embedded text contains the real flag.

---

## Resources

- **audio.wav** — Challenge file (in the challenge folder).
- **[Resources/fix.py](Resources/fix.py)** — Script to fix the extracted PNG.
- **[Resources/si.txt](Resources/si.txt)** — Extracted file from Deepsound (created during solve).

---

## Flag

```
0xfun{c47s_4r3_n07_s33_7hr0ugh_bu7_7h3y_4r3_cur10us}
```

---
