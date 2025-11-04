## **Challenge Name: sqLite007**

### **Description**

DEADFACE is taunting us! We found their link! There was a breach!. How deep, and how for heaven's sakes did they got in, we don't know! Can you locate the flag?

Submit the flag as `deadface{text}`.

**Challenge URL**: [https://deadface-db01.chals.io](https://deadface-db01.chals.io)

---

### **Approach**

1. **Initial Reconnaissance**  
   - Accessed the login page at the challenge URL
   - Encountered an authentication page with no valid credentials
   - Attempted basic SQL injection techniques to bypass authentication

2. **Authentication Bypass**  
   - Tried the classic SQL injection payload: `admin' OR '1'='1`
   - Successfully bypassed authentication and gained access to the admin dashboard
   - Alternative payload that also worked: `admin' OR 1=1 --`

3. **Exploring the Dashboard**  
   - Found a search functionality with three database options:
     - Activity Logs
     - API Keys
     - Profiles
   - Initial search queries failed with SQL syntax errors: `near "%": syntax error`
   - Realized the search parameter was vulnerable to SQL injection

4. **Enumerating Database Schema**  
   - Used UNION-based SQL injection to extract table names from `sqlite_master`:
     ```
     ' UNION SELECT NULL,NULL,NULL,group_concat(name,','),NULL FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'--
     ```
   - Discovered the following tables:
     - `general`
     - `profiles`
     - `sessions`
     - `api_keys`
     - `activity_logs`

5. **Finding the Flag Table**  
   - Inspected each table's structure using `PRAGMA table_info()`:
     ```
     ' UNION SELECT NULL,NULL,NULL,group_concat(name,','),NULL FROM pragma_table_info('general')--
     ```
   - Found that the `general` table contains a `flag` column

6. **Extracting the Flag**  
   - Executed the final SQL injection to retrieve the flag:
     ```
     ' UNION SELECT NULL,NULL,NULL,group_concat(CAST(flag AS TEXT),','),NULL FROM general--
     ```
   - Successfully extracted the flag from the database

---

### **Flag**

`DEADFACE{you_found_the_sqli_01_flag!}`

---

