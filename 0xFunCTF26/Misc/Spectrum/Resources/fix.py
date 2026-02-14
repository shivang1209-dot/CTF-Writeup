import struct, zlib
sig = bytes.fromhex("89504e470d0a1a0a")
with open("seccat.png", "rb") as f:
    raw = f.read()
def make_ihdr(w, h, depth=8, color_type=6):
    data = b'IHDR' + struct.pack('>IIBBBBB', w, h, depth, color_type, 0, 0, 0)
    crc = zlib.crc32(data) & 0xffffffff
    return struct.pack('>I', 13) + data + struct.pack('>I', crc)
fixed = sig + make_ihdr(796, 541, color_type=6) + raw[8:]

iend = bytes.fromhex("0000000049454e44ae426082")
pos = fixed.find(iend)
# Remove the erroneous first IEND, keep everything else, then append IEND at end
without_first_iend = fixed[:pos] + fixed[pos + len(iend):]
final = without_first_iend + iend
with open("seccat_fixed.png", "wb") as f:
    f.write(final)
print("Final size:", len(final))