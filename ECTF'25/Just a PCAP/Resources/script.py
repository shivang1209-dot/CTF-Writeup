with open("extracted_data.txt", "r") as f:
    hex_data = "".join(f.read().split())  # Remove spaces, newlines, etc.

# Convert hex to binary data
binary_data = bytes.fromhex(hex_data)

# Save as a PNG file
with open("flag.png", "wb") as img_file:
    img_file.write(binary_data)

print("Image successfully recovered as 'flag.png'")
