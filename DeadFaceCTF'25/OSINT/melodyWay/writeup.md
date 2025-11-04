## **Challenge Name: melodyWay**

### **Description**

Tilon is a mysterious figure who enjoys his poetic life. Mirveal has discovered an image from one of Tilon's trips. Apperently he goes often there. Now all that's left is to get the name of the building.

Flag format: DEADFACE{building_name_across_the_road}

**Files provided**: 
- [OSINT05_-_Melody_Way.jpg](OSINT05_-_Melody_Way.jpg)
- [imgi_84_20250710_191953.jpg](imgi_84_20250710_191953.jpg)

---

### **Approach**

1. **Initial Image Analysis**  
   - Examined the image metadata using `exiftool`:
     ```bash
     exiftool OSINT05_-_Melody_Way.jpg
     ```
   - Found standard image metadata but no GPS coordinates in the EXIF data
   - The image showed a street scene with Korean text visible

2. **Image Content Analysis**  
   - Performed static analysis of the image
   - Identified Korean text on a standee that translates to: `Paris Baguette`
   - This provided a clue about the location

3. **Reverse Image Search**  
   - Performed reverse Google image search on the image
   - Found a blog post: `https://blog.naver.com/PostView.nhn?blogId=cyberseller&logNo=223933686981`
   - The blog mentioned: "The place is a 5 minute walk from the Exit 1 of Sindorm Station"

4. **Locating the Building**  
   - Found another article: `https://m.blog.naver.com/dlaldus5244/222882134082`
   - The article mentioned: "Mapo Jokbal Sundaeguk is locate on the first floor of the Prugio building right infront of the Sindorim Station"
   - Also identified another shop: "24 hours Fruit OROT"

5. **Finding the Exact Location**  
   - Located the area on Google Maps near Sindorim Station
   - Found the exact location: `https://www.google.com/maps/place/Homeplus+Sindorim/@37.509204,126.888077`
   - Identified the building across the road: **D-CUBE CITY**

---

### **Flag**

```
DEADFACE{D-CUBE_CITY}
```

---

