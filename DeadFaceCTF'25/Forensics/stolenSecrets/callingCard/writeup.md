## **Challenge Name: callingCard**

### **Description**

DEADFACE has left a taunting message in their initial probing of the MyShare web application at http://files.techglobalresearch.com. Their attack involves a simple HTTP request with a hidden flag. Can you uncover their calling card?

Submit the flag as deadface{text}

**Note**: Use the ZIP file from Stolen Secrets: The Source

---

### **Approach**

1. **Accessing the PCAP File**  
   - Extracted the PCAP file from the ZIP archive provided in "Stolen Secrets: The Source"
   - The file is located at: `artifacts/cap-1753106207.pcap`

2. **Analyzing Network Traffic**  
   - Opened the PCAP file in Wireshark for analysis
   - Examined the HTTP traffic to identify DEADFACE's initial request

3. **Finding the Calling Card**  
   - Located the first HTTP request in the capture
   - Found a Base64-encoded message in the request:
     ```
     SeKAmXZlIGdhaW5lZCBmdWxsIGFjY2VzcyB0byB5b3VyIG5ldHdvcmsuIEV2ZXJ5IGZpbGUsIGV2ZXJ5IGNyZWRlbnRpYWwsIGV2ZXJ5IHN5c3RlbSDigJQgdW5kZXIgbXkgY29udHJvbC4gWW91IGRpZG7igJl0IG5vdGljZSBiZWNhdXNlIEkgZGlkbuKAmXQgd2FudCB5b3UgdG8uCgpUaGlzIHdhc27igJl0IGx1Y2suIEl0IHdhcyBwcmVjaXNpb24uIFlvdXIgZGVmZW5zZXMgd2VyZSBpbmFkZXF1YXRlLCBhbmQgSeKAmXZlIHByb3ZlbiBpdC4KClRoaXMgYXR0YWNrIGlzIGJyb3VnaHQgdG8geW91IGJ5IG1pcnZlYWwuIFRoYW5rcyBmb3IgdGhlIHNlY3JldHMh
     ```
   - Decoded the Base64 message:
     ```
     I've gained full access to your network. Every file, every credential, every system — under my control. You didn't notice because I didn't want you to.
     
     This wasn't luck. It was precision. Your defenses were inadequate, and I've proven it.
     
     This attack is brought to you by mirveal. Thanks for the secrets!
     ```

4. **Extracting the Flag**  
   - Found the flag in the HTTP header for this request:
     ```
     deadface{l3ts_get_Th3s3_fiL3$}
     ```

---

### **Flag**

```
deadface{l3ts_get_Th3s3_fiL3$}
```

---

