#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
from Crypto.Cipher import AES, DES
from Crypto.Util.Padding import pad
from Crypto.Util.number import long_to_bytes

BANNER = r"""
   __  __      ____          _ 
  |  \/  | ___/ __ \_      _| |
  | |\/| |/ _ \ |  | \ /\ / / |
  | |  | |  __/ |__| |\ V  V /| |
  |_|  |_|\___|\____/  \_/\_/ |_|
                     ECC Cipher
"""

p = 1070960903638793793346073212977144745230649115077006408609822474051879875814028659881855169
a = 0
b = 19

Px = 850194424131363838588909772639181716366575918001556629491986206564277588835368712774900915
Py = 749509706400667976882772182663506383952119723848300900481860146956631278026417920626334886

Qx = 54250358642669756154015134950152636682437522715786363311759940981383592083045988845753867
Qy = 324772290891069325219931358863917293864610371020855881775477694333357303867104131696431188

aes_iv = "7d0e47bb8d111b626f0e17be5a761a14"
des_iv = "86fd0c44751700d4"
ciphertext = (
    "7d34910bca6f505e638ed22f412dbf1b50d03243b739de0090d07fb097ec0a2c"
    "a19158949f32e39cd84adea33d2229556f635237088316d2"
)

def check_curve(x: int, y: int) -> bool:
    lhs = (y * y) % p
    rhs = (x * x * x + a * x + b) % p
    return lhs == rhs

def encrypt_flag(d: int, flag: bytes) -> bytes:
    k = long_to_bytes(d)
    aes_key = hashlib.sha256(k + b"MeOwl::AES").digest()[:16]
    des_key = hashlib.sha256(k + b"MeOwl::DES").digest()[:8]

    c1 = AES.new(aes_key, AES.MODE_CBC, iv=bytes.fromhex(aes_iv)).encrypt(pad(flag, 16))
    c  = DES.new(des_key, DES.MODE_CBC, iv=bytes.fromhex(des_iv)).encrypt(pad(c1, 8))
    return c

def main() -> None:
    print(BANNER)
    print(f"p = {p}")
    print(f"a = {a}")
    print(f"b = {b}")
    print()
    print("P :")
    print(f"  Px = {Px}")
    print(f"  Py = {Py}")
    print()
    print("Q :")
    print(f"  Qx = {Qx}")
    print(f"  Qy = {Qy}")
    print()
    print("ciphertext =", ciphertext)
    print()

if __name__ == "__main__":
    main()
