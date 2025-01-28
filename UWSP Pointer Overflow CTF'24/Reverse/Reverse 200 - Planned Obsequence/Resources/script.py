# Hexadecimal representation of the obfuscated flag
hex_obfuscated_flag = "2d383c313f2432302c2d08710870356e376f086d3f083b6c713270262a"

# Convert hex to ASCII characters
obfuscated_flag = bytes.fromhex(hex_obfuscated_flag)


def deobfuscate(flag):
    deobfuscated_flag = ""
    for char in flag:
        # Reverse the obfuscation steps: subtract 3, then XOR with 0x5A
        original_char = (char - 3) ^ 0x5A
        deobfuscated_flag += chr(original_char)
    return deobfuscated_flag

# Run deobfuscation
flag = deobfuscate(obfuscated_flag)
print("Deobfuscated Flag:", flag)
