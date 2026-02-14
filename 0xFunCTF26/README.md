# 0xFUN CTF 2026 Writeups

Welcome to my repository for the **0xFUN CTF 2026** writeups!  
This CTF was organized by **Bunkyowerstens** and held online (12–14 Feb 2026). Event details: [CTFtime – 0xFUN CTF 2026](https://ctftime.org/event/3081).

## Repo Structure

This repository contains writeups for **challenges** I attempted during the competition. Each challenge has its own folder by category. Inside each folder you will find:
- A **writeup** in Markdown explaining how the challenge was solved.
- **Resources** (images, scripts, and other files) used during the solve, where applicable.
- **Flag(s)** or answers for the challenge.

## Categories

### Warmup (8 challenges)
- **Shell** — ExifTool RCE via malicious image upload
- **TLSB** — Third Least Significant Bit steganography (BMP)
- **Perceptions** — Multi-path blog and secret directory
- **Music** — Bucking Music Cipher (phonetic/notation)
- **Templates** — Server-Side Template Injection (SSTI), Jinja2 RCE
- **UART** — Sigrok UART decode from logic capture
- **Leonine Misbegotten** — Layered Base16/32/64/85 + SHA-1 peel
- **Guess The Seed** — Time-seeded rand() prediction

### Crypto (3 challenges)
- **MeOwl ECC** — Anomalous curve, Smart’s attack, AES+DES decrypt
- **TheSlotWhisperer** — LCG prediction from partial output
- **Back in the 90's** — Cipher decode (see challenge folder)

### Forensics (7 challenges)
- **Bard** — StegSeek on JPEG, Base64 decode, fix PNG header
- **DTMF** — DTMF decode, binary→Base64, Vigenère (key in EXIF)
- **Tesla** — Flipper SubGhz batch script, XOR known-plaintext
- **PrintedParts** — G-code 3D print preview, flag in toolpath
- **Ghost** — PNG trailer, 7z extraction, password from image
- **kd** — MiniDuMP crash dump, strings
- **Nothing Expected** — Excalidraw JSON in PNG, extract and view

### Misc (6 challenges)
- **Counting** — Discord counting channel collaboration
- **Dots** — WAV → SSTV → DotCode barcode
- **Emoji** — Emoji steganography
- **Insanity 1** — Discord API, query user roles for flag
- **MazeRunna** — Roblox maze game
- **Spectrum** — Spectrogram decoy + Deepsound + PNG fix
- **Trapped** — SSH, ACLs, GECOS credential, user pivot

### OSINT (6 challenges)
- **Frog Finder 2** — X profile, geoOSINT, reviews for flag
- **MultiVerse** — Reddit + Base58, Spotify + Base64, combine flag parts
- **Lookup 0xfun** — DNS TXT record for ctf.0xfun.org
- **Malware Analysis 1** — MSI filename from report (3aw.msi)
- **Malware Analysis 2** — Malicious domain (bestiamos.com)
- **Malware Analysis 3** — Original MSI filename from hash lookup

### Web (3 challenges)
- **Tony Toolkit** — SQLi, hash crack, cookie userID tampering (IDOR)
- **Jinja** — SSTI in email field, Jinja2 RCE
- **Skyport Ops** — GraphQL, JWT alg confusion, path traversal upload, /leak

## Folder Structure

```
0xFunCTF26/
├── Warmup/
│   ├── Shell/
│   ├── TLSB/
│   ├── Perceptions/
│   ├── Music/
│   ├── Templates/
│   ├── UART/
│   ├── Leonine Misbegotten/
│   └── Guess The Seed/
├── Crypto/
│   ├── MeOwlECC/
│   ├── TheSlotWhisperer/
│   └── Back in the 90's/
├── Forensics/
│   ├── Tesla/
│   ├── PrintedParts/
│   ├── Bard/
│   ├── DTMF/
│   ├── Tesla/
│   ├── PrintedParts/
│   ├── Ghost/
│   ├── kd/
│   └── Nothing Expected/
├── Misc/
│   ├── Counting/
│   ├── Dots/
│   ├── Emoji/
│   ├── Insanity 1/
│   ├── MazeRunna/
│   ├── Spectrum/
│   └── Trapped/
├── OSINT/
│   ├── Frog Finder 2/
│   ├── MultiVerse/
│   ├── Lookup 0xfun/
│   ├── Malware Analysis 1/
│   ├── Malware Analysis 2/
│   └── Malware Analysis 3/
├── Web/
│   ├── Tony Toolkit/
└── README.md
```

## Resources organization

- **Every challenge has its own `Resources/` folder** for that challenge’s files (scripts, challenge binaries, images, extracted data).
- Writeups link to these files using **Resources/** paths (e.g. `[Resources/solve.py](Resources/solve.py)`, `[Resources/decoded-image.png](Resources/decoded-image.png)`).
- Place any personal resources (screenshots, solver scripts, challenge files) in the challenge’s **Resources/** folder so the writeup links resolve.

---

*Happy Hacking!*
