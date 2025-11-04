## **Challenge Name: theSourceOfOurTroubles**

### **Description**

DEADFACE compromised Night Veil University's student portal website. NVU swears up and down that they've secured the site, but the school leaderships wants us to validate that their site is no longer vulnerable. DEADFACE left several artifacts throughout the web app to taunt school staff. See if you can compromise the web app and find the artifacts left behind by DEADFACE.

Let's start by finding any artifacts on NVU's homepage at http://env01.deadface.io:8080. NVU has graciously provided us with their System Design Document that includes information about the application and its intended behavior. Use these documents to facilitate your activities.

**Challenge URL**: `http://env01.deadface.io:8080`

---

### **Approach**

1. **Accessing the Homepage**  
   - Visited the URL: `http://env01.deadface.io:8080`
   - Examined the page for any visible artifacts

2. **Viewing Page Source**  
   - Opened the browser's Developer Tools (F12)
   - Viewed the page source (Right-click → View Page Source)

3. **Finding the Flag in Comments**  
   - Scrolled through the HTML source code
   - Found the flag in HTML comments:
     ```html
     <!-- deadface{v13w_s0urc3_4lw4ys_f1rst} -->
     ```

---

### **Flag**

```
deadface{v13w_s0urc3_4lw4ys_f1rst}
```

---

