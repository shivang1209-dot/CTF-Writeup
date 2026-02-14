#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MeOwl ECC - Pure Python solve (no Sage).
Curve: y^2 = x^3 + 19 over GF(p). Uses Smart's attack for anomalous curves (#E = p).
"""

import hashlib
from Crypto.Cipher import AES, DES
from Crypto.Util.Padding import unpad
from Crypto.Util.number import long_to_bytes

# ---------- Challenge parameters ----------
p = 1070960903638793793346073212977144745230649115077006408609822474051879875814028659881855169
a = 0
b = 19

Px = 850194424131363838588909772639181716366575918001556629491986206564277588835368712774900915
Py = 749509706400667976882772182663506383952119723848300900481860146956631278026417920626334886

Qx = 54250358642669756154015134950152636682437522715786363311759940981383592083045988845753867
Qy = 324772290891069325219931358863917293864610371020855881775477694333357303867104131696431188

aes_iv = "7d0e47bb8d111b626f0e17be5a761a14"
des_iv = "86fd0c44751700d4"
ciphertext_hex = (
    "7d34910bca6f505e638ed22f412dbf1b50d03243b739de0090d07fb097ec0a2c"
    "a19158949f32e39cd84adea33d2229556f635237088316d2"
)


def mod_inv(a, m):
    """Extended gcd: return x such that a*x ≡ 1 (mod m)."""
    def ext_gcd(a, b):
        if a == 0:
            return b, 0, 1
        g, x1, y1 = ext_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return g, x, y
    g, x, _ = ext_gcd(a % m, m)
    if g != 1:
        raise ValueError("inverse does not exist")
    return (x % m + m) % m


def hensel_lift_y(x, y, p, p2, a_eff=None, b_eff=None):
    """Lift (x,y) to Y with Y^2 = x^3 + a_eff*x + b_eff (mod p^2), Y ≡ y (mod p)."""
    if a_eff is None:
        a_eff = a
    if b_eff is None:
        b_eff = b
    rhs = (x * x * x + a_eff * x + b_eff) % p2
    f_y = (y * y - rhs) % p2
    if f_y % p != 0:
        f_y = (y * y - (x * x * x + a_eff * x + b_eff)) % p
    assert f_y % p == 0, "point not on curve"
    k = f_y // p
    denom = (2 * y) % p
    if denom == 0:
        raise ValueError("y=0, cannot lift")
    t = (k * mod_inv(denom, p)) % p
    Y = (y + t * p) % p2
    return Y


def ec_add(x1, y1, x2, y2, p2, a_eff=0):
    """Add two points on y^2 = x^3 + a_eff*x + b over Z/p^2Z."""
    if x1 is None:
        return (x2, y2)
    if x2 is None:
        return (x1, y1)
    if x1 == x2:
        if y1 == y2:
            return ec_double(x1, y1, p2, a_eff)
        else:
            return (None, None)
    dx = (x2 - x1) % p2
    dy = (y2 - y1) % p2
    lam = (dy * mod_inv(dx, p2)) % p2
    x3 = (lam * lam - x1 - x2) % p2
    y3 = (lam * (x1 - x3) - y1) % p2
    return (x3, y3)


def ec_double(x1, y1, p2, a_eff=0):
    """Double point on y^2 = x^3 + a_eff*x + b."""
    if y1 == 0:
        return (None, None)
    lam = (3 * x1 * x1 + a_eff) * mod_inv(2 * y1, p2) % p2
    x3 = (lam * lam - 2 * x1) % p2
    y3 = (lam * (x1 - x3) - y1) % p2
    return (x3, y3)


def ec_mul(n, x, y, p2, a_eff=0):
    """Scalar multiplication: n * (x, y)."""
    if n == 0:
        return (None, None)
    rx, ry = (None, None)
    bx, by = x, y
    while n:
        if n & 1:
            rx, ry = ec_add(rx, ry, bx, by, p2, a_eff)
        bx, by = ec_double(bx, by, p2, a_eff)
        n >>= 1
    return (rx, ry)


def smart_attack_python(Gx, Gy, Qx, Qy, p):
    """
    Smart's attack for anomalous curve: #E(F_p) = p.
    We have Q = d*P. Returns d.
    Uses randomized lift to avoid canonical lift (where p*G = O on same curve).
    """
    import random
    p2 = p * p
    for _ in range(100):  # retry with different random curve if canonical lift
        try:
            r, s = random.randrange(1, p), random.randrange(1, p)
            a_eff = (a + r * p) % p2
            b_eff = (b + s * p) % p2
            Gyl = hensel_lift_y(Gx, Gy, p, p2, a_eff, b_eff)
            Qyl = hensel_lift_y(Qx, Qy, p, p2, a_eff, b_eff)
            pGx, pGy = ec_mul(p, Gx, Gyl, p2, a_eff)
            pQx, pQy = ec_mul(p, Qx, Qyl, p2, a_eff)
            if pGx is None or pGy is None or pQx is None or pQy is None:
                continue
            if pGx % p != 0 or pGy % p != 0 or pQx % p != 0 or pQy % p != 0:
                continue
            a_num, b_num = pQx // p, pQy // p
            c_num, e_num = pGx // p, pGy // p
            den = (b_num * c_num) % p
            if den == 0:
                continue
            d = (a_num * e_num * mod_inv(den, p)) % p
            return d
        except ValueError:
            continue
    raise ValueError("Canonical lift: try running with Sage (sage solve.sage)")


def decrypt_with_d(d):
    """Decrypt ciphertext using secret d."""
    k = long_to_bytes(int(d))
    aes_key = hashlib.sha256(k + b"MeOwl::AES").digest()[:16]
    des_key = hashlib.sha256(k + b"MeOwl::DES").digest()[:8]
    c = bytes.fromhex(ciphertext_hex)
    c1 = unpad(DES.new(des_key, DES.MODE_CBC, iv=bytes.fromhex(des_iv)).decrypt(c), 8)
    flag = unpad(AES.new(aes_key, AES.MODE_CBC, iv=bytes.fromhex(aes_iv)).decrypt(c1), 16)
    return flag.decode()


def main():
    import sys
    if len(sys.argv) >= 3 and sys.argv[1] == "--decrypt":
        d = int(sys.argv[2])
        print(f"[+] Flag: {decrypt_with_d(d)}")
        return

    p2 = p * p
    assert (Py * Py - Px ** 3 - 19) % p == 0
    assert (Qy * Qy - Qx ** 3 - 19) % p == 0

    print("[*] Assuming anomalous curve (#E = p), using Smart's attack (pure Python).")
    try:
        d = smart_attack_python(Px, Py, Qx, Qy, p)
    except Exception as e:
        print(f"[!] Smart's attack failed: {e}")
        print("[*] Run with Sage to get d: docker run --rm -v \"$(pwd):/work\" -w /work sagemath/sagemath sage solve.sage")
        print("[*] Then: python3 solve.py --decrypt <d>")
        return
    print(f"[*] Secret d = {d}")

    print(f"[+] Flag: {decrypt_with_d(d)}")


if __name__ == "__main__":
    main()
