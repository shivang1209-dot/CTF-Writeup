# Challenge Name: UART

## Description

**Category:** Warmup

> A strange transmission has been recorded. Something valuable lies within.

**Provided files:** [Resources/](Resources/) — sigrok logic capture (`metadata`, `version`, `logic-1-1`).

**Flag format:** `0xfun{...}`

---

## Writeup

### Step 1: Understanding the Capture

The challenge provides a **sigrok logic capture** of a UART (serial) transmission:

- `logic-1-1` — raw logic samples (1 probe, 1 MHz): each byte is one sample (0 = low, 1 = high).
- `metadata` — sigrok metadata (probe `uart.ch1`, samplerate 1 MHz).
- `version` — session format version.

### Step 2: Building a Sigrok Session

Pack the files from **Resources/** into a sigrok session (ZIP with `.sr` extension):

```bash
cd Resources && zip -j uart.sr metadata version logic-1-1
```

The pre-built session file is [uart.sr](Resources/uart.sr).

### Step 3: Decoding UART

Use sigrok-cli with the built-in UART decoder:

```bash
sigrok-cli -i Resources/uart.sr -I logic -P uart
```

### Step 4: Extracting the Flag

From the decoder output, extract lines like `uart-1: 30` (hex bytes). Convert the hex bytes to ASCII to get the flag string.

---

## Resources

- **[Resources/metadata](Resources/metadata)** — Sigrok session metadata.
- **[Resources/version](Resources/version)** — Session format version.
- **[Resources/logic-1-1](Resources/logic-1-1)** — Raw logic capture data.
- **[Resources/uart.sr](Resources/uart.sr)** — Pre-built sigrok session file.

---

## Flag

```
0xfun{UART_82_M2_B392n9dn2}
```
