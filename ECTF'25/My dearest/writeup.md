### Challenge Name: My dearest  

#### Description:  
We've been told you're good at puzzles, so we're going to test that with a small 100-piece puzzle.  

I have Received a love letter by a fake email. Can you help me to find who is the author ?

Flag format: ectf{NameLastName}

**Files Provided:**  
[Forensic_5_-_My_dearest.zip](Resources/Forensic_5_-_My_dearest.zip) 

---

### Solution  

1. **Initial Analysis**  
   - Used `oletools` to analyze the document but found nothing suspicious.  

2. **Extracting Metadata**  
   - Ran `exiftool` on the document to check for embedded metadata:  
     ```
     exiftool My\ dearest.docx  
     ```
   - The output included details such as file type, modification timestamps, and **the document's author**:  
     ```
     ExifTool Version Number         : 13.00
     File Name                       : My dearest.docx
     Directory                       : .
     File Size                       : 16 kB
     File Modification Date/Time     : 2025:01:30 08:53:23-05:00
     File Access Date/Time           : 2025:02:01 11:17:14-05:00
     File Inode Change Date/Time     : 2025:02:01 11:17:07-05:00
     File Permissions                : -rw-rw-rw-
     File Type                       : DOCX
     File Type Extension             : docx
     MIME Type                       : application/vnd.openxmlformats-officedocument.wordprocessingml.document
     Zip Required Version            : 20
     Zip Bit Flag                    : 0x0006
     Zip Compression                 : Deflated
     Zip Modify Date                 : 1980:01:01 00:00:00
     Zip CRC                         : 0x7102bc4a
     Zip Compressed Size             : 365
     Zip Uncompressed Size           : 1576
     Zip File Name                   : [Content_Types].xml
     Title                           : 
     Subject                         : 
     Creator                         : Michel Teller
     ```
   - The **"Creator" field** reveals the author's name: **Michel Teller**  

---

### Flag:  
```
ectf{MichelTeller}
```