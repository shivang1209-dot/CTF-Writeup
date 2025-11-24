## **Challenge Name: Where's Legally Distinct Waldo Two**

### **Description**

Find the building where Waldo is. The flag is the building from which this photograph was taken. The full building name is the flag. Separate spaces with underscores.

"Apply eyeballs liberally to the image" - Challenge author Sid Kumar

This OSINT challenge has 10 maximum attempts.

---

### **Approach**

1. **Initial Analysis**  
   - Provided with a photograph
   - Need to identify the building from which the photo was taken
   - The challenge author's hint: "Apply eyeballs liberally to the image"

2. **Image Analysis**  
   - Examined the photograph for identifying features
   - Found a vehicle with text: **"Reston limousine"**
   - Identified surrounding buildings:
     - To the left: **Rogers Hall**
     - To the right: **Peterson Family Health Sciences Hall**

3. **Geolocation**  
   - The building names suggest George Mason University campus
   - Analyzed the perspective and angle of the shot

4. **Identifying the Building**  
   - Based on the visible landmarks and perspective:
     - The building to the left is Rogers Hall
     - The building to the right is Peterson Family Health Sciences Hall
     - The shooting location appears to be **Thompson Hall**

5. **Verification**  
   - Verified the angle and perspective match Thompson Hall's location
   - Confirmed the visible landmarks align with this identification

---

### **Flag**

```
pctf{Thompson_Hall}
```

---

