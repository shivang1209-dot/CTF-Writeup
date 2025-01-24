### **Challenge Name: DF 300 - I'm a Stranger Here Myself**

---

### **Description**

I was inspired to create this challenge after a real case I worked. In my experience, actual steganography is pretty rare and typically signifies a subject with advanced domain competency in counter-forensics. Most subjects will use encryption or basic obfuscation because you get similar results with less hassle. Only the most sensitive of evidence and most paranoid of subjects encrypt and hide their data.

I was contacted to reexamine evidence in a criminal case. It was an alleged criminal conspiracy with multiple subjects. Five, to be exact, and it was suspected that there was a sixth. The only problem was that there was no solid evidence directly linking this sixth member to the conspiracy. I took a look and discovered a situation that is crudely reproduced in this challenge.

**NOTE:** The flag for this challenge uses a '1' in place of both the 'i' and 'l' characters. You can submit the flag as found, or using the character set in the rules. Either will be accepted.

#### **File Provided**  
- [DF300-3.pcap](Resources/DF300-3.pcap)

---

### **Approach**

- **Wireshark file**.

**USERNAME** - user  
**PASSWORD** - password  

The flag is in 2 parts, which are sent as 2 files.

- **Part 1** looks like a JPEG, due to the footer of the FTP data for part 1. (tcp stream eq 2)  
- **Part 2** is the missing header for the JPEG file sent in part 1. (tcp stream eq 4)

The current directory is `/home/user`.

Let's follow the TCP stream, view it as raw bytes, and save these files with their respective extensions.

- **Packet 218** - Part 1 completed.  
- **Packet 261** - Part 2 initialized.  
- **Packet 267** - Part 2 completed.  

So, we need to:

1. Extract the second part, then extract the first part and append it to the second part.
2. Save the second part as `DF-300_flag_part1` and open it up in a hex editor. 
3. Edit the first 4 hex bytes (`de ad be ef`) with the magic number for JPEGs (`dd f8 dd e0`).
4. Now, extract the second half, name it `DF-300_flag_part2`, and then append it to the `part1` file and save it as [recovered_image.jpg](Resources/recovered_image.jpg).

That didn't work.

Looks like the file has some error, so I tried an online repair JPG site, and it fixed the issue. I was able to get the flag - ![repaired_image.jpg](Resources/repaired_image.jpg).

### **Flag**

`poctf{uwsp_f34r_15_7h3_m1nd_k1113r}`

---