## **Challenge Name: Project-153-Q4**

### **Description**

Thomas Yatangaki: Bro, I think, we did the gr90 the wrong way round.  
Maboi 💪: damn 💀 At least, the view was better at the end.  
Wait, do you see the place in the background in the middle? We've got to get over there, what's the name?  
Thomas Yatangaki: No I don't think we should 💀.  
Flag format: ectf{Name_of_the_Place} (in French)

**Files:**  
[OSINT_1_-_question-4.zip](Resources/OSINT_1_-_question-4.zip)

---

### **Approach**

1. **Observation**  
   - The challenge involves identifying the place shown in the background of the image.
   - The flag format requires the name of the place in French.

2. **Initial Analysis**  
   - The image file is analyzed using the `file` and `exiftool` commands, but no additional information from EXIF metadata provides a clue about the location.
   - The clue lies in the phrase **"gr90"** and the background "in the middle."

3. **Reverse Image Search**  
   - A **reverse image search** leads to the discovery of the location: **Chapelle Notre-Dame de Constance**.

4. **Exploration on the Map**  
   - Upon zooming out on the map for **Chapelle Notre-Dame de Constance**, two islands are visible that match the islands in the image.
   - The longer island is the one we're looking for, which is **Île du Levant**.

5. **Final Solution**  
   - The name of the place in French is **Île du Levant**, and the flag is formatted as:

   ```
   ectf{Île_du_Levant}
   ```

---

### **Flag**

`ectf{Île_du_Levant}`

---