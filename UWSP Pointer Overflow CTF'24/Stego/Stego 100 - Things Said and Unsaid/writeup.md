## **Challenge Name: Stego 100 - Things Said and Unsaid**  

---

### **Description**  

So there I was connected to the free McDonald's Wi-Fi hackin' the ISS nav computer as it passed by from orbit and I intercepted a still image from one of the onboard camera feeds. Something about it just seems a little odd, but I can't quite place it... Then again, it might just be my face-blindness acting up!

Remember, this is a Stego challenge. A password will be required to solve the challenge, and that means the password will also be hidden somewhere in the challenge.

**Image Provided:**  
![Stego100-3.jpeg](Resources/Stego100-3.jpeg)

---

### **Approach**  

Ran exiftool for details - JPG, no special metadata.

Ran binwalk - found 

0             0x0             JPEG image data, JFIF standard 1.01
562069        0x89395         Zip archive data, encrypted compressed size: 57, uncompressed size: 29, name: Stego100-3_flag.txt
562298        0x8947A         End of Zip archive, footer length: 22

Extracted zip using - binwalk -e Stego100-3.jpeg

Unzipping - Found zip was password protected.

Bruteforced using stegseek on jpg for password - No passphrase found

Opened the image in a hex editor, header looks normal, went to the footer and we can see our flag file inside a zip but after that we see a string - "probably_improbable"

Ran exiftool to see it's listed as the Zip File Name... Could be the password.

└─$ exiftool 89395.zip      
ExifTool Version Number         : 13.00
File Name                       : 89395.zip
Directory                       : .
File Size                       : 251 bytes
File Modification Date/Time     : 2025:01:28 10:42:02-05:00
File Access Date/Time           : 2025:01:28 10:42:16-05:00
File Inode Change Date/Time     : 2025:01:28 10:42:02-05:00
File Permissions                : -rw-rw-r--
File Type                       : ZIP
File Type Extension             : zip
MIME Type                       : application/zip
Zip Required Version            : 51
Zip Bit Flag                    : 0x0001
Zip Compression                 : Unknown (99)
Zip Modify Date                 : 2024:09:18 09:21:30
Zip CRC                         : 0x00000000
Zip Compressed Size             : 57
Zip Uncompressed Size           : 29
Zip File Name                   : probably_improbable

Ran 7z x file.zip with probably_improbable as password and our flag was extracted



---

### **Flag**  

`poctf{uwsp_w3_4r3_such_57uff}`