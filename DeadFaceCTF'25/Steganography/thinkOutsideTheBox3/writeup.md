## **Challenge Name: thinkOutsideTheBox3**

### **Description**

DEADFACE is taunting us again. After their latest attack, they left an image behind. The only problem is that the important information left behind seems to be missing from the image. Try to figure out what the chat bubble is supposed to say in the image.

Submit the flag as deadface{flag_text}.

**File provided**: [thinkoutsidethebox3.png](thinkoutsidethebox3.png)

---

### **Approach**

1. **Initial File Analysis**  
   - Checked the file type and metadata using `exiftool`:
     ```bash
     exiftool thinkoutsidethebox3.png
     ```
   - Found standard PNG metadata but nothing suspicious

2. **Steganography Analysis**  
   - Attempted to use `zsteg` to extract hidden data:
     ```bash
     zsteg -a thinkoutsidethebox3.png
     ```
   - Found some text but nothing useful:
     ```
     b2,r,msb,xy,prime   .. text: "*<\no2wf1<"
     b2,r,msb,Xy,prime   .. text: "\tw@0koc-"
     ```

3. **Steganography Tools**  
   - Used `stegsolve` (or similar steganography analysis tool)
   - Applied color inversion to reveal hidden content
   - The color inversion revealed the flag text in the chat bubble

---

### **Flag**

```
deadface{Th3_b0X_d0esnT_eX1st}
```

---

