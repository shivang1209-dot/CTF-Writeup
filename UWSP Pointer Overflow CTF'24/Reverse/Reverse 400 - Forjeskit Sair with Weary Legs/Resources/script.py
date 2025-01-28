from Crypto.Cipher import AES

# XOR operation with 42 for each byte in the input
def xor_42(data):
    return ''.join(chr(byte ^ 42) for byte in data)

# Transformation of the letter based on a given key
def transform(letter, key):
    return (letter >> key) | (letter << (8 - key)) & 255

# Main processing function that uses the transform function for each byte
def process(text, key, iv):
    result = bytearray()
    for index, letter in enumerate(text):
        # Calculate the shift value (H) using the key and IV
        shift_value = (key[index % len(key)] + iv[index % len(iv)]) % 8
        result.append(transform(letter, shift_value))
    return result

# AES decryption function using CBC mode
def decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.decrypt(ciphertext)

# Main script
encrypted_flag = 'fa21c9c2596099915dbc7845c941c14e81594b5c4f69177cc4059da11e782e0b'
key = bytes.fromhex('504f43544632303234').ljust(16, b'\x00')  # 16-byte key, padded if necessary
iv = bytes.fromhex('437261636b3430302d58'.ljust(32, '0'))  # 32-byte IV, padded if necessary

# Perform decryption, process the result, and XOR with 42
decrypted_data = decrypt(bytes.fromhex(encrypted_flag), key, iv)
processed_data = process(decrypted_data, key, iv)
final_result = xor_42(processed_data)

print(final_result)
