## **Challenge Name: DF 100 - A Record of Events**

---

### **Description**

This is a simple forensics challenge. The scenario involves an old flash drive that was lost near campus many years ago. Attempts to trace its owner were unsuccessful as it hadn’t been connected to any campus computers. There’s speculation that it might have belonged to one of the missionaries frequently seen on campus, but this detail didn't provide a solid lead. The flash drive was locked away in a safe and forgotten for about 20 years before being rediscovered. Before disposing of it, a challenge was created to explore its contents.

#### **File Provided**  
- [DF100-1](https://uwspedu-my.sharepoint.com/:u:/g/personal/cjohnson_uwsp_edu/EZ8KXiGBIGxOrN1lhymI81gB2CaRXdaL2vOkySuzvIcz3Q?e=XjHifH)

---

### **Approach**

#### **Step 1: Analyzing the File**

1. **File Overview**: The provided file, `DF100-1.001`, is a 480 MB disk image, likely representing the contents of the flash drive.

2. **Initial Inspection with Binwalk**:  
   - Ran `binwalk` to analyze the file structure and identify embedded files.  
   - Detected numerous file types, including MP3s, JPEGs, PNGs, PDFs, and ZIPs.
   - Attempted to extract the files using `binwalk -e`, but many extracted ZIPs turned out to be disk images, making direct extraction unfeasible.

#### **Step 2: Deep Analysis with Sleuthkit**

To overcome the challenges with direct extraction, I switched to **Sleuthkit** for deeper forensic analysis.

1. **Identify Partition Structure**:  
   Used the `mmls` command to list all partitions within the disk image.

   ```bash
   mmls DF100-1.001
   ```

2. **List File Contents**:  
   Ran `fls` to recursively list all files in the partition. Adjusted the partition offset based on `mmls` output (e.g., offset 32).

   ```bash
   fls -r -o 32 DF100-1.001
   ```

3. **File Extraction**:  
   Extracted files one by one using `icat` and analyzed them.

#### **Step 3: Finding the Flag**

1. Among the extracted files, `sotto-voce.mp3` file stood out as potentially interesting.
2. Opened the MP3 in **Audacity** and played the audio.
3. The audio contained a voice dictating the flag.

---

### **Flag**

`poctf{uwsp_57r4n63r_1n_4_57r4n63_14nd}`

---