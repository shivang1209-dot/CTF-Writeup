## **Challenge Name: Crack 100 - I Have Written Down My Secrets**

### **Description**

Summer breaks are great, but I can't stand the downtime. I need to keep my mind occupied. I need a project, a puzzle, a challenge. It's not about staying productive, per se. I just need to keep this mind moving or I'll get bored. I've found the hobby that is presently perfect without being too invested: Learning languages. Simple, no-pressure, infinitely valuable, and a great intellectual challenge.  

This summer, I went a little overboard and overindulged in Duo's offerings. I spent at least a few hours every day learning **Spanish, French, German, Italian, Russian, Mandarin, Arabic, Finnish, Hindi,** and **Swedish**. I know, that's obviously way too many languages to attempt at once, but it's easy to over-commit and spread myself thin when there are so many wonderful options available.  

French was actually my focus this summer. I had so much fun learning that I would over-zealously do extra lessons. Is Duo the best way to learn? *Non!* Am I really learning all that much in the end? *Occupez-vous de vos oignons!* After a summer of learning, am I able to even communicate at all in French? *Absolument pas!*  

*Je te dis, c'était mieux que de mater les JO à Paris cet été.*

**File provided**: [Crack100-2.pdf](Resources/Crack100-2.pdf)

---

### **Approach**

1. **Initial Observations**  
   - The phrase *"Occupez-vous de vos oignons"* translates to *"Mind your own business."*  
   - Another phrase, *"Absolument pas! Je te dis, c'était mieux que de mater les JO à Paris cet été."* translates to *"Absolutely not! I tell you, it was better than watching the Olympics in Paris this summer."*

2. **Extracting Data from the PDF**  
   - Ran `john2pdf` on the provided PDF file, generating a `hashes.txt` file.  
   - Attempted cracking the hashes using `john` with the `rockyou.txt` wordlist but didn’t succeed.  
   - Tried various French wordlists, but none worked initially.

3. **Identifying the Pattern**  
   - Observed an imperative tone in *"Occupez"* and identified it as a French word.  
   - Related the solution to the challenge description keywords: over-indulge and over-commit.  

4. **Finding the Correct Word**  
   - The correct French word was *"surinvesti"* (overinvested), which cracked the hash.

5. **Decoding the Hidden Data**  
   - The PDF contained the encoded string:  
     `cG9jdGZ7dXdzcF9XMW5kNV8wZl9DaDRuZzN9`  
   - Decoded it using Base64, revealing the flag.

---

### **Flag**

`poctf{uwsp_W1nd5_0f_Ch4ng3}`

---
