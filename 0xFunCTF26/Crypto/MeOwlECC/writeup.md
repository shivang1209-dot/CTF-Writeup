# Challenge Name: MeOwl ECC

## Description

**Category:** Crypto

> ECC-based challenge: recover the private key and decrypt the flag.

**Provided files:** [chall.py](Resources/chall.py), [output.txt](Resources/output.txt)

**Flag format:** `0xfun{...}`

---

## Writeup

### Summary

- **Curve:** `y² = x³ + 19` over `GF(p)` (anomalous: `#E = p`).
- **Given:** Generator point `P`, public point `Q = d*P`, AES+DES encrypted flag.
- **Attack:** Smart's attack on anomalous curves (ECDLP in polynomial time).

### Step 1: Anomalous Curve

The curve has order `#E(F_p) = p`. The curve is *anomalous*, so Smart's attack applies.

### Step 2: Smart's Attack

Lift the curve and points to the p-adics (or work in `Z/p²Z` with a randomized lift to avoid the canonical lift). Recover the discrete log `d` with `Q = d*P` from the formal group.

### Step 3: Decryption

`d` is used to derive keys:

- `k = long_to_bytes(d)`
- `aes_key = SHA256(k || "MeOwl::AES").digest()[:16]`
- `des_key = SHA256(k || "MeOwl::DES").digest()[:8]`

Ciphertext is DES-CBC then AES-CBC; decrypt with DES first, then AES.

### How to Run

- **With Sage (e.g. Docker):**

```bash
docker run --rm -v "$(pwd):/work" -w /work sagemath/sagemath sage Resources/solve.sage
```

- **One-liner:**

```bash
./Resources/run_solve.sh
```

- **Decrypt only (if you already have `d`):**

```bash
python3 Resources/solve.py --decrypt <d>
```

---

## Resources

- **[Resources/chall.py](Resources/chall.py)** — Challenge encryption script.
- **[Resources/output.txt](Resources/output.txt)** — Challenge encrypted output.
- **[Resources/solve.sage](Resources/solve.sage)** — Sage script: curve setup, Smart's attack, optional decryption.
- **[Resources/solve.sage.py](Resources/solve.sage.py)** — Auto-generated Python version of the Sage script.
- **[Resources/solve.py](Resources/solve.py)** — Pure Python: decryption with `--decrypt <d>`.
- **[Resources/run_solve.sh](Resources/run_solve.sh)** — Runs Sage in Docker and then decrypts.

---

## Flag

```
0xfun{n0n_c4n0n1c4l_l1f7s_r_c00l}
```
