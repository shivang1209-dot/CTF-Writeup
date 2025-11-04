## **Challenge Name: badBoy**

### **Description**

DEADFACE left this image on a victim's machine with a hidden message. See if you can discover the flag hidden in this image. Submit the flag as deadface{flag text}.

**File provided**: [baddestboi.png](baddestboi.png)

---

### **Approach**

1. **Initial File Analysis**  
   - Checked the file type using the `file` command:
     ```bash
     file baddestboi.png
     ```
     Result: PNG image data, 1024 x 1024, 8-bit/color RGB, non-interlaced

2. **Metadata Extraction**  
   - Used `exiftool` to examine image metadata:
     ```bash
     exiftool baddestboi.png
     ```
   - Found interesting information:
     - Author: `.syyntax`
     - Description: "an ugly derpy chihuahua in a hoodie..."
     - **Warning**: `[minor] Trailer data after PNG IEND chunk`
   - The warning indicated extra data after the PNG IEND chunk, suggesting hidden content

3. **Extracting Hidden Data**  
   - Used `zsteg` to extract hidden data from the PNG file:
     ```bash
     zsteg -a baddestboi.png
     ```
   - Output revealed:
     ```
     [?] 32 bytes of extra data after image end (IEND), offset = 0x1a7465
     extradata:0         .. text: "deadface{th3_b4dd3st_B0i_al1V3}\n"
     ```
   - The flag was found in the extra data after the PNG IEND chunk

---

### **Flag**

```
deadface{th3_b4dd3st_B0i_al1V3}
```

---

