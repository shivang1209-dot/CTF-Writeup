## **Challenge Name: stickToTheScript**

### **Description**

NVU thought they were being clever by obfuscating some of their code, but DEADFACE was able to figure it out. Despite this, NVU hasn't remediated the issue; we're pretty sure the secret they tried to hide in their code is still there - easily readable to anyone who sees it. Find the flag that is obfuscated in the web app's code.

Submit the flag as deadface{flag text}.

**Challenge URL**: `http://env01.deadface.io:8080`

---

### **Approach**

1. **Viewing Page Source**  
   - Visited the homepage and viewed the page source (Right-click → View Page Source)
   - Found a reference to `script.js`

2. **Examining JavaScript Files**  
   - Opened the JavaScript file: `http://env01.deadface.io:8080/script.js`
   - Examined the source code for obfuscated content

3. **Finding the Obfuscated Flag**  
   - Found a Base64-encoded string in a comment:
     ```javascript
     const config = {
         version: '2.1.4',
         buildDate: '2025-10-15',
         // ZGVhZGZhY2V7ajR2NHNjcjFwdF9jNG5faDFkM19zM2NyM3RzfQ==
         features: ['announcements', 'courses', 'research']
     };
     ```

4. **Decoding the Flag**  
   - Decoded the Base64 string: `ZGVhZGZhY2V7ajR2NHNjcjFwdF9jNG5faDFkM19zM2NyM3RzfQ==`
   - Result: `deadface{j4v4scr1pt_c4n_h1d3_s3cr3ts}`

---

### **Flag**

```
deadface{j4v4scr1pt_c4n_h1d3_s3cr3ts}
```

---

