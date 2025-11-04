## **Challenge Name: potOfGreed**

### **Description**

We got a report from a law firm on the east coast that one of Turbo Tactical's laptops was hacked. Based on what we heard on the call, it sounds like DEADFACE. The team is paranoid now and needs to figure out where this attack occurred. Can you use your detective skills and see if DEADFACE has mentioned anything about a specific location that they executed their attack from.

Enter the answer as deadface{Business_Name}.

**File provided**: [0563700f72ae4c89a9f7ff4c658cae3731f33237.jpeg](0563700f72ae4c89a9f7ff4c658cae3731f33237.jpeg)

---

### **Approach**

1. **Finding the Thread**  
   - Searched the Ghost Town message board for relevant threads
   - Found the thread: `https://ghosttown.deadface.io/t/how-we-re-going-to-gut-turbo-tactical/80`
   - Located an image in the last comment (comment #7) with a message about a coffee shop

2. **Image Analysis**  
   - Examined the image metadata using `exiftool`:
     ```bash
     exiftool 0563700f72ae4c89a9f7ff4c658cae3731f33237.jpeg
     ```
   - Found no GPS coordinates in the EXIF data
   - The image showed a street corner with a sign visible

3. **Image Content Analysis**  
   - Analyzed the image content:
     - A board on the top left says `DC Capitol Hill` & `2 ND Street`
     - This indicated the location is in Washington D.C., near Capitol Hill on 2nd Street
   - The text mentioned finding a coffee shop on this corner

4. **Locating the Coffee Shop**  
   - Searched for coffee shops on 2nd Street near Capitol Hill in Washington D.C.
   - Examined every crossroad on 2nd Street using Google Maps
   - Found the location: `https://www.google.com/maps/@38.8973627,-77.0033061`
   - Identified the coffee shop: **Ebenezers**

---

### **Flag**

```
deadface{ebenezers}
```

---

