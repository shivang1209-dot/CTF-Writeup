# Challenge Name: Guess The Seed

## Description

**Category:** Reverse Engineering (50 pts)  

*I've created the ultimate number guessing game! Nobody can guess my completely unpredictable numbers. If you can somehow beat these mathematical odds and guess all 5 numbers correctly, I'll give you the flag.*

**Provided file:** [Resources/guess_the_seed](Resources/guess_the_seed) — stripped Linux ELF 64-bit binary.

**Flag format:** `0xfun{...}`

---

## Writeup

### Step 1: Recon

```bash
file guess_the_seed
# ELF 64-bit LSB pie executable, x86-64, dynamically linked, stripped
```

`strings` shows `time`, `srand`, `rand`, `scanf`, `printf` — the program uses **libc RNG** seeded with time.

### Step 2: Static Analysis

Decompilation shows:

- `srand(time(NULL));`
- Five values: `rand() % 1000` (each).
- User input is compared to these five numbers.

So the “secret” numbers are deterministic from the **Unix timestamp** at which the program was run.

### Step 3: Vulnerability

`time(NULL)` has 1-second resolution and glibc `rand()` is deterministic, so we can **replicate** the sequence by trying nearby timestamps.

### Step 4: Strategy

1. Replicate glibc `rand()` (same libc as target; use Docker if needed: `linux/amd64`).
2. For timestamps around “now” (e.g. ±10 seconds), compute `srand(seed)` then five times `rand() % 1000`.
3. Run the binary and, when it prompts, enter the five numbers from the matching timestamp.

### Step 5: Solver Script

Example (run in an environment with the same libc as the binary, e.g. Docker `ubuntu`):

```python
import ctypes
import time

libc = ctypes.CDLL("libc.so.6")
now = int(time.time())

for delta in range(-10, 11):
    libc.srand(now + delta)
    nums = [libc.rand() % 1000 for _ in range(5)]
    print(f"{delta:+} ->", *nums)
```

Run `python3 Resources/solve.py`, then start `./guess_the_seed` and enter the five numbers for the correct time offset (e.g. `+1`).

### Step 6: Result

When the five numbers match, the program prints the flag.

---

## Resources

- **[Resources/guess_the_seed](Resources/guess_the_seed)** — Challenge binary.
- **[Resources/solve.py](Resources/solve.py)** — Script to generate candidate numbers for nearby timestamps (use same arch/libc as target).

---

## Flag

```
0xfun{W3l1_7h4t_w4S_Fun_4235328752619125}
```

---
