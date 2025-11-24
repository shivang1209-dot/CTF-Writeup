## **Challenge Name: Mysterious XOR**

### **Description**

One byte is all you ever need.

**Challenge author**: Biplav

**Server connection**: `18.212.136.134:2345`

---

### **Approach**

1. **Initial Analysis**  
   - Provided with a PCAP file containing network traffic
   - Connected to the server to understand the challenge
   - The description mentions "one byte" suggesting a single-byte XOR cipher

2. **Analyzing the PCAP**  
   - Opened the PCAP file in Wireshark
   - Found data packets containing many `0x67` byte values
   - This suggested the data might be XOR-encrypted with key `0x67`

3. **Extracting and Decrypting**  
   - Extracted the hex stream from the PCAP
   - XORed the data with `0x67` to decrypt
   - This revealed an ELF (executable) file

4. **Analyzing the ELF**  
   - Examined the decrypted ELF file
   - Found that it creates a file at `/tmp/<UTC-timestamp>` where the timestamp is when the ELF was executed
   - The filename is XORed with "1337" (padded with spaces) to create a 20-byte payload

5. **Understanding the Server Protocol**  
   - The server expects a 20-byte payload
   - It XORs the payload with "1337" to get the expected timestamp
   - If the timestamp matches, it returns the flag

6. **Finding the Timestamp**  
   - Extracted EXIF information from the PCAP to get a timestamp reference
   - Brute-forced timestamps around the EXIF time (±24 hours)
   - For each timestamp, created the filename `/tmp/<UTC-timestamp>`, XORed it with "1337", and sent to the server
   - Found the correct timestamp: `20251123T0540Z`

7. **Retrieving the Flag**  
   - Sent the correct payload to the server
   - Received the flag in the response

---

### **Flag**

```
PCTF{X0r_N_Myst3rIOus_Bin}
```

---

