data = open("FLGPRNTR.COM","rb").read()
dec = bytes(b ^ 0x2A for b in data)
print(dec.decode("latin1",errors="ignore"))
