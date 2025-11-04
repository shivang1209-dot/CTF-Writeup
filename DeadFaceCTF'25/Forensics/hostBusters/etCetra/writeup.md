## **Challenge Name: etCetra**

### **Description**

gh0st404 is complaining in Ghost Town about his script not working. See if you can locate the script on the remote machine and read the flag.

Submit the flag as deadface{flag_text}.

**Note**: Use the connection information from Hostbusters: Let Me In

---

### **Approach**

1. **Finding the Thread**  
   - Located the Ghost Town thread: `https://ghosttown.deadface.io/t/bruh-why-is-my-script-still-broken/93`
   - The thread mentioned:
     ```
     ok soooo i wrote this shell script to automate some log parsing junk right
     but when i try to run it, i keep getting Permission Denied
     i thought maybe i was in the wrong folder or something, so i just moved it into /etc/ cause that felt official or whatever
     BUT IT STILL DENIED ME :sob:
     ```

2. **SSH Connection**  
   - Connected to the remote machine using credentials from "letMeIn":
     ```bash
     ssh hostbusters.deadface.io -l gh0st404
     ```
   - Password: `ReadySetG0!`

3. **Locating the Script**  
   - Enumerated the `/etc/` directory:
     ```bash
     ls -la /etc/
     ```
   - Found the script: `logclean.sh`
   - The permissions showed: `----------` (no permissions for anyone)

4. **Reading the Script**  
   - Attempted to read the script:
     ```bash
     cat /etc/logclean.sh
     ```
   - Received: `Permission denied`
   - Changed permissions to allow reading:
     ```bash
     chmod 777 /etc/logclean.sh
     ```
   - Read the script contents:
     ```bash
     cat /etc/logclean.sh
     ```
   - The flag was at the end of the script

---

### **Flag**

```
deadface{hostbusters3_0547796725934bbd}
```

---

