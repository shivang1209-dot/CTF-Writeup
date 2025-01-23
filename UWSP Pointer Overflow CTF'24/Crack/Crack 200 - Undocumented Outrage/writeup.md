## **Challenge Name: Crack 200 - Undocumented Outrage**

### **Description**

There's a lot to like about where I live. There's beautiful wilderness. You're never more than thirty feet from a tavern, bank, and fast food restaurant. And thanks to the university, there are some unique opportunities.  

When I was in high school, I started learning Russian. My choices were French, German, Spanish, or Russian. Most school districts in the USA only offer the first three if they have any foreign language programs at all. I picked Russian because I thought it would be the hardest—and I am a total fool. But I stuck with it. I was determined to learn, and Госпожа Демовидова was determined to teach me. I ended up taking it longer than I technically had to: two years in high school and four years in university.  

Anyway, there's plenty to dislike about where I live, too. Like the cold. I realize that many of you might be from cold climates, but I'm talking *cold.* As in below zero for many weeks most years. So cold that if you throw a cup of water in the air, it will be frozen solid by the time it hits the ground. So cold that if you take some rolls right out of the oven, they'll be delicious and hot. Set them near an open window to cool, and they will be cold in seconds. And no one likes cold rolls. Cold rolls steal all the joy warm bread brings.  

I suppose I'm rambling enough. We should probably get to the challenge. Here's an encrypted `.docx` file. I seem to have forgotten the password, but I'm sure you'll find it as long as you can stay cool under pressure.  

**File provided**: [Crack200-2.docx](Resources/Crack200-2.docx)

---

### **Approach**

1. **Analyzing the Challenge**  
   - The description mentions Russian extensively, hinting that the password may involve the Russian language.  
   - Downloaded a Russian wordlist:  
     [Russian Wordlist](https://raw.githubusercontent.com/sharsi1/russkiwlst/refs/heads/master/russkiwlst_top_2k.lst).

2. **Extracting the Password Hash**  
   - Used `office2john` to extract the password hash from the `.docx` file.

3. **Trying Different Wordlists**  
   - Tested several wordlists, including the Russian wordlist mentioned above.  
   - Looked up "Mrs. Demovidova" from the description and discovered Anna Demovidova's website.  
   - Used `cewl` to generate a custom wordlist from her site but found no success.

4. **Using Transliterated Wordlists**  
   - Found a tool called **CRWG** that shows how Russian people transliterate English passwords using similar-looking characters on the keyboard.  
   - Generated a custom transliterated wordlist using CRWG and ran `john` with it.

5. **Cracking the Password**  
   - Successfully cracked the password: `холоднокатаного` (translates to "cold rolled").  

6. **Extracting the Flag**  
   - Opened the `.docx` file using the cracked password and retrieved the flag.

---

### **Flag**

`poctf{uwsp_wh15p3r5_1n_7h3_d4rk}`

--- 
