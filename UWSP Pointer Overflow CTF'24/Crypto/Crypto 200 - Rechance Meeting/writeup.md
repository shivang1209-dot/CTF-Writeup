## **Challenge Name: Crypto 200 - Rechance Meeting**

### **Description**

Full disclosure... I can't even remember what this challenge was supposed to be about. See, I do development of the contest over the summer, and I also have a lot of other things going on. Mostly birthdays. It seems like almost everyone in my life has a summer birthday. You'd think that there would be an equal chance of any given day being someone's birthday, but I'm afraid it just doesn't work that way.

I'm just going to give you the files and hopefully you can figure it out. Looks like I wrote a hash function. And this other thing looks like a word list. I definitely remember putting the flag in the archive. I also definitely remember that the password for the archive was two words from the list mashed together. As in, if the two words on this were "like" and "this" then the password for the archive is the two of them together "likethis."

So... uh, good luck! I guess!

**Files provided:**  
- [Crypto200-2_flag.zip](Resources/Crypto200-2_flag.zip)  
- [Crypto200-2_hashfunc.py](Resources/Crypto200-2_hashfunc.py)  
- [Crypto200-2_words.txt](Resources/Crypto200-2_words.txt)  

---

### **Approach**

The wordlist contains too many passwords to brute-force directly. The complexity of a full brute-force would be \(370k^2\).  

Instead, I focused on the challenge description, which mentions summer, birthdays, and months. These seemed to hint at wordlist patterns like:  
- `MonthDate`  
- `DateMonth`  
- `SeasonMonth`  
- `MonthSeason`

However, the wordlist only contains lowercase English words, eliminating the possibility of dates or years.  

### **Identifying a Birthday Attack**  
A hash function was provided, so I generated hashes for all words in the wordlist and searched for two distinct words that resulted in the same hash (a hash collision). These two words together form the password for the archive.

### **Steps Taken**  
1. Generated hashes for all words in the wordlist using the provided `hashfunc.py`.  
2. Detected 78 hash collisions using [collisions.py](Resources/collisions.py).  
3. None of the detected collisions unlocked the zip archive.  

### **Bug in the Wordlist**  
After contacting the challenge author, it was confirmed there was a bug in the provided wordlist. Once a fixed wordlist was released, I repeated the process:  
- Recomputed hashes.  
- Found the correct pair of words forming the password.  

**Password for archive:** `Moeso-gothicTarzanish`  
**Flag:** `poctf{uwsp_w3_c4n_r3m3mb3r_17}`  

---

### **Flag**

`poctf{uwsp_w3_c4n_r3m3mb3r_17}`

---