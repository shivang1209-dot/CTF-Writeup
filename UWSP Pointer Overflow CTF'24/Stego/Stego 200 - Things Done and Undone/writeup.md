## **Challenge Name: Stego 200 - Things Done and Undone**  

---

### **Description**  

You know, I can't help but feel like the Stego challenges have been missing something. Like, it's almost as if several of the challenges contained clues that hinted that a certain method was employed, and then it turns out that they actual indicated some other method. It's honestly starting to bother me. It's like knowing that something is just a little bit off but not being able to identify it. Like there's unfinished business to tend to. I normally wouldn't let something so insignificant bother me, but I just can't leave things undone like this.

**Files Provided:**  
[Stego200-3.png](Resources/Stego200-3.png) 

---

### **Approach**  

1. **File Inspection**:  
   - Checked file type to ensure it’s a valid PNG:  
     ```bash  
     ┌──(kali㉿kali)-[~/Desktop/poctf/stego]  
     └─$ file Stego200-3.png  
     Stego200-3.png: PNG image data, 1024 x 1024, 8-bit/color RGB, non-interlaced  
     ```  

2. **Metadata Check**:  
   - Extracted metadata using `exiftool`, but found nothing significant:  
     ```bash  
     ┌──(kali㉿kali)-[~/Desktop/poctf/stego]  
     └─$ exiftool Stego200-3.png  
     File Name                       : Stego200-3.png  
     File Size                       : 2.0 MB  
     Image Width                     : 1024  
     Image Height                    : 1024  
     Bit Depth                       : 8  
     Color Type                      : RGB  
     ...  
     ```  

3. **Steganography Analysis with `zsteg`**:  
   - Ran `zsteg` to analyze hidden data layers within the PNG:  
     ```bash  
     ┌──(kali㉿kali)-[~/Desktop/poctf/stego]  
     └─$ zsteg Stego200-3.png  
     imagedata           .. text: "=83XZJ$\""  
     b1,r,msb,xy         .. text: "S`\trQlmU1"  
     b1,g,lsb,xy         .. file: OpenPGP Public Key  
     b1,g,msb,xy         .. file: OpenPGP Public Key  
     b1,rgb,lsb,xy       .. text: "poctf{uwsp_70_b3_0r_n07_70_b3}"  
     ```  

4. **Flag Extraction**:  
   - The flag was embedded in the RGB LSB channel (`b1,rgb,lsb,xy`).  
   - Directly extracted the flag:  
     ```
     poctf{uwsp_70_b3_0r_n07_70_b3}  
     ```  

---

### **Flag**  

`poctf{uwsp_70_b3_0r_n07_70_b3}`  

---  