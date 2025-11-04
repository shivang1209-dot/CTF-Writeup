## **Challenge Name: dissTrack**

### **Description**

We where looking at the message board and saw that lilith and deephax communicated that they would have a secret way of talking to each other while they ran an attack. We cant make heads or tales of it but we did note that they mentioned Band names and referenced some songs.

Enter the answer as deadface{flag text}.

---

### **Approach**

1. **Initial Investigation**  
   - Located the thread on the Ghost Town message board where lilith and deephax were communicating
   - Found the thread at: `https://ghosttown.deadface.io/t/how-do-y-all-decompress-after-ops/84/9`

2. **Discovering the Playlist**  
   - Found a message from lilith containing a Spotify playlist identifier:
     ```
     Hey Deep, Since you like music so much I put something together for that THING that's happening.
     check it out tell me what you think
     34qdvkzNI5IIZUR5kVOpNx
     ```
   - The string `34qdvkzNI5IIZUR5kVOpNx` is a Spotify playlist/user identifier

3. **Accessing the Playlist**  
   - Constructed the Spotify playlist URL: `https://open.spotify.com/playlist/34qdvkzNI5IIZUR5kVOpNx`
   - Accessed the playlist to examine its contents

4. **Finding the Flag**  
   - Read the playlist description, which contained the flag:
     ```
     You made it! Happy to see you are participating this year! Here is your flag: deadface{D!6_7H47_Cr^ZY_rHY7HM!}
     ```
   - Note: There was also an attached image in the thread (a spreadsheet), but it was a misdirection and not relevant to solving the challenge

---

### **Flag**

```
deadface{D!6_7H47_Cr^ZY_rHY7HM!}
```

---

