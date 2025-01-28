def reconstruct_key():
    key = bytearray(22)
    # Equivalent values from the code, reconstructed
    section1 = bytearray("tsxv", 'ascii')
    section1.append(103)
    for i in range(len(section1)):
        key[i] = section1[i] ^ 16
    
    section2 = bytearray([1027284744 >> (i * 8) & 0xFF for i in range(4)])
    section2.append(47)
    for i in range(len(section2)):
        key[5 + i] = section2[i] ^ 90
    
    section3 = bytearray([18377328 >> (i * 8) & 0xFF for i in range(4)])
    section3.append(80)
    for i in range(len(section3)):
        key[10 + i] = section3[i] ^ 32
    
    section4 = bytearray([1701714534 >> (i * 8) & 0xFF for i in range(4)])
    section4.extend(bytearray([1934431845 >> (i * 8) & 0xFF for i in range(2)]))
    for i in range(len(section4)):
        key[15 + i] = (48 if i <= 4 else 0) ^ section4[i]
    
    return key.decode('ascii')

def decrypt_flag(key):
    encrypted = [
        1598823021010422804,
        2391150064061842708,
        4346327761577126938,
        600200794888878428
    ]
    
    encrypted_bytes = bytearray()
    for num in encrypted:
        encrypted_bytes.extend(num.to_bytes(8, 'little'))

    for i in range(len(encrypted_bytes)):
        encrypted_bytes[i] ^= key[i % len(key)]
    
    decrypted_flag = encrypted_bytes.decode('ascii').strip()
    print("Flag:", decrypted_flag)

key = reconstruct_key()
print("Generated Key:", key)
decrypt_flag(bytearray(key, 'ascii'))
