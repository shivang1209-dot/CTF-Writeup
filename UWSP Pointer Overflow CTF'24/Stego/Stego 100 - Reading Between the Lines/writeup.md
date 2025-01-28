## **Challenge Name: Stego 100 - Reading Between the Lines**  

---

### **Description**  

Good news, everyone! I've decided it's time to write my memoirs. After a lifetime of interesting experiences, I think it's time the astounding story of my life be recorded for the benefit and advancement of humanity. I can tell everyone about the time that I... Hmm... Ok, maybe my life isn't so interesting after all...

...But it can be! I'm going to throw in a couple of interesting details! Give it a little something extra! No one will notice if I embellish a little as long as I don't change it too much. I can always just put a disclaimer on it that it's only based on true events - a little transparency is a good thing.

**Files Provided:**  
[Stego100-2.txt](Resources/Stego100-2.txt)

---

### **Approach**  

When I opened the `Stego100-2.txt` file in Sublime Text, I noticed some weird characters in the first couple of lines. These characters, `<0x200c>` and `<0x200b>`, represent invisible spaces (known as Zero Width Non-Joiner and Zero Width Space) that can't be seen, but they are present.

Opening the file in Notepad on Windows, the invisible characters become clearly visible. This indicated that the file might contain hidden data.

To further explore, I examined the hex dump of the file using `xxd`:

```bash
┌──(kali㉿kali)-[~/Desktop/poctf/stego]
└─$ xxd Stego100-2.txt | head
00000000: 0d0a e280 8c4f e280 8b6e e280 8b63 e280  .....O...n...c..
00000010: 8b65 e280 8c20 e280 8c75 e280 8c70 e280  .e... ...u...p..
00000020: 8c6f e280 8c6e e280 8b20 e280 8b61 e280  .o...n... ...a..
00000030: 8c20 e280 8b74 e280 8b69 e280 8b6d e280  . ...t...i...m..
00000040: 8b65 e280 8c2c e280 8b20 e280 8b69 e280  .e...,... ...i..
00000050: 8c6e e280 8c20 e280 8c61 e280 8b20 e280  .n... ...a... ..
00000060: 8b6c e280 8c61 e280 8b6e e280 8b64 e280  .l...a...n...d..
00000070: 8b20 e280 8c77 e280 8b68 e280 8c65 e280  . ...w...h...e..
00000080: 8c72 e280 8c65 e280 8b20 e280 8b74 e280  .r...e... ...t..
00000090: 8c68 e280 8c65 e280 8b20 e280 8b63 e280  .h...e... ...c..
```

In the hex dump, we see two distinct patterns, `e2808b` and `e2808c`, which are the Unicode representations of the invisible characters. To extract the hidden message, I wrote a Python script that identified and decoded these patterns.

---

Running this [script](Resources/script.py) on the provided file extracts the [flag](Resources/flag.txt).

---

### **Flag**  

`poctf{uwsp_b3w4r3_7h3_j4bb3rw0ck}`

---