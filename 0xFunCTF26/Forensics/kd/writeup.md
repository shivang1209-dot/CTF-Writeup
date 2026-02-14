# Challenge Name: kd

## Description

Something crashed. Something was left behind.

---

## Writeup

### Step 1: Identifying the Dump

We are given a **memory dump** ([Resources/crypter.dmp](Resources/crypter.dmp)). Check the type:

```bash
file Resources/crypter.dmp
# Mini DuMP crash report, 18 streams, ...
```

So it is a **Windows MiniDump** (crash dump).

### Step 2: Extracting Strings

Dump files often contain plaintext or encoded strings. Run:

```bash
strings Resources/crypter.dmp > strings.txt
```

### Step 3: Searching for the Flag

Search for the flag format in the strings:

```bash
grep 0xfun strings.txt
```

The flag appears in the dump as plaintext.

---

## Resources

- **[Resources/crypter.dmp](Resources/crypter.dmp)** — MiniDuMP crash report.
- **Resources/** may also contain **config.dat**, **events.xml**, **transcript.enc** as provided.

---

## Flag

```
0xfun{wh0_n33ds_sl33p_wh3n_y0u_h4v3_cr4sh_dumps}
```

---
