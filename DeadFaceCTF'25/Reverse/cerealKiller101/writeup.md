## **Challenge Name: cerealKiller101**

### **Description**

The Tech Bro AI Moguls are now getting in on the act! They all want to have favorite, spooky cereals, too! Unfortunately, since they can't decide which they like the best, they are asking their respective LLMs.

Mr. Sam Altman, CEO of OpenAI, has a favorite "spooky" cereal. Choose your poison, Windows or Linux, and see if you can figure out which "spooky" (there it is again) he likes the best!

(You only need to choose one platform.)

**File provided**: [ck01-2025-rev03.bin](ck01-2025-rev03.bin)

---

### **Approach**

1. **Initial Binary Analysis**  
   - Analyzed the binary file using a reverse engineering tool (Binary Ninja or similar)
   - Examined the binary's strings and decompiled code

2. **Finding the Password Hash**  
   - Discovered a string in the binary:
     ```
     *(&var_518 + rcx_1) = *(u"One step closer... : aee1ee5262757cf67b619ff63e9672b6" + i)
     ```
   - The hash `aee1ee5262757cf67b619ff63e9672b6` appears to be an MD5 hash of the password required to execute the binary

3. **Cracking the Hash**  
   - Used an online hash cracking service (hashes.com) to crack the MD5 hash
   - Found the plaintext password: `peanutbuttercrunch`

4. **Executing the Binary**  
   - Ran the binary and entered the password when prompted:
     ```bash
     ./ck01-2025-rev03.bin
     ```
   - Entered password: `peanutbuttercrunch`
   - The binary executed and displayed:
     ```
     ChatGPT says: 
     The SPOOKIEST cereal is...
     
     *********** (I THINK I MIGHT BE HALLUCINATING) ***********
     
     deadface{Yeah-its-not-a-monster-cereal--Mr-Altman-is----different!}
     
     *********** (I THINK I MIGHT BE HALLUCINATING) ***********
     ```

---

### **Flag**

```
deadface{Yeah-its-not-a-monster-cereal--Mr-Altman-is----different!}
```

---

