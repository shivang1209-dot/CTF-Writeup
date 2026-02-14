# Challenge Name: MeOwl ECC

## Description

ECC-based challenge: recover the private key and decrypt the flag.

**Flag Format:** `0xfun{.*}`

---

## Writeup

### Summary

- **Curve:** `y² = x³ + 19` over `GF(p)` (anomalous: `#E = p`).
- **Given:** Generator point `P`, public point `Q = d*P`, AES+DES encrypted flag.
- **Attack:** Smart’s attack on anomalous curves (ECDLP in polynomial time).
- **Flag:** `0xfun{n0n_c4n0n1c4l_l1f7s_r_c00l}`

### Step 1: Anomalous Curve

The curve has order `#E(F_p) = p`. The curve is *anomalous*, so Smart’s attack applies.

### Step 2: Smart’s Attack

Lift the curve and points to the p-adics (or work in `Z/p²Z` with a randomized lift to avoid the canonical lift). Recover the discrete log `d` with `Q = d*P` from the formal group (e.g. ratio of parameters mod `p`).

### Step 3: Decryption

`d` is used to derive keys:

- `k = long_to_bytes(d)`
- `aes_key = SHA256(k || "MeOwl::AES").digest()[:16]`
- `des_key = SHA256(k || "MeOwl::DES").digest()[:8]`

Ciphertext is DES-CBC then AES-CBC; decrypt with DES first, then AES.

### How to Run

Run from the challenge folder (so `Resources/` is available):

- **With Sage (e.g. Docker):**  
  `docker run --rm -v "$(pwd):/work" -w /work sagemath/sagemath sage Resources/solve.sage`  
  If `Crypto` is not available, the script prints `d`; then run:  
  `python3 Resources/solve.py --decrypt <d>`

- **One-liner:**  
  `./Resources/run_solve.sh`  
  (runs Sage in Docker, extracts `d`, then runs `Resources/solve.py --decrypt`)

- **Decrypt only (if you already have `d`):**  
  `python3 Resources/solve.py --decrypt <d>`

---

## Resources

- **[Resources/solve.sage](Resources/solve.sage)** — Sage script: curve setup, Smart’s attack, optional decryption.
- **[Resources/solve.py](Resources/solve.py)** — Pure Python: decryption and `--decrypt <d>`; optional pure-Python Smart’s attack.
- **[Resources/run_solve.sh](Resources/run_solve.sh)** — Runs Sage in Docker and then decrypts with `Resources/solve.py`.
- **Resources/** also contains challenge files (e.g. from `MeOwl ECC`): `chall.py`, `output.txt`.

---

## Flag

```
0xfun{n0n_c4n0n1c4l_l1f7s_r_c00l}
```

---
