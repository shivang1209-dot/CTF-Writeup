# Capture the Hidden - Writeup

## Challenge Description
A suspicious network transmission has been intercepted. A cybersecurity agent detected suspicious network traffic before disappearing. The attackers attempted to erase their tracks, but a PCAP file was recovered.

Somewhere within these packets, a crucial file was exfiltrated. Can you analyze the traffic, extract the hidden data, and uncover the secret message?

#### Files - [forensic-6-forensic-capture-the-hidden.zip](Resources/forensic-6-forensic-capture-the-hidden.zip)
---

## Solution Walkthrough

### Step 1: Extracting the PCAP File
The challenge provides a zip file containing a PCAP capture. First, we extract it using:
```sh
unzip forensic-6-forensic-capture-the-hidden.zip
```
This gives us the PCAP file to analyze.

### Step 2: Inspecting the PCAP File
Open the PCAP file in Wireshark and look for suspicious packets. The first packet contains an HTTP POST request to a malicious server's upload endpoint with encoded data:
```
data=646174613d5a574e305a6e74514d445630587a467a5833597a636e6c664d7a5131655639554d4639474d5535
```

### Step 3: Decoding the Hidden Data
Using CyberChef, we first hex decode the data and then base64 decode the output. This reveals:
```
ectf{P05t_1s_v3ry_345y_T0_F1N
```
This appears to be part of the flag, but it's incomplete.

### Step 4: Finding Other Clues in the Traffic
Further analysis reveals multiple DNS queries to suspicious subdomains:
```
o47uz8ukve.malicious.com
ll8f304lle.malicious.com
h1ik2nm84z.malicious.com
khd34rzf7s.malicious.com
8gsi65gim0.malicious.com
```
These might be part of a covert exfiltration mechanism.

Another key packet:
```
7 0.001307 192.168.1.20 203.0.113.5 FTP 53 Request: USER hacker
```
Following the stream reveals:
```
USER hacker
PASS secret123
PUT hidden_file.txt
```
The attacker uploaded a file named `hidden_file.txt`, but it is not visible in the capture.

### Step 5: Extracting Data from Retransmitted Packets
By revisiting the TCP retransmissions in Wireshark, we locate additional data hidden within FTP commands:
```
PUT hidden_file.txt
```
Using `strings` on the PCAP file confirms the presence of encoded data, what a waste of time I did:
```
data=ZWN0ZntQMDV0XzFzX3YzcnlfMzQ1eV9UMF9GMU5EfQ==
```

### Step 6: Decoding the Full Flag
Decoding this base64 string gives us the complete flag:
```
ectf{P05t_1s_v3ry_345y_T0_F1ND}
```
---

```
ectf{P05t_1s_v3ry_345y_T0_F1ND}
```


