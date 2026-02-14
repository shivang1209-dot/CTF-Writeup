# Challenge Name: TheSlotWhisperer

## Description

**Category:** Crypto

> The oldest slot machine in the casino runs on predictable gears. Watch it spin, learn its rhythm, and predict what comes next.

**Connection:** `nc chall.0xfun.org 63653`

**Flag format:** `0xfun{...}`

---

## Writeup

### Step 1: Observing the Service

The server outputs 10 numbers (e.g. 50, 12, 17, 35, 52, 42, 0, 70, 56, 91) and asks for the next 5 spins (space-separated). The challenge source is in [slot.py](Resources/slot.py).

### Step 2: Identifying the PRNG

The server uses an **LCG** (Linear Congruential Generator) with:

- `M = 2147483647`, `A = 48271`, `C = 12345`
- Each "spin" is `next() % 100`, i.e. internal state modulo 100.

The server sends **10 numbers**: `state_0 % 100` through `state_9 % 100`. We must predict the **next 5 spins**.

### Step 3: Recovering the Full State

We only see `state_i % 100`, so the full state is `state_i = s_i + 100*k` for some unknown `k`. Brute force over `k`: try `state_0 = observed[0] + 100*k` for `k = 0, 1, ...` and check that running the LCG gives `state_1 % 100 == observed[1]`, ..., `state_9 % 100 == observed[9]`. The first matching `state_0` is the seed. Then advance 9 steps and output the next 5 spins.

### Step 4: Running the Solver

```bash
python3 Resources/slot.py
```

Submit the next 5 numbers; the server responds with the flag.

---

## Resources

- **[Resources/slot.py](Resources/slot.py)** — Challenge source / solver reference.

---

## Flag

```
0xfun{sl0t_wh1sp3r3r_lcg_cr4ck3d}
```
