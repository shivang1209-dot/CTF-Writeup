#!/usr/bin/env sage
# -*- coding: utf-8 -*-
"""
MeOwl ECC - Solve script.
Curve: y^2 = x^3 + 19 over GF(p). If #E = p (anomalous), use Smart's attack for ECDLP.
Then decrypt: ciphertext is DES then AES; we reverse (AES then DES) using key derived from d.
"""

from sage.all import EllipticCurve, GF, Qq, ZZ

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


def gf_to_qq(n, qq, x):
    return ZZ(x) if n == 1 else qq(list(map(int, x.polynomial())))


def lift_point(E, p, Px, Py):
    for P in E.lift_x(Px, all=True):
        if (P.xy()[1] % p) == (Py % p):
            return P


def smart_attack(G, P):
    """Smart's attack for anomalous curves (#E = p). Returns d such that P = d*G."""
    E = G.curve()
    if E.trace_of_frobenius() != 1:
        raise ValueError("Curve is not anomalous (trace != 1)")
    F = E.base_ring()
    q = F.characteristic()
    assert q == F.order()
    n = F.degree()
    qq = Qq(q, names="g")

    E_q = EllipticCurve(qq, [gf_to_qq(n, qq, a) + q * ZZ.random_element(1, q) for a in E.a_invariants()])
    Gx, Gy = gf_to_qq(n, qq, G.xy()[0]), gf_to_qq(n, qq, G.xy()[1])
    Gx, Gy = (q * lift_point(E_q, p, Gx, Gy)).xy()
    Px, Py = gf_to_qq(n, qq, P.xy()[0]), gf_to_qq(n, qq, P.xy()[1])
    Px, Py = (q * lift_point(E_q, p, Px, Py)).xy()
    l = ZZ(((Px / Py) / (Gx / Gy)) % p)

    if n > 1:
        G0 = p ** (n - 1) * G
        G0x, G0y = gf_to_qq(n, qq, G0.xy()[0]), gf_to_qq(n, qq, G0.xy()[1])
        G0x, G0y = (q * lift_point(E_q, p, G0x, G0y)).xy()
        for i in range(1, n):
            Pi = p ** (n - i - 1) * (P - l * G)
            if Pi.is_zero():
                continue
            Pix, Piy = gf_to_qq(n, qq, Pi.xy()[0]), gf_to_qq(n, qq, Pi.xy()[1])
            Pix, Piy = (q * lift_point(E_q, p, Pix, Piy)).xy()
            l += p ** i * ZZ(((Pix / Piy) / (G0x / G0y)) % p)

    return int(l)


def main():
    F = GF(p)
    E = EllipticCurve(F, [a, b])
    P = E(Px, Py)
    Q = E(Qx, Qy)

    n = E.order()
    print(f"[*] Curve order #E = {n}")
    print(f"[*] p = {p}")
    if n == p:
        print("[*] Anomalous curve (#E = p). Using Smart's attack.")
        d = smart_attack(P, Q)
    else:
        print("[*] Using generic discrete_log (Pohlig-Hellman, etc.)")
        d = P.discrete_log(Q)

    print(f"[*] Secret d = {d}")

    # Decrypt using d (need pycryptodome; if not in Sage env, run: python3 solve.py --decrypt <d>)
    try:
        import hashlib
        from Crypto.Cipher import AES, DES
        from Crypto.Util.Padding import unpad
        from Crypto.Util.number import long_to_bytes

        k = long_to_bytes(int(d))
        aes_key = hashlib.sha256(k + b"MeOwl::AES").digest()[:16]
        des_key = hashlib.sha256(k + b"MeOwl::DES").digest()[:8]

        c = bytes.fromhex(ciphertext_hex)
        c1 = unpad(DES.new(des_key, DES.MODE_CBC, iv=bytes.fromhex(des_iv)).decrypt(c), 8)
        flag = unpad(AES.new(aes_key, AES.MODE_CBC, iv=bytes.fromhex(aes_iv)).decrypt(c1), 16)
        print(f"[+] Flag: {flag.decode()}")
    except ImportError:
        print("[*] Crypto not available in this environment. Run: python3 solve.py --decrypt", d)


if __name__ == "__main__":
    main()
