# Challenge Name: DTMF

## Description

**Category:** Misc / Audio
**Difficulty:** Easy

> A series of encoded messages awaits. Analyze the signals and uncover what's hidden within.

**Provided file:** [message.wav](Resources/message.wav) — WAV (Microsoft PCM), mono, 8000 Hz, ~50 seconds.

**Flag format:** `0xfun{...}`

---

## Writeup

### Step 1: Inspect Metadata

First, inspect metadata:

```bash
exiftool Resources/message.wav
```

Relevant output:

```
Comment : uhmwhatisthis
```

This is the **Vigenere key** for the final step.

### Step 2: Decode DTMF Tones

Listening to `message.wav`, the audio clearly consists of telephone keypad tones (Dual-Tone Multi-Frequency / DTMF).

Using an online DTMF decoder ([dtmf.netlify.app](https://dtmf.netlify.app)), we decode the audio and obtain the following binary string:

```
010011010100100001001010011101000101101000110010011100000011011101010110010010000101010101111000011000100101010001000110011001100101100001101010010100100110111101011000001100100110110001111010010110010111101001010110011001100110010001101101001101010011000001100011011011100011000000111101
```

### Step 3: Binary to Base64 to Text

Take this binary blob into **CyberChef** and apply:

1. **From Binary**
2. **From Base64**

This produces:

```
0rmgj{Tu1m1_b4h_isc5_vntr}
```

This resembles a flag format but is clearly still encrypted.

### Step 4: Vigenere Decryption

Recall the earlier EXIF comment: `uhmwhatisthis` — this is the **Vigenere key**.

Using Vigenere **decrypt**:

- **Ciphertext:** `0rmgj{Tu1m1_b4h_isc5_vntr}`
- **Key:** `uhmwhatisthis`

We obtain the flag.

---

## Resources

- **[Resources/message.wav](Resources/message.wav)** — Challenge audio file (add the challenge file here).

---

## Flag

```
0xfun{Mu1t1_t4p_plu5_dtmf}
```
