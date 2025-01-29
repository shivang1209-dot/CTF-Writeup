# Challenge Name: Cats

**Files Provided:**  
[`chall.jpg`](Resources/chall.jpg)

## Description

> "Because Events Head said 'NO CATS'"

## Writeup

### Initial Analysis
First verify the file type:
```bash
┌──(kali㉿kali)-[~/Desktop/tmp]
└─$ file chall.jpg 
chall.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1280x952, components 3
```
This shows `chall.jpg`, is a valid JPEG image. Visual inspection shows a normal image:

```bash
┌──((kali㉿kali)-[~/Desktop/tmp]
└─$ eog chall.jpg
```

### Steganography Investigation
Used `stegseek` with rockyou.txt wordlist:
```bash
┌──(kali㉿kali)-[~/Desktop/tmp]
└─$ stegseek chall.jpg

StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "acatsmeow"         
[i] Original filename: "flag.txt".
[i] Extracting to "chall.jpg.out"
```

### Flag Extraction
Found embedded file containing the flag:
```bash
┌──(kali㉿kali)-[~/Desktop/tmp]
└─$ cat chall.jpg.out 
CodefestCTF{573gh1de_ch4ll_m30w}
```

## Flag
`CodefestCTF{573gh1de_ch4ll_m30w}`

---
