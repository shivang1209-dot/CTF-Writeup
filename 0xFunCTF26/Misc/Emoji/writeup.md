# Challenge Name: Emoji

## Description

**Category:** Misc

> Something seems to be in here :thinking:?

**Provided file:** [emoji.txt](Resources/emoji.txt)

**Flag format:** `0xfun{...}`

---

## Writeup

### Step 1: Emoji Steganography

The challenge suggests **emoji steganography**. A common tool is [emoji.paulbutler.org](https://emoji.paulbutler.org/?mode=decode) (decode mode).

### Step 2: Decoding the Challenge Message

Decoding the emoji in the challenge description may yield a message such as "nothing to be expected here" — a red herring for the main flag.

### Step 3: Analyzing emoji.txt

Inspect the provided [emoji.txt](Resources/emoji.txt):

```bash
xxd Resources/emoji.txt
```

The file contains UTF-8 encoded emoji sequences. Count the **unique emoji types** (e.g. 17). The pattern or mapping of these emojis encodes the hidden message.

### Step 4: Decoding the Emoji Sequence

Use the appropriate emoji-steganography scheme (e.g. mapping emoji to bits or characters) to decode the sequence in `emoji.txt` and extract the flag.

---

## Resources

- **[Resources/emoji.txt](Resources/emoji.txt)** — Challenge file with emoji-encoded data.
- **Reference tool:** [Emoji steganography (Paul Butler)](https://emoji.paulbutler.org/?mode=decode).

---

## Flag

Decoded from the emoji sequence in `emoji.txt` and submitted as `0xfun{...}`.
