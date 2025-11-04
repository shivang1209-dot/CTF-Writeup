## **Challenge Name: secretStash**

### **Description**

Look around for files that gh0st404 might have hidden - he's a novice DEADFACE member so we suspect he probably hides files in the simplest way.

Submit the flag as deadface{flag_text}.

**Note**: Use the connection information from Hostbusters: Let Me In

---

### **Approach**

1. **SSH Connection**  
   - Connected to the remote machine using credentials from "letMeIn":
     ```bash
     ssh hostbusters.deadface.io -l gh0st404
     ```
   - Password: `ReadySetG0!`

2. **Finding Hidden Files**  
   - The most novice method to hide files in Linux is adding a `.` prefix
   - Listed all files including hidden ones:
     ```bash
     ls -la
     ```
   - Found hidden files:
     - `.ash_history`
     - `.dont_forget`

3. **Reading the Hidden File**  
   - Read the `.dont_forget` file:
     ```bash
     cat .dont_forget
     ```
   - The file contained:
     ```
     random junk, don't lose this file (again)
     
     [personal]
     Gh0st!v3r$e_404
     0nly_Sh4d0w_Kn0ws
     n0scopez420!
     
     [tools]
     - burp:         waf_slayer$$
     - metasploit:   c0d3BReaKer!
     - vpn (alt):    4sh3s2dust_
     
     [misc]
     - music:      s1lent_echoes
     - github:       b4ckd00rRabb1t
     - deephax pen: Fr4gm3ntedSkull!!
     
     # note to self: change the pen one (again)
     
     deadface{hostbusters2_4685d0c801939781}
     ```
   - The flag was at the end of the file

---

### **Flag**

```
deadface{hostbusters2_4685d0c801939781}
```

---

