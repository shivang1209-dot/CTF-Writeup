## **Challenge Name: Project-153-Q6**

### **Description**

Thomas Yatangaki: unfortunately, it's not part of project 153, but it's still very beautiful here 😻.  
Maboi 💪: How many steps were there again?  
Flag format: ectf{number_zipcodeofthetown}

---

### **Approach**

1. **Image Metadata Analysis**  
   - The metadata reveals that the image is a **JPEG** file, with a resolution of **4000x3000** and a size of **788 KB**. The file was created on **2025:01:31**.

2. **Image Context**  
   - Upon examining the image, we can identify that it is related to the **Chapel of Notre-Dame de Beauvoir**.

3. **Number of Steps**  
   - Researching the **Chapel of Notre-Dame de Beauvoir** reveals that it is accessed by **262 steps** up the Way of the Cross. 

4. **Location Search**  
   - The chapel is located in **Moustiers-Sainte-Marie**, France. The **zip code** for the town is **04360**.

[Chapel](Resources/image1.png)

5. **Final Solution**  
   - The flag is a combination of the number of steps (262) and the zip code (04360), formatted as:

   ```
   ectf{262_04360}
   ```

---

### **Flag**

`ectf{262_04360}`

---