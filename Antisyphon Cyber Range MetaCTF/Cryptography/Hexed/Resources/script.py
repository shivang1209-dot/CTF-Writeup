def hexdump_to_png(input_file, output_file):
    hex_data = ""
    
    # Read the hexdump file
    with open(input_file, 'r') as file:
        for line in file:
            # Extract characters from the 11th to the 50th (indices 10 to 50)
            hex_data += line[10:50].strip()
    
    # Remove all white spaces (if any remain)
    hex_data = hex_data.replace(" ", "").replace("\n", "")
    
    # Convert the hex string to binary
    binary_data = bytes.fromhex(hex_data)
    
    # Write the binary data to the output file
    with open(output_file, 'wb') as file:
        file.write(binary_data)

# File paths
input_file = 'hexed.png'
output_file = 'output.png'

# Convert hexdump to PNG
hexdump_to_png(input_file, output_file)
