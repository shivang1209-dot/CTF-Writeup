## **Challenge Name: versions**

### **Description**

Based on the network traffic, what web server software and version is MyShare running?

Submit the flag as deadface{software_version}. Example: deadface{apache_1.2.3}

**Note**: Use the ZIP file from Stolen Secrets: The Source

---

### **Approach**

1. **Accessing the PCAP File**  
   - Extracted the PCAP file from the ZIP archive provided in "Stolen Secrets: The Source"
   - The file is located at: `artifacts/cap-1753106207.pcap`

2. **Analyzing HTTP Headers**  
   - Opened the PCAP file in Wireshark
   - Examined HTTP response headers to find server information

3. **Finding Server Information**  
   - Located the HTTP response headers in the same request where the calling card flag was found
   - Found the Server header:
     ```
     Server: nginx/1.25.5
     ```
   - This indicates MyShare is running nginx version 1.25.5

---

### **Flag**

```
deadface{nginx_1.25.5}
```

---

