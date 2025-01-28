from PIL import Image
import string

def extract_first_quantization_table_ascii_clean(image_path):
    img = Image.open(image_path)
    quant_tables = img.quantization

    # Extract only the first quantization table (ID 0)
    first_table = quant_tables.get(0, None)
    
    if first_table:
        result = []
        for value in first_table:
            # Convert to ASCII if it's a printable character
            if chr(value) in string.printable and not chr(value).isspace():
                result.append(chr(value))
        
        # Join the list into a clean string without spaces
        cleaned_output = ''.join(result)
        print(f"Flag: {cleaned_output}")
    else:
        print("No quantization table found with ID 0.")

# Path to your JPEG file
image_path = 'Stego400.jpg'
extract_first_quantization_table_ascii_clean(image_path)