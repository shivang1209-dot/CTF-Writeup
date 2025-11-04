## **Challenge Name: accessGranted**

### **Description**

We need to gain authenticated access to the web app, but we want to see if we can do it the way DEADFACE did. NVU admits they haven't fixed anything regarding their authentication process. See if you can login to the web app.

Submit the flag as deadface{flag text}.

**Note**: the application will present you with the flag once you login.

**Challenge URL**: `http://env01.deadface.io:8080`

---

### **Approach**

1. **Initial Reconnaissance**  
   - Accessed the login page at the challenge URL
   - Observed test accounts provided on the page:
     - Student: `jstudent` / `password123`
     - Faculty: `deephax` / `music4life`
   - Noted the hint: "Try different SQL injection techniques to access specific accounts..."

2. **SQL Injection Attempt**  
   - Attempted to bypass authentication using SQL injection in the username field
   - Used the classic SQL injection payload:
     ```
     admin' OR '1'='1
     ```
   - Successfully bypassed authentication and logged in as admin

3. **Retrieving the Flag**  
   - After successful login, the application displayed the admin dashboard with user information:
     ```
     Username: admin
     Email: admin@nvu.edu
     Role: admin
     Member Since: October 25, 2025
     Admin Access Granted!
     ```
   - The flag was displayed on the admin page

---

### **Flag**

```
deadface{sql_1nj3ct10n_byp4ss_4uth}
```

---

