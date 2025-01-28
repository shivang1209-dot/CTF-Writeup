def hex_dump(file_path):
    """Generate a hex dump of the binary file."""
    with open(file_path, 'rb') as file:
        data = file.read()
    return data.hex()

def extract_binary_and_convert_to_ascii(file_path, output_file='flag.txt'):
    """Extract binary values based on ZWSP (e2808b) and ZWNJ (e2808c) presence, convert to ASCII, and write to output file."""
    # Generate the hex dump of the file
    hex_data = hex_dump(file_path)
    
    # Define the hex patterns for ZWSP and ZWNJ
    zwsp_hex = 'e2808b'  # Zero Width Space (1)
    zwnj_hex = 'e2808c'  # Zero Width Non-Joiner (0)

    # Initialize a variable to hold the binary string
    binary_result = []

    # Iterate through the hex data
    i = 0
    while i < len(hex_data) - 6:
        next_char = hex_data[i:i+6]
        
        # Append '1' or '0' based on the presence of ZWSP or ZWNJ
        if next_char == zwsp_hex:
            binary_result.append('1')
            i += 6  # Move to the next character
        elif next_char == zwnj_hex:
            binary_result.append('0')
            i += 6  # Move to the next character
        else:
            i += 2  # Move forward if no match found

    # Join the binary list into a single string
    binary_string = ''.join(binary_result)
    
    # Convert binary string to ASCII
    ascii_text = ''.join(chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8))

    # Write the ASCII text to the output file
    with open(output_file, 'w') as output:
        output.write(ascii_text)

    print(f"Decoded ASCII text has been written to {output_file}")

# Example usage
file_path = 'Stego100-2.txt'  # Replace with your actual file path
extract_binary_and_convert_to_ascii(file_path)
