## **Challenge Name: Reverse Metadata Part 1**

### **Description**

This server processes uploaded images and reads their metadata every few minutes. But… something feels off. Our analysts suspect a hidden vulnerability in how the metadata is handled. Can you investigate the system and uncover the flaw?

**Challenge author**: _itzamn

**Challenge URL**: `http://18.212.136.134:9090/`

**Tip**: Exiftool

---

### **Approach**

1. **Initial Investigation**  
   - Accessed the challenge URL and found an image upload service
   - The description mentions metadata processing, suggesting ExifTool vulnerability
   - The tip explicitly mentions ExifTool

2. **Identifying the Vulnerability**  
   - This challenge exploits **CVE-2021-22204**, a critical RCE vulnerability in ExifTool
   - ExifTool versions 7.44 through 12.23 are vulnerable
   - The vulnerability allows arbitrary code execution when processing malicious image metadata

3. **Understanding the Attack Vector**  
   - ExifTool improperly neutralizes user data in the DjVu file format
   - We can embed malicious Perl code through embedded metadata
   - When ExifTool reads the metadata, it executes the embedded Perl code

4. **Creating the Exploit**  
   - Used an exploit script to create a malicious image:
     ```bash
     python3 exploit.py -c "cat /flag.txt > /var/www/html/flag_output.txt"
     ```
   - The exploit:
     - Creates a Perl payload: `(metadata "\c${system('command')};")`
     - Compresses it using `bzz` (DjVu compression)
     - Embeds it in a DjVu file using `djvumake`
     - Injects the DjVu file into a JPEG image's metadata using ExifTool
     - Uploads the malicious image to the server

5. **Executing the Exploit**  
   - Uploaded the malicious image to the server
   - Waited for the server to process it (runs every few minutes)
   - Initially tried to read `/flag.txt` but it was empty
   - Listed files to find the correct flag location:
     ```bash
     python3 exploit.py -c "ls -la / > /var/www/html/ls_out.txt"
     ```
   - Found a `/flags` directory

6. **Reading the Flag**  
   - Listed contents of `/flags`:
     ```bash
     python3 exploit.py -c "ls -la /flags > /var/www/html/flags_out.txt"
     ```
   - Found `root.txt` in `/flags` directory
   - Read the flag:
     ```bash
     python3 exploit.py -c "cat /flags/root.txt > /var/www/html/flag.txt"
     ```
   - Retrieved the flag from the output file

---

### **Flag**

```
MASONCC{images_give_us_bash?}
```

---

