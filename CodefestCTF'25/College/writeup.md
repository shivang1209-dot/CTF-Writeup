# Challenge Name: College

## Description   
Determine the exact coordinates of the landmark shown in the challenge image, rounded to 4 decimal places.  

**Flag Format**  
`CodefestCTF{latitude_longitude}`  

## Writeup

### Image Analysis
1. Performed reverse image search on `chall.png`  
2. Identified location as **Banaras Hindu University (BHU) Main Gate**  
3. Recognized statue of *Pandit Madan Mohan Malviya*  

### Coordinate Investigation
**Initial Attempt**  
- Approximate coordinates:  
  `25.2779283, 83.002355`  
  Rounded to: `25.2779_83.0023` *(Incorrect submission)*  

**Precision Adjustment**  
1. Used Google Street View verification:  
   [BHU Gate Coordinates](https://www.google.com/maps/@25.2779318,83.002362,3a,75y,212h,84.75t/data=!3m8!1e1!3m6!1sM_R-x5mPASf6pe7h1Q3c5Q!2e0!5s20230201T000000!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D5.245901286878464%26panoid%3DM_R-x5mPASf6pe7h1Q3c5Q%26yaw%3D212.00057284713597!7i13312!8i6656?entry=ttu&g_ep=EgoyMDI1MDEyMi4wIKXMDSoASAFQAw%3D%3D)  
2. Exact coordinates:  
   `25.2779318, 83.002362`  
3. Rounded to 4 decimals:  
   **Latitude:** 25.2779  
   **Longitude:** 83.0024  

## Flag  
`CodefestCTF{25.2779_83.0024}`  

---