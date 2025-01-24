### **Challenge Name: DF 400 - No Irony in Rain**

---

### **Description**

I know this is probably not a good use of the contest, but I figure I have a lot of brainpower between the lot of you and I could use the help. Here's the situation: I had a really cool idea. I was going to finance an independent film called, "POCTF 2024: The Movie." A big-budget, sci-fi, action, rom-com starring Yours Truly. Worldwide distribution with premiere releases in New York, Moscow, Toronto, Dubai, Karnataka, and it was going to be THE movie event of this century. I got a screener copy right before the start of the contest. I decided to post it to YouTube to get some comments. You know, like a test screening. Things were going great. I had 24 views after just one week of having it up on my channel. Then it really started blowing up. It went viral, and I had 506 views at the end of the weekend! A smash hit! But then I started getting weird comments on the video. People posting "xaxaxaxaxa" and ")))" a lot. I don't know what that means, but I naturally assumed it was some kind of attack. I need you to comb through the video and tell me if anything seems fishy to you. Here's an exact copy of the video that I uploaded to my channel for you to review.

#### **File Provided**  
- [DF400.mov](https://pointeroverflowctf.com/static/DF400.mov)

---

### **Approach**

- **Video Editing Software**: Blackmagic Design DaVinci Resolve Studio

In the YouTube subtitles of the video, here’s what was translated from various languages:

- **Arabic**: 
  - "Inspired by real events" (مستوحاة من أحداث حقيقية)
  - "Pain breeds perseverance." ("فالآلام تولد المثابرة")
  - "Perseverance breeds character" (والمثابرة تولد الشخصية)
  - "Character creates hope" (والشخصية تولد الأمل)
  - "The story of crimes in West Mesa" and the serial killer is on the loose (قصة الجرائم في غرب ميسا" والقاتل المتسلسل طليق)
  - "West Mesa, New Mexico" (غرب "ميسا"، "نيو مكسيكو")
  - 2009

- **Bangla**:
  - "Give the shield. Solder it. -Don't shout. I give" (ঝাল দিন। এটাতে ঝাল দিন। -চিৎকার করো না। আমি দিচ্ছি)
  - "Hurry up" (তারাতারি কর।)
  - "Take this" (এই নাও)

- **English**: beep boop [red herring]  
  - "/*._         _  
    .-*'`    `*-.._.-'  /  
    < * ))     ,            (  
    `*-._`._(__.--*"`.\"

- **Russian**:
  - "POSTF 2024 - FILM" (ПОСТФ 2024 - ФИЛМ)
  - "The professor ordered me to write Russian subtitles." (Профессор приказал мне написать русские субтитры.)
  - "I ask him: 'What is the salary?'" (Я спрашиваю его: «Какая зарплата?»)
  - "He says, 'Experience, student.'" (Он говорит: «Опыт, студент».)
  - "I tell him to go to hell." (Я говорю ему, чтобы он пошел к черту.)
  - "But he doesn't understand." (Но он не понимает.)
  - "зщсеаХгцыз_50_17_6035b"

Let’s try and guess by reading[Russian DF400.txt](Resources/Russian%20DF400.txt):
- "poctf{uwsp_50_17_6035}"

I got it on the first try, but as this is a Level 400 challenge, I'm inclined to look at all the subtitles as it could be something interesting.

I downloaded the subtitles for all languages from [this website](https://views4you.com/tools/youtube-subtitles-downloader/) and generated an automated Python script to translate and save them in a text file for easier reading.

The English subtitle file, funny enough, only contained a red herring.

- The **Arabic subtitles** translate to the trailer of a movie, *Boneyard (2024)*.
- The **Bangla subtitles** translate to basic instructions.
- The **Russian subtitles** contain the flag.

### **Flag**

`poctf{uwsp_50_17_6035}`

---