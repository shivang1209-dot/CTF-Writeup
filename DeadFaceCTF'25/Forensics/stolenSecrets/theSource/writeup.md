## **Challenge Name: theSource**

### **Description**

A department at TGRI was getting lazy with sensitive files. Rather than use the company's approved filesharing application, a member used an application called MyShare and forgot to configure it to run HTTPS.

DEADFACE found the site and were able to compromise it and steal several sensitive files. Based on DEADFACE's past behavior, let's assume that flags discovered may be used as DEADFACE passwords.

First thing's first: what is the IP address of the DEADFACE attacker? Submit the flag as deadface{X.X.X.X}.

**Files provided**: [artifacts/](artifacts/)

---

### **Approach**

1. **Examining the Artifacts**  
   - Located the artifacts folder containing:
     - `access.log`
     - `cap-1753106207.pcap`
     - `error.log`
     - `error.php.log`

2. **Analyzing Access Logs**  
   - Opened `access.log` to examine web server access records
   - Looked for unusual IP addresses making requests to the MyShare application

3. **Identifying the Attacker IP**  
   - Found that the majority of requests were coming from IP address: `134.199.202.160`
   - This IP address was identified as the DEADFACE attacker's source

---

### **Flag**

```
deadface{134.199.202.160}
```

---

