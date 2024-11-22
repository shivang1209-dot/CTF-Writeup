# Base64 character set
CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def base64_to_bits(b64_string):
    # Convert each Base64 character to its 6-bit binary representation
    bits = ''.join(format(CHARSET.index(char), '06b') for char in b64_string if char in CHARSET)
    return bits

with open('Resources/steg64.txt', 'r') as f:
    base64_strings = f.readlines()

total_hidden = ''

for s in base64_strings:
    s = s.strip()  # Remove any extra spaces or newlines from the base64 string
    bits = base64_to_bits(s)
    
    # Get the hidden portion (padding bits)
    visible = bits[:(len(bits) // 8) * 8]  # Whole octets (8 bits each)
    hidden = bits[len(visible):]  # Remaining bits are hidden
    
    total_hidden += hidden

# Convert hidden bits to bytes (Hidden Message)
decoded_bytes = bytes([int(total_hidden[i:i+8], 2) for i in range(0, len(total_hidden), 8)])
print("Hidden Message:", decoded_bytes.decode(errors='ignore'))
