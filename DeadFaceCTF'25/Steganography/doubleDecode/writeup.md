## **Challenge Name: doubleDecode**

### **Description**

While doing forensics after a recent DEADFACE attack, the team found a file that was added to the system called qr_flag.png. Nothing seems wrong with the file, but we are sure Deadface is doing something with it. Can you figure out how this file has been modified and reveal the hidden secrets?

Submit the flag as deadface{flag_text}.

**File provided**: [qr_flag.png](qr_flag.png)

---

### **Approach**

1. **Initial File Analysis**  
   - Checked the file type and metadata using `exiftool`:
     ```bash
     exiftool qr_flag.png
     ```
   - Found a warning: `[minor] Trailer data after PNG IEND chunk`
   - This indicated extra data after the PNG image end marker

2. **Extracting Hidden Data**  
   - Used `zsteg` to extract hidden data:
     ```bash
     zsteg -a qr_flag.png
     ```
   - Found Base64-encoded data in the trailer:
     ```
     [?] 187 bytes of extra data after image end (IEND), offset = 0x24b
     extradata:0         .. text: "\n#df#\nIyBwYXlsb2FkLnB5CgpkYXRhID0gIjY0IDY1IDYxIDY0IDY2IDYxIDYzIDY1IDdiIDQ1IDVhIDcwIDZlIDY3IDQ4IDMxIDY0IDMxIDZlIDY3IDdkIgoKZmxhZyA9IGJ5dGVzLmZyb21oZXgoZGF0YSkuZGVjb2RlKCkKcHJpbnQoZmxhZykK\n"
     ```

3. **Decoding Base64**  
   - Decoded the Base64 string to reveal Python code:
     ```python
     # payload.py
     
     data = "64 65 61 64 66 61 63 65 7b 45 5a 70 6e 67 48 31 64 31 6e 67 7d"
     
     flag = bytes.fromhex(data).decode()
     print(flag)
     ```

4. **Hex Decoding**  
   - Decoded the hexadecimal string `64 65 61 64 66 61 63 65 7b 45 5a 70 6e 67 48 31 64 31 6e 67 7d`
   - Converted from hex to ASCII to get the flag

---

### **Flag**

```
deadface{EZpngH1d1ng}
```

---

