### **Challenge Name: Stego 300 - Everything and Nothing**

---

### **Description**

This challenge revolves around a steganography puzzle in a grayscale PNG image. The task is to extract hidden information concealed within the image's data. It leverages techniques often used in stego challenges, requiring knowledge of file structure and specialized tools to uncover the embedded flag.

---

### **Approach**

#### **Step 1: Initial Inspection**
- **File Command**:
  ```bash
  file Stego300-2.png
  ```
  Output:
  ```
  Stego300-2.png: PNG image data, 1024 x 1024, 8-bit/color RGBA, non-interlaced
  ```

  This confirms it is a valid PNG file with RGBA channels.

- **EXIF Metadata**:
  Using `exiftool` to inspect for hidden metadata:
  ```bash
  exiftool Stego300-2.png
  ```
  Key Output:
  ```
  File Type: PNG
  Image Size: 1024x1024
  Color Type: RGB with Alpha
  Compression: Deflate/Inflate
  ```

  No unusual metadata or embedded comments were observed in the EXIF data.

#### **Step 2: Steganography Analysis**
- **Tool Used: `zsteg`**:
  This tool checks for hidden data in PNG images by examining different bitplanes and encodings.

  Command:
  ```bash
  zsteg Stego300-2.png
  ```
  Key Output:
  ```
  b1,r,lsb,xy         .. text: "poctf{uwsp_n07_4ll_7h053_wh0_w4nd3r}"
  ```

  The flag is embedded in the least significant bit (LSB) of the red channel.

#### **Step 3: Verify the Flag**
- Extracted flag:
  ```
  poctf{uwsp_n07_4ll_7h053_wh0_w4nd3r}
  ```

---

### **Flag**

`poctf{uwsp_n07_4ll_7h053_wh0_w4nd3r}`

---