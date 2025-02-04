## **Challenge Name: Project-153-Q5**

### **Description**

Maboi 💪: Bruh, the name of the mountain where I was lmao 🧠.  
Flag format: ectf{Name_of_the_Place} (in French)

---

### **Approach**

1. **Image Analysis**  
   - The image is a panorama, and after extracting the metadata with `exiftool`, we see it's a **JPEG** file taken with a **Mi 9T** camera on **2022:04:08**. The file size is large (31 MB), and the image resolution is **13776x3712**, indicating it's a high-quality panoramic shot.

2. **Date of Image**  
   - The date of the photo (**2022:04:08**) provides a clue that may help narrow down location data or associated events.

3. **Further Research**  
   - Researching the **Pointe du Cerveau** and related names leads to the identification of the location: **Le Gros Cerveau**.

4. **Final Solution**  
   - The name of the mountain in French is **Gros Cerveau**, and the flag is formatted as:

   ```
   ectf{Gros-Cerveau}
   ```

---

### **Flag**

`ectf{Gros-Cerveau}`

---