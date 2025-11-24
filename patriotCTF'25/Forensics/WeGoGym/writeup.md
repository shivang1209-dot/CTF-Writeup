## **Challenge Name: We Go Gym**

### **Description**

Our gym IT staff noticed some weird traffic going through on our local network, do you think you can investigate and find our what information was sent?

**Challenge author**: Salochi

---

### **Approach**

1. **Initial Analysis**  
   - Provided with a PCAP (packet capture) file
   - Opened the file in Wireshark for analysis
   - Looked for unusual patterns or hidden data in the network traffic

2. **Examining HTTP Traffic**  
   - Filtered for HTTP traffic in Wireshark
   - Noticed that TTL (Time To Live) values in IP headers might contain hidden information

3. **Extracting TTL Values**  
   - Used `tshark` to extract TTL values from HTTP packets:
     ```bash
     tshark -r wegogym.pcap -Y "http" -T fields -e ip.ttl
     ```
   - This extracted all TTL values from HTTP traffic

4. **Decoding the Flag**  
   - The TTL values represented decimal ASCII codes
   - Cleaned up the output to get the sequence:
     ```
     80 67 84 70 123 116 49 109 51 95 116 48 95 103 51 55 95 53 119 48 49 125
     ```
   - Converted each decimal value to its ASCII character:
     - `80` = 'P'
     - `67` = 'C'
     - `84` = 'T'
     - `70` = 'F'
     - `123` = '{'
     - etc.

5. **Reconstructing the Flag**  
   - Converted all decimal values to ASCII characters
   - Reconstructed the complete flag string

---

### **Flag**

```
PCTF{t1m3_t0_g37_5w01}
```

---

