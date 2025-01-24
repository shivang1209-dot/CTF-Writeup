# RSA parameters
p = 61
q = 53
n = 3233
e = 17
d = 2753

# Function to decrypt the ciphertext using RSA
def rsa_decrypt(ciphertext_hex, d, n):
    # Convert the ciphertext from hexadecimal to decimal
    ciphertext_decimal = [int(c, 16) for c in ciphertext_hex]
    
    # Decrypt each block using the RSA decryption formula
    plaintext_decimal = [pow(c, d, n) for c in ciphertext_decimal]
    
    # Convert the decimal values back to ASCII characters
    plaintext = ''.join(chr(m) for m in plaintext_decimal)
    
    return plaintext

# Input ciphertext in hexadecimal (output from encryption script)
ciphertext_hex = input("Enter the ciphertext in hex (space separated): ").split()

# Decrypt the ciphertext
plaintext = rsa_decrypt(ciphertext_hex, d, n)

# Print the decrypted plaintext
print("Decrypted plaintext:", plaintext)
