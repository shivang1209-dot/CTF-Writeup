## **Challenge Name: letMeIn**

### **Description**

Due to the efforts of the Turbo Tactical team, we've managed to acquire credentials belonging to gh0st404 that can be used on a remote DEADFACE machine. Access this machine and find the flag in the user's home directory.

Submit the flag as deadface{flag_text}

**Connection Information**:
- IP Address: `hostbusters.deadface.io`
- Username: `gh0st404`
- Password: `ReadySetG0!`

---

### **Approach**

1. **Network Reconnaissance**  
   - Started with `nmap` to identify open services on the target:
     ```bash
     nmap hostbusters.deadface.io
     ```
   - Found open ports:
     - `21/tcp` - FTP
     - `22/tcp` - SSH
     - `554/tcp` - RTSP
     - `1723/tcp` - PPTP

2. **SSH Connection**  
   - Connected to the remote machine via SSH:
     ```bash
     ssh hostbusters.deadface.io -l gh0st404
     ```
   - Entered the password: `ReadySetG0!`
   - Successfully authenticated and gained access

3. **Finding the Flag**  
   - Listed files in the home directory:
     ```bash
     ls
     ```
   - Found `notes.txt` and a `tools` directory
   - Read the `notes.txt` file:
     ```bash
     cat notes.txt
     ```
   - The flag was located at the end of the notes file

---

### **Flag**

```
deadface{hostbusters1_cf6a12ddf781cfbc}
```

---

