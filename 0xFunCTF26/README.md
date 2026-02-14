# 0xFUN CTF 2026 Writeups

Welcome to my repository for the **0xFUN CTF 2026** writeups!
This CTF was organized by **Bunkyowerstens** and held online (12–14 Feb 2026). Event details: [CTFtime – 0xFUN CTF 2026](https://ctftime.org/event/3081).

## Repo Structure

This repository contains writeups for **challenges** I attempted during the competition. Each challenge has its own folder by category. Inside each folder you will find:

- A **writeup.md** in Markdown explaining how the challenge was solved.
- A **Resources/** folder containing images, scripts, and other files used during the solve (where applicable).
- **Flag(s)** or answers for the challenge.

## Categories

### Warmup (8 challenges)

| Challenge | Technique |
|-----------|-----------|
| [Shell](Warmup/Shell/) | ExifTool RCE via malicious image upload |
| [TLSB](Warmup/TLSB/) | Third Least Significant Bit steganography (BMP) |
| [Perceptions](Warmup/Perceptions/) | Multi-path blog and secret directory |
| [Music](Warmup/Music/) | Bucking Music Cipher (phonetic/notation) |
| [Templates](Warmup/Templates/) | Server-Side Template Injection (SSTI), Jinja2 RCE |
| [UART](Warmup/UART/) | Sigrok UART decode from logic capture |
| [Leonine Misbegotten](Warmup/Leonine%20Misbegotten/) | Layered Base16/32/64/85 + SHA-1 peel |
| [Guess The Seed](Warmup/Guess%20The%20Seed/) | Time-seeded rand() prediction |

### Crypto (3 challenges)

| Challenge | Technique |
|-----------|-----------|
| [MeOwl ECC](Crypto/MeOwlECC/) | Anomalous curve, Smart's attack, AES+DES decrypt |
| [TheSlotWhisperer](Crypto/TheSlotWhisperer/) | LCG prediction from partial output |
| [Back in the 90's](Crypto/Back%20in%20the%2090's/) | LSPK90-CW (Leet Speak 90° Clockwise) decode |

### Forensics (7 challenges)

| Challenge | Technique |
|-----------|-----------|
| [Bard](Forensics/Bard/) | StegSeek on JPEG, Base64 decode, fix PNG header |
| [DTMF](Forensics/DTMF/) | DTMF decode, binary → Base64, Vigenere (key in EXIF) |
| [Tesla](Forensics/Tesla/) | Flipper SubGhz batch script, XOR known-plaintext |
| [PrintedParts](Forensics/PrintedParts/) | G-code 3D print preview, flag in toolpath |
| [Ghost](Forensics/Ghost/) | PNG trailer, 7z extraction, password from image |
| [kd](Forensics/kd/) | MiniDuMP crash dump, strings |
| [Nothing Expected](Forensics/Nothing%20Expected/) | Excalidraw JSON in PNG, extract and view |

### Misc (7 challenges)

| Challenge | Technique |
|-----------|-----------|
| [Counting](Misc/Counting/) | Discord counting channel collaboration |
| [Dots](Misc/Dots/) | WAV → SSTV → DotCode barcode |
| [Emoji](Misc/Emoji/) | Emoji steganography |
| [Insanity 1](Misc/Insanity%201/) | Discord API, query user roles for flag |
| [Spectrum](Misc/Spectrum/) | Spectrogram decoy + Deepsound + PNG fix |
| [Trapped](Misc/Trapped/) | SSH, ACLs, GECOS credential, user pivot |

### OSINT (6 challenges)

| Challenge | Technique |
|-----------|-----------|
| [Frog Finder 2](OSINT/Frog%20Finder%202/) | X profile, geoOSINT, reviews for flag |
| [MultiVerse](OSINT/MultiVerse/) | Reddit + Base58, Spotify + Base64, combine flag parts |
| [Lookup 0xfun](OSINT/Lookup%200xfun/) | DNS TXT record for ctf.0xfun.org |
| [Malware Analysis 1](OSINT/Malware%20Analysis%201/) | MSI filename from report (3aw.msi) |
| [Malware Analysis 2](OSINT/Malware%20Analysis%202/) | Malicious domain (bestiamos.com) |
| [Malware Analysis 3](OSINT/Malware%20Analysis%203/) | Original MSI filename from hash lookup |

### Web (1 challenge)

| Challenge | Technique |
|-----------|-----------|
| [Tony Toolkit](Web/Tony%20Toolkit/) | SQLi, hash crack, cookie userID tampering (IDOR) |

## Folder Structure

```
0xFunCTF26/
├── README.md
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
│   ├── Spectrum/
│   └── Trapped/
├── OSINT/
│   ├── Frog Finder 2/
│   ├── MultiVerse/
│   ├── Lookup 0xfun/
│   ├── Malware Analysis 1/
│   ├── Malware Analysis 2/
│   └── Malware Analysis 3/
└── Web/
    └── Tony Toolkit/
```

## Resources Organization

- **Every challenge has its own `Resources/` folder** for scripts, challenge binaries, images, and extracted data.
- Writeups link to these files using relative `Resources/` paths (e.g. `[solve.py](Resources/solve.py)`).
- Remote-only challenges (SSH, web) may not have a Resources/ folder if no local files are needed.

---

*Happy Hacking!*
