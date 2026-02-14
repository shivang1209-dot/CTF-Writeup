# Challenge Name: Dots

## Description

**Category:** Misc

> Unusual dots scatter across the page, sparking a whirlwind of ideas — perhaps a pattern to decode, a secret message to uncover, or a design to bring to life.

**Provided file:** [dots.wav](Resources/dots.wav)

**Flag format:** `0xfun{...}`

---

## Writeup

### Step 1: Inspecting the File

We are given an audio file: [dots.wav](Resources/dots.wav).

```bash
file Resources/dots.wav
# RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 44100 Hz
```

Given the name *Dots* and the audio format, **SSTV (Slow Scan Television)** is a likely encoding.

### Step 2: Converting Sample Rate for QSSTV

QSSTV often works more reliably with 48 kHz. Resample with `sox`:

```bash
sox Resources/dots.wav -r 48000 Resources/dots_fixed.wav
```

### Step 3: Decoding SSTV

Load the converted file ([dots_fixed.wav](Resources/dots_fixed.wav)) in **QSSTV** and decode to obtain an image.

The image shows a grid of black dots on white — not the final flag but encoded data.

### Step 4: Identifying the Barcode

The uniform dot grid (no QR finder patterns, no DataMatrix borders) is consistent with **DotCode**, a 2D matrix barcode.

### Step 5: Decoding DotCode

Upload the decoded image ([decoded-image.png](Resources/decoded-image.png)) to a DotCode-capable reader, e.g. [Dynamsoft Barcode Reader](https://demo.dynamsoft.com/barcode-reader/). Decode to get the embedded text (the flag).

---

## Summary

```
WAV Audio → SSTV (QSSTV) → PNG Image → DotCode Barcode → Flag
```

---

## Resources

- **[Resources/dots.wav](Resources/dots.wav)** — Original challenge audio file.
- **[Resources/dots_fixed.wav](Resources/dots_fixed.wav)** — Resampled audio (48 kHz) for QSSTV.
- **[Resources/decoded-image.png](Resources/decoded-image.png)** — SSTV-decoded PNG containing the DotCode barcode.

---

## Flag

```
0xfun{d07_c0d3_k1nd4_d1ff3r3n7_45_175_4_w31rd_qr_7yp3}
```
