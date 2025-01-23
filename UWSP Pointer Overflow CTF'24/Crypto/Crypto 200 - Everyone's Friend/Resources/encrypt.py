# RSA parameters
p = 61
q = 53
n = 3233
e = 17
d = 2753

# Function to encrypt the plaintext message using RSA
def rsa_encrypt(plaintext, e, n):
    # Convert the plaintext to ASCII values
    plaintext_ascii = [ord(char) for char in plaintext]
    
    # Encrypt each ASCII value using the RSA encryption formula
    ciphertext = [pow(m, e, n) for m in plaintext_ascii]
    
    # Convert the ciphertext into hexadecimal format
    ciphertext_hex = [hex(c)[2:] for c in ciphertext]
    
    return ciphertext_hex

# Input plaintext
plaintext = input("Enter the plaintext message: ")

# Encrypt the plaintext
ciphertext_hex = rsa_encrypt(plaintext, e, n)

# Print the ciphertext in hexadecimal format
print("Ciphertext in hex:", ' '.join(ciphertext_hex))
