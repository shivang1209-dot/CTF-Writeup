#!/usr/bin/env python3
# solve_send_filename.py
# pip install pwntools

from pwn import remote
import re
import sys
import time

HOST = "augury.challs.pwnoh.io"
PORT = 1337
A = 3404970675
B = 3553295105
MOD = 2**32
PNG_HEADER = bytes.fromhex("89504e470d0a1a0a")

def recv_all_with_timeout(r, timeout=1.0):
    """Read from socket until timeout elapses with no data."""
    data = b""
    t0 = time.time()
    while True:
        try:
            chunk = r.recv(timeout=timeout)
            if not chunk:
                break
            data += chunk
            t0 = time.time()
        except Exception:
            break
        if time.time() - t0 > timeout:
            break
    return data

def fetch_and_choose_file(host, port, choice=b"2\n", timeout=1.0):
    r = remote(host, port, ssl=True, timeout=8)
    # try to sync to menu prompt
    try:
        r.recvuntil(b"> ", timeout=3)
    except Exception:
        pass
    # send option 2 (view files)
    r.send(choice)
    # read the response block where filenames are printed and service asks for choice
    part = recv_all_with_timeout(r, timeout=timeout)
    text = part.decode(errors="replace")
    # Try to extract filenames: words with an extension, e.g. name.ext
    candidates = re.findall(r'\b[A-Za-z0-9_\-\.]+\.[A-Za-z0-9]{1,6}\b', text)
    # Filter out long hex-like things accidentally picked up (only keep those with letters outside a-f or with dot)
    filtered = []
    for c in candidates:
        # require a dot (already ensured) and not all hex and length less than some huge value
        if len(c) > 200: 
            continue
        # reject pure hex (no dot) — we've already got dot so ok
        filtered.append(c)
    if not filtered:
        # fallback: if server printed "Available files:" then maybe filenames are on following lines; try to read more
        more = recv_all_with_timeout(r, timeout=1.0)
        text2 = (text + more.decode(errors="replace"))
        filtered = re.findall(r'\b[A-Za-z0-9_\-\.]+\.[A-Za-z0-9]{1,6}\b', text2)
    # choose a sensible filename: prefer one containing 'secret', otherwise first candidate
    filename = None
    if filtered:
        for f in filtered:
            if 'secret' in f.lower():
                filename = f
                break
        if filename is None:
            filename = filtered[0]
    else:
        # Last-resort: try the common name used in challenge
        filename = "secret_pic.png"

    # send the filename
    r.send((filename + "\n").encode())
    # now read everything server sends (the hex blob and potentially the menu)
    full = recv_all_with_timeout(r, timeout=2.0)
    try:
        r.close()
    except Exception:
        pass
    return text + full.decode(errors="replace"), filename

def extract_longest_hex(s: str):
    matches = re.findall(r'[0-9a-fA-F]{16,}', s)
    if not matches:
        return None
    return max(matches, key=len)

def decrypt_from_hex(hexstr: str) -> bytes:
    cipher = bytes.fromhex(hexstr)
    if len(cipher) < 4:
        raise ValueError("ciphertext too short")
    p0 = PNG_HEADER[:4]
    c0 = cipher[:4]
    k = int.from_bytes(bytes([c0[i] ^ p0[i] for i in range(4)]), "big")
    out = bytearray()
    i = 0
    while i < len(cipher):
        kb = k.to_bytes(4, "big")
        for j in range(4):
            if i + j >= len(cipher):
                break
            out.append(cipher[i+j] ^ kb[j])
        i += 4
        k = (k * A + B) % MOD
    return bytes(out)

def main():
    print("[*] Connecting, listing files and choosing a filename...")
    raw_response, chosen = fetch_and_choose_file(HOST, PORT)
    print(f"[*] Chosen filename: {chosen}")
    # debug: you can uncomment to inspect raw server response
    # print("---- server response ----\n", raw_response, "\n---- end ----")
    hexstr = extract_longest_hex(raw_response)
    if not hexstr:
        print("[!] Could not find hex blob in server response. Full response below for inspection:\n")
        print(raw_response)
        sys.exit(1)
    print(f"[*] Found hex blob of length {len(hexstr)} (bytes: {len(hexstr)//2})")
    plain = decrypt_from_hex(hexstr)
    if plain.startswith(PNG_HEADER):
        print("[+] Decrypted file starts with PNG header - looks good.")
    else:
        print("[!] Warning: decrypted data does not start with PNG header. Still writing output for inspection.")
    outname = "secret.png"
    with open(outname, "wb") as f:
        f.write(plain)
    print(f"[+] Written decrypted file to {outname}")

if __name__ == "__main__":
    main()
