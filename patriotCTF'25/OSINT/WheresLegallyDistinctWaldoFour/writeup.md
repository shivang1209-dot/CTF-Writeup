## **Challenge Name: Where's Legally Distinct Waldo Four**

### **Description**

Find the building where Waldo is. The flag is the building from which this photograph was taken. The full building name is the flag. Separate spaces with underscores.

The building name should have underscores instead of slashes or spaces.

"Apply eyeballs liberally to the image" - Challenge author Sid Kumar

This OSINT challenge has 10 maximum attempts.

---

### **Approach**

1. **Initial Analysis**  
   - Provided with a photograph
   - Need to identify the building from which the photo was taken
   - The challenge author's hint: "Apply eyeballs liberally to the image"
   - Note: Building name should use underscores instead of slashes or spaces

2. **Image Analysis**  
   - Examined the photograph for identifying features
   - Found clues pointing to **Freedom Park in Charlotte, North Carolina** (FP)
   - However, this was a misdirection

3. **Geolocation**  
   - Now, going back to this category it made sense to look around the same area we found the first 3 parts
   - We find a pond nearby
   - The image shows a theater or performance space
   - Identified various potential building names:
     - `pctf{Buchanan_Hall}`
     - `pctf{Mason_Building}`
     - `pctf{Center_for_the_Arts}`
     - `pctf{George_Mason_University_School_of_Dance}`
     - `pctf{Innovation_Hall}`
     - `pctf{TheaterSpace-George_Mason_University}`
     - `pctf{George_Mason_University_School_of_Music}`
     - `pctf{George_Mason_University_School_of_Theater}`
     - `pctf{Music_and_Theater_Building}`
     - `pctf{Center_for_the_Arts_College_of_Visual_and_Performing_Arts}`

4. **Identifying the Correct Building**  
   - After multiple attempts, found the correct building name
   - The building from which the photo was taken is: **Center for the Arts Concert Hall**
   - Formatted with underscores: `Center_for_the_Arts_Concert_Hall`

5. **Verification**  
   - Verified the perspective and visible landmarks match this location
   - Confirmed the identification is correct

---

### **Flag**

```
pctf{Center_for_the_Arts_Concert_Hall}
```

---

