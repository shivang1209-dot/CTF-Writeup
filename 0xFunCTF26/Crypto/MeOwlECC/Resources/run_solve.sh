#!/bin/sh
# Full solve: run Sage (Smart's attack) then decrypt with Python.
# Requires: Docker, pycryptodome
cd "$(dirname "$0")"
echo "[*] Running Smart's attack with Sage (Docker)..."
d=$(docker run --rm -v "$(pwd):/work" -w /work sagemath/sagemath sage solve.sage 2>&1 | tee /dev/stderr | grep 'Secret d = ' | sed 's/.*Secret d = //')
if [ -z "$d" ]; then
  echo "[!] Could not get d. Check Sage output above."
  exit 1
fi
echo "[*] Decrypting with d=$d"
python3 solve.py --decrypt "$d"
