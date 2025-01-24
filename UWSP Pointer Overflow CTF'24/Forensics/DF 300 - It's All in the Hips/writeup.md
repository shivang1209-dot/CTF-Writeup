### **Challenge Name: DF 300 - It's All in the Hips**

---

### **Description**

Somehow, I've ended up with a collection of security cameras. Mostly from POCs. You know, working on security you sometimes vet physical security systems. Particularly if they have large IT requirements and deal with potentially sensitive data. Well, because they're never in service I just sort-of keep them laying around. However, I came in after break one morning and noticed one of the cameras was not in it usual place. Suspecting a set-up (I am always wary of people trying to grass me up), I examined the camera. What I found was astounding. Seems the camera went on quite an adventure in the night. Not sure who's responsible, but it seems they had fun.

#### **File Provided**  
- [DF300-1.001](https://pointeroverflowctf.com/static/DF300-1.001)

---

### **Approach**

We've got a `.001` file, which is typically part of a disk image.

#### **Step 1: Identify the File Type**  
Used the `file` command to analyze the file:

```bash
┌──(kali㉿kali)-[~/Desktop/poctf]
└─$ file DF300-1.001          
DF300-1.001: DOS/MBR boot sector; partition 1 : ID=0xe, start-CHS (0x0,2,4), end-CHS (0x78,254,63), startsector 129, 1950591 sectors, extended partition table (last)
```

The file is a DOS/MBR boot sector with a FAT16 partition.

#### **Step 2: Analyze Partitions**  
Used `fdisk` to list partitions:

```bash
┌──(kali㉿kali)-[~/Desktop/poctf]
└─$ fdisk -l DF300-1.001
Disk DF300-1.001: 952.5 MiB, 998768640 bytes, 1950720 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xdf39475b

Device        Boot Start     End Sectors   Size Id Type
DF300-1.001p1        129 1950719 1950591 952.4M  e W95 FAT16 (LBA)
```

#### **Step 3: Recover Files Using `foremost`**  
Extracted files from the disk image:

```bash
┌──(kali㉿kali)-[~/Desktop/poctf]
└─$ foremost -i DF300-1.001 -o output
```

This extracted two JPEG images. Ran `stegseek` and `exiftool` on both, but no hidden data or metadata was found.

#### **Step 4: Detailed File System Analysis with SleuthKit**  
Listed partition layout with `mmls`:

```bash
┌──(kali㉿kali)-[~/Desktop/poctf]
└─$ mmls DF300-1.001 
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000000128   0000000129   Unallocated
002:  000:000   0000000129   0001950719   0001950591   Win95 FAT16 (0x0e)
```

Listed files using `fls`:

```bash
┌──(root㉿kali)-[/home/kali/Desktop/poctf]
└─# fls -o 129 DF300-1.001

d/d 5:  fat16_partition
r/r * 8:        this-could-be_us.jpg
r/r * 11:       night_monkey.jpg
r/r * 12:       _tsme.jpg
r/r * 13:       _ad.jpg
r/r * 15:       gib_money.jpg
r/r * 16:       _tsme.jpg
r/r * 18:       gib_money.jpg
v/v 31201779:   $MBR
v/v 31201780:   $FAT1
v/v 31201781:   $FAT2
V/V 31201782:   $OrphanFiles
```

#### **Step 5: Extract Files Using `icat`**  
Extracted files:

```bash
┌──(root㉿kali)-[/home/kali/Desktop/poctf]
└─# icat -o 129 DF300-1.001 8 > this-could-be_us.jpg
└─# icat -o 129 DF300-1.001 11 > night_monkey.jpg
└─# icat -o 129 DF300-1.001 12 > _tsme.jpg
└─# icat -o 129 DF300-1.001 13 > _ad.jpg
└─# icat -o 129 DF300-1.001 15 > gib_money.jpg
└─# icat -o 129 DF300-1.001 16 > _tsme1.jpg
└─# icat -o 129 DF300-1.001 18 > gib_money1.jpg
```

Two were valid JPEGs. The rest were corrupt.

#### **Step 6: Repairing Corrupt Images**  
Opened corrupt images in a hex editor and repaired their headers. Successfully restored the images.  

#### **Step 7: Flag Discovery**  
One repaired image, `this-could-be_us.jpg`, contained the flag upon inspection.

---

### **Flag**

`poctf{uwsp_7h3_574r5_my_d3571n4710n}`

---### **Challenge Name: DF 300 - It's All in the Hips**

---

### **Description**

Somehow, I've ended up with a collection of security cameras. Mostly from POCs. You know, working on security you sometimes vet physical security systems. Particularly if they have large IT requirements and deal with potentially sensitive data. Well, because they're never in service I just sort-of keep them laying around. However, I came in after break one morning and noticed one of the cameras was not in it usual place. Suspecting a set-up (I am always wary of people trying to grass me up), I examined the camera. What I found was astounding. Seems the camera went on quite an adventure in the night. Not sure who's responsible, but it seems they had fun.

#### **File Provided**  
- [DF300-1.001](https://pointeroverflowctf.com/static/DF300-1.001)

---

### **Approach**

We've got a `.001` file, which is typically part of a disk image.

#### **Step 1: Identify the File Type**  
Used the `file` command to analyze the file:

```bash
┌──(kali㉿kali)-[~/Desktop/poctf]
└─$ file DF300-1.001          
DF300-1.001: DOS/MBR boot sector; partition 1 : ID=0xe, start-CHS (0x0,2,4), end-CHS (0x78,254,63), startsector 129, 1950591 sectors, extended partition table (last)
```

The file is a DOS/MBR boot sector with a FAT16 partition.

#### **Step 2: Analyze Partitions**  
Used `fdisk` to list partitions:

```bash
┌──(kali㉿kali)-[~/Desktop/poctf]
└─$ fdisk -l DF300-1.001
Disk DF300-1.001: 952.5 MiB, 998768640 bytes, 1950720 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xdf39475b

Device        Boot Start     End Sectors   Size Id Type
DF300-1.001p1        129 1950719 1950591 952.4M  e W95 FAT16 (LBA)
```

#### **Step 3: Recover Files Using `foremost`**  
Extracted files from the disk image:

```bash
┌──(kali㉿kali)-[~/Desktop/poctf]
└─$ foremost -i DF300-1.001 -o output
```

This extracted two JPEG images. Ran `stegseek` and `exiftool` on both, but no hidden data or metadata was found.

#### **Step 4: Detailed File System Analysis with SleuthKit**  
Listed partition layout with `mmls`:

```bash
┌──(kali㉿kali)-[~/Desktop/poctf]
└─$ mmls DF300-1.001 
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000000128   0000000129   Unallocated
002:  000:000   0000000129   0001950719   0001950591   Win95 FAT16 (0x0e)
```

Listed files using `fls`:

```bash
┌──(root㉿kali)-[/home/kali/Desktop/poctf]
└─# fls -o 129 DF300-1.001

d/d 5:  fat16_partition
r/r * 8:        this-could-be_us.jpg
r/r * 11:       night_monkey.jpg
r/r * 12:       _tsme.jpg
r/r * 13:       _ad.jpg
r/r * 15:       gib_money.jpg
r/r * 16:       _tsme.jpg
r/r * 18:       gib_money.jpg
v/v 31201779:   $MBR
v/v 31201780:   $FAT1
v/v 31201781:   $FAT2
V/V 31201782:   $OrphanFiles
```

#### **Step 5: Extract Files Using `icat`**  
Extracted files:

```bash
┌──(root㉿kali)-[/home/kali/Desktop/poctf]
└─# icat -o 129 DF300-1.001 8 > this-could-be_us.jpg
└─# icat -o 129 DF300-1.001 11 > night_monkey.jpg
└─# icat -o 129 DF300-1.001 12 > _tsme.jpg
└─# icat -o 129 DF300-1.001 13 > _ad.jpg
└─# icat -o 129 DF300-1.001 15 > gib_money.jpg
└─# icat -o 129 DF300-1.001 16 > _tsme1.jpg
└─# icat -o 129 DF300-1.001 18 > gib_money1.jpg
```

Two were valid JPEGs. The rest were corrupt.

#### **Step 6: Repairing Corrupt Images**  
Opened corrupt images in a hex editor and repaired their headers. Successfully restored the images.  

#### **Step 7: Flag Discovery**  
One repaired image, [this-could-be_us.jpg](Resources/this-could-be_us.jpg), contained the flag upon inspection.

---

### **Flag**

`poctf{uwsp_7h3_574r5_my_d3571n4710n}`

---