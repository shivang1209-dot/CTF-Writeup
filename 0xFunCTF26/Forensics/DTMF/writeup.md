# Challenge Name: DTMF

**Category:** Misc / Audio
**Difficulty:** Easy

---

## Description

> A series of encoded messages awaits. Analyze the signals and uncover what’s hidden within.

**Provided file:** [Resources/message.wav](Resources/message.wav) — WAV (Microsoft PCM), mono, 8000 Hz, ~50 seconds.

**Flag format:** `0xfun{...}`

---

## Writeup

### Step 1: Inspect metadata

First, let’s inspect metadata:

```bash
exiftool Resources/message.wav
```

Relevant output:

```
Comment : uhmwhatisthis
```

This is the **Vigenère key** for the final step.

### Step 2: Decode DTMF tones

Listening to `message.wav`, the audio clearly consists of telephone keypad tones (Dual-Tone Multi-Frequency / DTMF).

Using an online DTMF decoder (dtmf.netlify.app), we decode the audio and obtain the following binary string:

```
010011010100100001001010011101000101101000110010011100000011011101010110010010000101010101111000011000100101010001000110011001100101100101101010010100100110111101011000001100100110110001111010010110010111101001010110011001100110010001101101001101010011000001100011011011100011000000111101
```

---

### Step 3: Binary to Base64 to text

Next, we take this binary blob into **CyberChef** and apply:

1. **From Binary**
2. **From Base64**

This produces:

```
0rmgj{Tu1m1_b4h_isc5_vntr}
```

This resembles a flag format, but it’s clearly still encrypted.

---

### Step 4: Vigenère decryption

Recall the earlier EXIF comment:

```
uhmwhatisthis
```

This is almost certainly a **Vigenère key**.

Using Vigenère **decrypt**:

* **Ciphertext:** `0rmgj{Tu1m1_b4h_isc5_vntr}`
* **Key:** `uhmwhatisthis`

We obtain:

```
0xfun{Mu1t1_t4p_plu5_dtmf}
```

---

## Resources

- **[Resources/message.wav](Resources/message.wav)** — Challenge audio file.

---

## Flag

```
0xfun{Mu1t1_t4p_plu5_dtmf}
```
