## **Challenge Name: pestControl**

### **Description**

NVU has an API that we believe was leveraged by DEADFACE to gain configuration information that aided them in their attack on NVU's website. The API likely exposes sensitive information.

Submit the flag as deadface{flag text}.

**Challenge URL**: `http://env01.deadface.io:8080`

---

### **Approach**

1. **Finding API Endpoints**  
   - From the "consoleChaos" challenge, the browser console provided hints:
     ```
     Try: /api/debug.php?show=config
     Also check: /api/search.php?q=test&type=announcements
     ```

2. **Accessing Debug API**  
   - Visited the debug endpoint:
     ```
     http://env01.deadface.io:8080/api/debug.php?show=config
     ```
   - Received configuration data including the flag:
     ```json
     {
         "status": "success",
         "message": "Debug configuration retrieved",
         "data": {
             "app_version": "2.1.4",
             "php_version": "8.1.33",
             "server": "Apache\/2.4.65 (Debian)",
             "database": {
                 "host": "db",
                 "name": "nvu_portal",
                 "user": "nvu_user"
             },
             "flag": "deadface{4p1_d3bug_3xp0sur3_l34ks}",
             "paths": {
                 "root": "\/var\/www\/html",
                 "script": "\/var\/www\/html\/api\/debug.php"
             }
         }
     }
     ```

---

### **Flag**

```
deadface{4p1_d3bug_3xp0sur3_l34ks}
```

---

