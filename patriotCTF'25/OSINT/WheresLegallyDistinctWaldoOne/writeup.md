## **Challenge Name: Where's Legally Distinct Waldo One**

### **Description**

Find the building where Waldo is. The flag is the building from which this photograph was taken. The full building name is the flag wrapped in pctf{...}. For example: pctf{Burger_House}

Separate spaces with underscores.

"Apply eyeballs liberally to the image" - Challenge author Sid Kumar

This OSINT challenge has 10 maximum attempts.

---

### **Approach**

1. **Initial Analysis**  
   - Provided with a photograph
   - Need to identify the building from which the photo was taken
   - The challenge author's hint: "Apply eyeballs liberally to the image"

2. **Image Analysis**  
   - Using Reverse Image Lookup we can confirm it's George Mason University.

3. **Identifying the Target Building**  
   - The photo shows a tower and other buildings
   - Analyzed the angle and perspective to determine the shooting location
   - Identified landmarks visible in the image:
     - David King Hall (the building being photographed)
     - Other surrounding structures

4. **Determining the Shooting Location**  
   - Used geolocation techniques to find the exact building
   - Found coordinates: `38.83143, -77.3079745`
   - Identified the building as: **Horizon Hall**

5. **Verification**  
   - Verified the angle matches the perspective in the photo
   - Confirmed landmarks align with the identified location
   - The building name matches the visible features

---

### **Flag**

```
pctf{Horizon_Hall}
```

---

