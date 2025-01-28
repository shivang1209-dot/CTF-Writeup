## **Challenge Name: Stego 200 - You Never Liked My Music**  

---

### **Description**  

Did I ever mention that I used to want to be a professional musician? It's true. It never really worked out. Probably because I wasn't very good. Still, for a good portion of my 20s, I did the whole thing with garage bands and trying to get recognized and everything. I really wanted to make a mark on the world but didn't really have any means to do it. So I did the next best thing and made a lot of noise to be heard. Never seemed to work, though. Always fell on deaf ears.  

I gave up the dream after I entered university and discovered my next passions, and that brings us together today!  

Still, I've always had an affinity for music. Even as the years of loud music take their toll on my poor ears. I'm luckier than some since my hearing is still pretty good. Still, I get tinnitus ringing in my ears more often now, and I know when that happens that it means that I'm waving goodbye to another frequency of sound.  

The only bonus is that now I can play annoyingly high-pitched sounds to irritate the youngsters, and it doesn't bother me a bit!  

Anyway, I managed to find an old recording of my jazz drummer days to share with all of you. Oh, the dreams of a desperate kid. Enjoy!

**Files Provided:**  
<audio controls src="Resources/Stego200-1.wav" title="Stego200-1.wav"></audio>  

---

### **Approach**  

1. **Initial Observations**:  
   - Listened to the audio file and noticed faint ticking sounds scattered throughout.  
   - These sounds were subtle and difficult to discern.  

2. **Spectrogram Analysis**:  
   - Opened the audio file in Audacity and switched to spectrogram view.  
   - Initially, nothing unusual was visible.  

3. **Frequency Adjustment**:  
   - Remembering the hint about "ultrasonic sound," I increased the frequency range in the spectrogram view to 18kHz and above.  
   - This revealed patterns resembling encoded information.  

4. **Decoding the Pattern**:  
   - The patterns in the spectrogram suggested binary-like encoding based on the width and spacing of the lines.  
   - The data appeared as stacks of 0s and 1s.  

5. **Extracting and Converting Binary to ASCII**:  
   - Carefully measured the widths of the patterns to determine the binary data.  
   - Converted the extracted binary into ASCII text using an online converter:  
     ```  
     01110000 01101111 01100011 01110100 01100110 01111011 01110101 01110111 01110011 01110000  
     01011111 00110111 01101000 00110011 01011111 01110101 01101110 00110011 01111000 00110100  
     01101101 00110001 01101110 00110011 01100100 01011111 01101100 00110001 01100110 00110011  
     01111101  
     ```  
   - The binary converted to the flag.  

6. **Confirming Partial Data**:  
   - If decoding was challenging at first, I used the known plaintext prefix `poctf{uwsp_` to align and validate initial binary values.  

---

### **Flag**  

`poctf{uwsp_7h3_un3x4m1n3d_l1f3}`  

---