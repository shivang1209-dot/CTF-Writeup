# Challenge Name: Mind Boggle

## Description

My friend gave me this file, but I have no idea what it means!!!!! HELP

**Files:**
- `mystery.txt` - Contains encoded data

---

## Writeup

### Step 1: Identifying the Encoding

Looking at the file contents, it contains a series of characters like:
```
-[----->+<]>++.++++.---.[->++++++<]>.[---->+++<]>+...
```

This is clearly **Brainfuck** code - an esoteric programming language that uses only 8 characters: `+`, `-`, `>`, `<`, `[`, `]`, `.`, and `,`.

### Step 2: Decoding Brainfuck

We can use an online Brainfuck interpreter like [dcode.fr](https://www.dcode.fr/brainfuck-language) to decode the Brainfuck code.

The Brainfuck program outputs:
```
596D4E305A6E7430636A467762444E664E30677A583277306557565363313955636A467762444E66644768465830567559334A35554851784D453539
```

### Step 3: Hex Decoding

The output is hexadecimal-encoded. Decoding it gives:
```
YmN0Znt0cjFwbDNfN0gzX2w0eWVSc19UcjFwbDNfdGhFX0VuY3J5UHQxME59
```

### Step 4: Base64 Decoding

The hex-decoded string is Base64-encoded. Decoding it reveals the flag.

---

## Flag

```
bctf{tr1pl3_7H3_l4yeRs_Tr1pl3_thE_EncryPt10N}
```

---

