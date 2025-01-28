## **Challenge Name: Reverse 400 - Forjeskit Sair with Weary Legs**  

---

### **Description**  

Aye, gather around, ye codin' minds,  
A challenge waits, its path entwined.  
"In Forjeskit Sair," the whispers say,  
With weary legs, ye find yer way.  

#### **File Provided**  
- [Reverse400.exe](Resources/Reverse400.exe)  

---

### **Approach**  

Upon running the provided Windows binary, it prints the following encrypted flag to the command-line output:  
`bd7e9dad4a5fe0e7911f93cb1bf5a321`.

This binary is packed using PyInstaller, a tool that bundles Python programs into standalone executables. The next step is to unpack the binary and extract the Python code to examine it.

**1. Extract the Contents:**
To extract the contents of the binary, I used [pyinstxtractor](https://github.com/extremecoders-re/pyinstxtractor). After extracting, I found a file called `Reverse400.pyc` which contains the bytecode of the original Python script.

**2. Decompile the Bytecode:**
I used the [pycdc](https://github.com/zrax/pycdc) decompiler to turn the `.pyc` file back into readable Python code. The decompiled script is obfuscated, so I used a manual deobfuscation method to make it more understandable.

The deobfuscated Python code looked something like this:

```python
pyobfuscate = lambda getattr: [(lambda IIlII, IlIIl: setattr(__builtins__, IIlII, IlIIl))(IIlII, IlIIl) for IIlII, IlIIl in getattr.items()]
Il = chr(114)
lI = '[^a-zA-Z0-9]'
lIl = chr(115) * chr(117) / chr(98)
lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllIIllIIlI = (__import__, getattr, bytes, exec)
__import__('sys').setrecursionlimit(100000000)
```

This code was clearly obfuscated, so to deal with it, I used tools like `pydeobfuscator` or `pyarmor` for some assistance. However, I also needed to do some manual adjustments to reveal the underlying logic.

**3. Analyze the Key Operations:**
Upon analysis, the script performed the following operations:

- **XOR Operation:** A byte-by-byte XOR operation with the value `42` was used on the data.
- **Transformation Function:** A bit-shift transformation based on a provided key and IV (Initialization Vector) was applied to each byte.
- **AES Decryption:** The encrypted data was decrypted using the AES algorithm in CBC mode with a 16-byte key and a 32-byte IV.
- **Final Processing:** After AES decryption, the processed data went through the XOR operation again.

**4. The AES Decryption Setup:**
I located the encrypted flag (`fa21c9c2596099915dbc7845c941c14e81594b5c4f69177cc4059da11e782e0b`), the decryption key (`504f43544632303234`), and the IV (`437261636b3430302d58`) in the script. The key and IV are provided in hexadecimal format.

**5. Implement the Decryption Process:**
I implemented the AES decryption and transformation logic in Python as follows:

```python
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
```

**6. Obtain the Flag:**
Upon running the decryption process, the final result returned the flag:  

**`poctf{uwsp_4ll_7h47_gl1773r5}`**

---

### **Flag**  

`poctf{uwsp_4ll_7h47_gl1773r5}` 