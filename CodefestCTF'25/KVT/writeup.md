# Challenge Name: KVT

## Description  
**Geolocation Identification**  
Determine the precise coordinates of the photographer's position at Dashashwamedh Ghat, Varanasi, rounded to 4 decimal places.

![chall.png](Resources/chall.png)

**Flag Format**  
`CodefestCTF{latitude_longitude}`  

## Writeup

### Visual Recognition
1. Identified distinctive features:
   - Signature painted riverfront towers
   - Stone steps leading to Ganges
   - Pilgrim boats with ceremonial decorations

### Geolocation Process
1. Confirmed location via reverse image search as **Dashashwamedh Ghat**
2. Analyzed Google Street View panoramas:
   [Verification Link](https://www.google.com/maps/@25.3070687,83.0103974,3a,75y,46.04h,87.91t/data=!3m8!1e1!3m6!1sAF1QipNEVkJUOiBV0-b-tZJSna-Yg0zeQZgRa6Ypbi5T!2e10!3e11!6shttps:%2F%2Flh3.googleusercontent.com%2Fp%2FAF1QipNEVkJUOiBV0-b-tZJSna-Yg0zeQZgRa6Ypbi5T%3Dw900-h600-k-no-pi2.08815933242974-ya282.04355772306974-ro0-fo100!7i4608!8i2304?hl=en-GB&entry=ttu&g_ep=EgoyMDI1MDEyMi4wIKXMDSoASAFQAw%3D%3D)

### Coordinate Precision
- Raw coordinates:  
  `25.3070687° N, 83.0103974° E`
- Rounded to 4 decimals:  
  **25.3071° N, 83.0104° E**

## Flag  
`CodefestCTF{25.3071_83.0104}`  

---
