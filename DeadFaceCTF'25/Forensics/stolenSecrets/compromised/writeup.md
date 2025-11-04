## **Challenge Name: compromised**

### **Description**

Which user did DEADFACE compromise and what was that user's password?

Submit the flag as deadface{username_password}. Example: deadface{user01_P@$$w0rd!}

**Note**: Use the ZIP file from Stolen Secrets: The Source

---

### **Approach**

1. **Accessing the PCAP File**  
   - Extracted the PCAP file from the ZIP archive provided in "Stolen Secrets: The Source"
   - The file is located at: `artifacts/cap-1753106207.pcap`

2. **Analyzing Network Traffic**  
   - Opened the PCAP file in Wireshark
   - Filtered for HTTP POST requests containing login attempts

3. **Examining Login Attempts**  
   - Found multiple login attempts in the HTTP form data:
     - First attempt: `username=cdootson`, `password=sparkles2023` (unsuccessful)
     - Second attempt: `username=dtenuto`, `password=SuP3RS3cr3tD34DF4C3#` (unsuccessful)
   - Continued analyzing the network stream to find successful authentication

4. **Finding the Compromised User**  
   - Located the successful login attempt later in the capture
   - Found the compromised credentials:
     ```
     Username: bsampsel
     Password: Sparkles2025!
     ```

---

### **Flag**

```
deadface{bsampsel_Sparkles2025!}
```

---

