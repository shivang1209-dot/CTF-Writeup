# Challenge Name: UART

## Description

A strange transmission has been recorded. Something valuable lies within.

**Flag Format:** `0xfun{.*}`

---

## Writeup

### Step 1: Understanding the Capture

The challenge provides a **sigrok logic capture** of a UART (serial) transmission:

- `logic-1-1` — raw logic samples (1 probe, 1 MHz): each byte is one sample (0 = low, 1 = high)
- `metadata` — sigrok metadata (probe `uart.ch1`, samplerate 1 MHz)
- `version` — session format version

### Step 2: Building a Sigrok Session

Pack the files from **Resources** into a sigrok session (ZIP with `.sr` extension):

```bash
cd "Warmup/UART/Resources" && zip -j ../uart.sr metadata version logic-1-1
```

### Step 3: Decoding UART

Use sigrok-cli with the built-in UART decoder (baud is auto-detected):

```bash
sigrok-cli -i uart.sr -I logic -P uart
```

### Step 4: Extracting the Flag

From the decoder output, extract lines like `uart-1: 30` (hex bytes). Convert the hex bytes to ASCII to get the flag string.

---

## Flag

```
0xfun{UART_82_M2_B392n9dn2}
```

---

## Resources

- **[Resources/](Resources/)** — Challenge files: `metadata`, `version`, `logic-1-1` (sigrok logic capture).

---
