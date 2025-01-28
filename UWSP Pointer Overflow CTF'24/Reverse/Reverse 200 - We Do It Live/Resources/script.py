import struct

def reverse_transform(v2):
    original_chars = []
    for char in v2:
        # Apply the reverse transformation
        original_char = (ord(char) - 5) ^ 63
        original_chars.append(chr(original_char))
    return ''.join(original_chars)

def ulong_to_ascii_values(value):
    # Pack the unsigned long integer into bytes (little-endian format)
    packed_value = struct.pack('<Q', value)  # '<Q' for little-endian unsigned long long
    # Convert bytes to their ASCII integer values
    return [b for b in packed_value]

def transform_ascii_values(ascii_values):
    original_chars = []
    for value in ascii_values:
        # Subtract 5 and then apply XOR with 63
        transformed_value = (value - 5) ^ 63
        # Convert back to character and add to the list
        original_chars.append(chr(transformed_value))
    return ''.join(original_chars)

# Process the first part
v2 = "TUaP^IOM"
flag_part_1 = reverse_transform(v2)

# Process the second part
v3 = 6225401146968986705
v4 = 7281577388051686673
v5 = 5141230679910321939
ascii_values_v3 = ulong_to_ascii_values(v3)
ascii_values_v4 = ulong_to_ascii_values(v4)
ascii_values_v5 = ulong_to_ascii_values(v5)
all_ascii_values = ascii_values_v3 + ascii_values_v4 + ascii_values_v5
flag_part_2 = transform_ascii_values(all_ascii_values)

# Combine the results to get the full flag
flag = flag_part_1 + flag_part_2
print("Flag:", flag)