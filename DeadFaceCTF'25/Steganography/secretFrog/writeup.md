## **Challenge Name: secretFrog**

### **Description**

DEADFACE left behind this strange image of a frog with the message:

"The frog has many secrets, but he'll only tell you if you make him smile."

There's obviously more to this image than we can see here. Figure out if you can find the flag associated with this image. Submit the flag as deadface{flag text}.

**Files provided**: 
- [froggy-steg.png](froggy-steg.png)
- [00002389.gif](00002389.gif)

---

### **Approach**

1. **Initial File Analysis**  
   - Checked the file type and metadata using `exiftool`:
     ```bash
     exiftool froggy-steg.png
     ```
   - Found a warning: `[minor] Trailer data after PNG IEND chunk`
   - This indicated extra data after the PNG image end marker

2. **Extracting Hidden Data**  
   - Used `zsteg` to extract hidden data:
     ```bash
     zsteg -a froggy-steg.png
     ```
   - Found a large amount of extra data (4500207 bytes) after the PNG IEND chunk
   - Detected a GIF file embedded in the extra data:
     ```
     extradata:0         .. file: GIF image data, version 89a, 461 x 461
     ```

3. **Extracting the GIF**  
   - Used `binwalk` or `foremost` to extract the embedded GIF:
     ```bash
     binwalk -e froggy-steg.png
     ```
   - Or:
     ```bash
     foremost froggy-steg.png
     ```
   - Extracted the GIF file: `00002389.gif`

4. **Fixing the GIF**  
   - The extracted GIF was corrupted
   - Used a hex editor (like `hexed.it`) to patch the GIF file
   - Opened the patched GIF to reveal the smiling frog with the flag

---

### **Flag**

```
deadface{sm1l3_4nd_th3_w0rld_sm1l3s_w1th_y0u}
```

---

