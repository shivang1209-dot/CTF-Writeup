#!/usr/bin/env python3
"""
Reconstruct a probable .zip from a $pkzip2$ hash string and try to extract a file
using a known password.

Usage:
  python3 reconstruct_pkzip2.py

Outputs:
  - candidate zip files: reconstructed_flag_c{comp}_u{unc}.zip
  - an extracted file if found: reconstructed_flag_c{...}.zip.extracted
"""
import re, binascii, struct, zipfile, os, sys

HASH_LINE = ("flag.zip/flag.txt:$pkzip2$1*1*2*0*34*28*64ac0ae2*0*26*0*34*64ac*"
             "a388*2c386d49756e1d70ab5f2d8b7ccf1703b28d2775e84d89ccf4bf26d0e"
             "735e9a817b0032b5071540889c34b9331b694d6042c30a0*$/pkzip2$:flag.txt:flag.zip::flag.zip")

PASSWORD = b"factfinder"
OUT_DIR = "reconstructed_out"
os.makedirs(OUT_DIR, exist_ok=True)

def le32(x): return struct.pack('<I', x)
def le16(x): return struct.pack('<H', x)

# Parse $pkzip2$ block
m = re.search(r'\$pkzip2\$(.*?)\$/pkzip2\$', HASH_LINE)
if not m:
    print("ERROR: no $pkzip2$ block found in HASH_LINE")
    sys.exit(1)

fields = m.group(1).split('*')

hex_candidates = [f for f in fields if re.fullmatch(r'[0-9A-Fa-f]+', f)]
if not hex_candidates:
    print("ERROR: no hex-like fields found inside $pkzip2$ block")
    sys.exit(1)


enc_hex_candidates = [h for h in hex_candidates if len(h) % 2 == 0]
if not enc_hex_candidates:
    enc_hex_candidates = hex_candidates
enc_hex = max(enc_hex_candidates, key=len)

enc = binascii.unhexlify(enc_hex)

crc_candidates = [f for f in fields if re.fullmatch(r'[0-9A-Fa-f]{8}', f)]
crc32_val = int(crc_candidates[0], 16) if crc_candidates else 0

trailing = HASH_LINE.split("$/pkzip2$")[-1]

trail_parts = trailing.split(':')
filename_guess = "flag.txt"
for part in trail_parts:
    if part and part.lower().endswith(".txt"):
        filename_guess = part
        break

print(f"Using encrypted blob length {len(enc)} bytes, crc32={hex(crc32_val)}, filename='{filename_guess}'")

compression_options = [0, 8]
unc_size_guesses = [0, 28, 34, len(enc), 52, 60, 100, 200, 300]

written = []
for comp in compression_options:
    for unc_guess in unc_size_guesses:
        fname_bytes = filename_guess.encode()
        # Local file header
        version_needed = 20
        gp_flag = 1  # bit 0 = encrypted
        modtime = 0
        moddate = 0
        local_header = b''
        local_header += struct.pack('<I', 0x04034b50)
        local_header += le16(version_needed)
        local_header += le16(gp_flag)
        local_header += le16(comp)
        local_header += le16(modtime)
        local_header += le16(moddate)
        local_header += le32(crc32_val)
        local_header += le32(len(enc))    
        local_header += le32(unc_guess)   
        local_header += le16(len(fname_bytes))
        local_header += le16(0)
        
        file_record = local_header + fname_bytes + enc

        # Central directory header
        centr = b''
        centr += struct.pack('<I', 0x02014b50)
        centr += le16(0x14)
        centr += le16(version_needed)
        centr += le16(gp_flag)
        centr += le16(comp)
        centr += le16(modtime)
        centr += le16(moddate)
        centr += le32(crc32_val)
        centr += le32(len(enc))
        centr += le32(unc_guess)
        centr += le16(len(fname_bytes))
        centr += le16(0)   # extra len
        centr += le16(0)   # comment len
        centr += le16(0)   # disk start
        centr += le16(0)   # internal attrs
        centr += le32(0)   # external attrs
        centr += le32(0)   # relative offset (we used 0)
        centr += fname_bytes

        # End of central directory (EOCD)
        eocd = b''
        eocd += struct.pack('<I', 0x06054b50)
        eocd += le16(0)    # disk
        eocd += le16(0)    # start disk
        eocd += le16(1)    # records on this disk
        eocd += le16(1)    # total records
        eocd += le32(len(centr))
        eocd += le32(len(file_record))
        eocd += le16(0)    # comment len

        zip_bytes = file_record + centr + eocd
        fname_out = f"reconstructed_flag_c{comp}_u{unc_guess}.zip"
        outpath = os.path.join(OUT_DIR, fname_out)
        with open(outpath, "wb") as fh:
            fh.write(zip_bytes)
        written.append(outpath)

        # Try opening and extracting using Python's zipfile (password provided)
        extracted_ok = False
        try:
            with zipfile.ZipFile(outpath) as zf:
                names = zf.namelist()
                if filename_guess in names:
                    try:
                        data = zf.read(filename_guess, pwd=PASSWORD)
                        # write extracted
                        extpath = outpath + ".extracted"
                        with open(extpath, "wb") as ef:
                            ef.write(data)
                        print(f"[+] Success: extracted {filename_guess} from {outpath} -> {extpath}")
                        try:
                            print("    (decoded text):")
                            print(data.decode('utf-8', errors='replace'))
                        except Exception:
                            print("    (binary data saved)")
                        extracted_ok = True
                        # Do not break so script produces all candidates, but continue to show results.
                    except RuntimeError as e:
                        # Wrong password or decompression error
                        pass
                    except zipfile.BadZipFile:
                        pass
        except Exception as e:
            pass

if not written:
    print("No candidate zips written — unexpected")
else:
    print("\nWrote candidate zip files to directory:", OUT_DIR)
    print("Check any '*.extracted' files there for recovered plaintext.")
