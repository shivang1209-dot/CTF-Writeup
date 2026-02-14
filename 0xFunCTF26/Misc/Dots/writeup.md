# Challenge Name: Dots

## Description

Unusual dots scatter across the page, sparking a whirlwind of ideas—perhaps a pattern to decode, a secret message to uncover, or a design to bring to life.

---

## Writeup

### Step 1: Inspecting the File

We are given an audio file: `dots.wav`.

```bash
file dots.wav
```

Output: `RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 44100 Hz`

Given the name *Dots* and the audio format, **SSTV (Slow Scan Television)** is a likely encoding.

### Step 2: Converting Sample Rate for QSSTV

QSSTV often works more reliably with 48 kHz. Resample with `sox`:

```bash
sox dots.wav -r 48000 dots_fixed.wav
```

### Step 3: Decoding SSTV

Load the converted file in **QSSTV** and decode to obtain an image (e.g. save as `decoded-image.png`).

```bash
file decoded-image.png
# PNG image data, 320 x 256, 8-bit/color RGB
```

The image shows a grid of black dots on white—not the final flag but encoded data.

### Step 4: Identifying the Barcode

- Uniform dot grid, no QR finder patterns, no DataMatrix borders → consistent with **DotCode**, a 2D matrix barcode.

### Step 5: Decoding DotCode

Upload the decoded image to a DotCode-capable reader, e.g. [Dynamsoft Barcode Reader](https://demo.dynamsoft.com/barcode-reader/). Decode to get the embedded text (the flag).

---

## Summary

Decoding chain:

```
WAV Audio → SSTV (QSSTV) → PNG Image → DotCode Barcode → Flag
```

---

## Resources

- **Tools:** sox, QSSTV, Dynamsoft Barcode Reader (or similar).
- **Decoded image:** Save the SSTV output as e.g. [Resources/decoded-image.png](Resources/decoded-image.png) for reference.

---

## Flag

```
0xfun{d07_c0d3_k1nd4_d1ff3r3n7_45_175_4_w31rd_qr_7yp3}
```

---
