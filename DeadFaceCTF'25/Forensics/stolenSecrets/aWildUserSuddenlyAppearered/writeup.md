## **Challenge Name: aWildUserSuddenlyAppearered**

### **Description**

Which user did DEADFACE create for persistence? What was that user's first name and password?

Submit the flag as deadface{firstname_password}. Example: deadface{John_P@$$w0rd!}.

**Note**: Use the ZIP file from Stolen Secrets: The Source

---

### **Approach**

1. **Accessing the PCAP File**  
   - Extracted the PCAP file from the ZIP archive provided in "Stolen Secrets: The Source"
   - The file is located at: `artifacts/cap-1753106207.pcap`

2. **Analyzing Network Traffic**  
   - Opened the PCAP file in Wireshark
   - Filtered for HTTP POST requests, particularly those creating new user accounts

3. **Finding User Creation Request**  
   - Located an HTTP POST request containing admin action to create a new user
   - Found the form data in the request:
     ```
     first_name=Dorla&last_name=Tenuto&email=dtenuto%40techglobalresearch.adsfglskdafhj.com&username=dtenuto&password=SuP3RS3cr3tD34DF4C3%23&is_admin=1&add_user=
     ```
   - Decoded the URL-encoded values:
     - First name: `Dorla`
     - Last name: `Tenuto`
     - Username: `dtenuto`
     - Password: `SuP3RS3cr3tD34DF4C3#`
     - Admin flag: `is_admin=1`

4. **Constructing the Flag**  
   - DEADFACE created a user with first name `Dorla` and password `SuP3RS3cr3tD34DF4C3#`

---

### **Flag**

```
deadface{Dorla_SuP3RS3cr3tD34DF4C3#}
```

---

