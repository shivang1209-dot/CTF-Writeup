## **Challenge Name: waffWaff**

### **Description**

Mirveal is keeping his shenanigans Doxing people around the world. Now we need to find the location of a person that Mirvael compromised his phone.

Enter the answer as deadface{Country_City_Street}.

**File provided**: [puppets.jpg](puppets.jpg)

---

### **Approach**

1. **Initial Image Analysis**  
   - Examined the image metadata using `exiftool`:
     ```bash
     exiftool puppets.jpg
     ```
   - Found only the modify date: `2018:08:06 06:49:27`
   - No GPS coordinates in the EXIF data

2. **Image Content Analysis**  
   - Analyzed the image content:
     - Text in Portuguese: "CUIDADO COM O ROTWEILER" (BEWARE OF THE ROTWEILER)
     - The product is a Ty Beanie Baby named Brutus, a plush Rottweiler dog
   - Mirrored the image to see the shop/building in the background

3. **Text Identification**  
   - The text "Sit-in" was visible on a sign in the background
   - The name at the top was cut off
   - Found a Ty logo, which is the logo for Ty Beanie Baby products

4. **Location Identification**  
   - The text on the top seemed to be from Rottweil, Germany
   - Identified the street name: **Oberamteigasse**
   - Confirmed the location: Rottweil, Germany

---

### **Flag**

```
deadface{Germany_Rottweil_Oberamteigasse}
```

---

