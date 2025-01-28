## **Challenge Name: Stego 100 - Things Seen and Unseen**  

---

### **Description**  

One of my first jobs in cybersecurity was at a major retailer in the USA. A multi-billion dollar, Fortune 500, international corporation. You'd think a business like that would have all kinds of resources invested in IT, but that wasn't the case.

The whole company hinged on an inventory system. If it went down, the company would immediately start treading water. This inventory system was released in 1986 and was written in Cobol. The original programmers were kept on retainer to handle problems when they cropped up, and these people were well into their golden years.

By the time I came around, there were only three of them left, and only two of those had worked on the most important portions of the program. The last one only did code reviews on the least significant bits, and even he was part of the eternal work of maintaining this single program!

I asked DALL-E to whip up a representation of the lengths the company would go through to avoid change. Enjoy!

**Image Provided:**  
![Stego100-1.png](Resources/Stego100-1.png)

---

### **Approach**  

The challenge involves extracting a hidden message (flag) embedded in the PNG image, which is a typical steganography task. For this, I used the `zsteg` tool, a great utility for solving PNG stego challenges.

1. **Run `zsteg` on the provided image**:  
   I ran the following command to analyze the image for any hidden messages:

   ```
   zsteg -a Stego100-1.png
   ```

2. **Examine the Output**:  
   The tool outputs the following:

   ```
   b1,g,lsb,xy         .. file: OpenPGP Public Key
   b1,g,msb,xy         .. file: OpenPGP Public Key
   b1,rgb,lsb,xy       .. text: "poctf{uwsp_wh47_15_d34d_m4y_n3v3r_d13}"
   ```

3. **Flag Extraction**:  
   The relevant line here is:

   ```
   b1,rgb,lsb,xy       .. text: "poctf{uwsp_wh47_15_d34d_m4y_n3v3r_d13}"
   ```

   This indicates that the flag is hidden in the least significant bit (LSB) of the red-green-blue (RGB) channels of the image. The flag is:

   **`poctf{uwsp_wh47_15_d34d_m4y_n3v3r_d13}`**

---

### **Flag**  

`poctf{uwsp_wh47_15_d34d_m4y_n3v3r_d13}`