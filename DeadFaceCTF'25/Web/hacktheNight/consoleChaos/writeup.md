## **Challenge Name: consoleChaos**

### **Description**

Let's make sure NVU cleaned up some of the comments in their codebase. We don't need them publicizing information that would help tip off DEADFACE. Use built-in browser tools to find any flags that we might have missed so far.

Submit the flag as deadface{text}.

**Challenge URL**: `http://env01.deadface.io:8080`

---

### **Approach**

1. **Accessing the Web Application**  
   - Visited the URL: `http://env01.deadface.io:8080`
   - Opened the browser's Developer Tools (F12 or right-click → Inspect)

2. **Checking the Console**  
   - As the challenge name suggests "consoleChaos", opened the browser console tab
   - Found console logs containing the flag:
     ```
     deadface{c0ns0l3_l0gs_4r3_y0ur_fr13nd}
     ```

---

### **Flag**

```
deadface{c0ns0l3_l0gs_4r3_y0ur_fr13nd}
```

---

