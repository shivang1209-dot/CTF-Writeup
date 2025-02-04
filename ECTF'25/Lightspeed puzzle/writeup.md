### Challenge Name: Lightspeed Puzzle  

#### Description:  
We've been told you're good at puzzles, so we're going to test that with a small 100-piece puzzle.  

Solve the puzzle and enter the code written on it in less than 10 seconds to get the flag.  

**Instance Deployment:**  
Deploy an instance: [https://instances.ectf.fr](https://instances.ectf.fr)  
Instance URL: [http://instances.ectf.fr:21555](http://instances.ectf.fr:21555)  

Flag format: `ECTF{....}`  

---

### Solution  

1. **Analyzing the Challenge**  
   - Visiting the website and clicking "Play" presents a **10x10 grid of images** (100 pieces).  
   - Inspecting the source code reveals image URLs following a pattern:  
     ```
     http://instances.ectf.fr:21555/static/1_0.png
     http://instances.ectf.fr:21555/static/9_9.png
     ```
   - The task is to reconstruct the puzzle and read the **hidden code** within 10 seconds.  

2. **Automating the Image Collection**  
   - Manually downloading 100 images is inefficient.  
   - Used a **Python script** to **automate** the downloading and stitching process.  
   - Extracted the code from the assembled image: `"GMBJCI"`  
   - Entered the code, but it **failed**—indicating that **images change per session**.  

3. **Investigating Session Persistence**  
   - Noticed the website **sets two cookies**, one being a **JWT token**.  
   - Decoded the JWT using **CyberChef** and found:  
     ```json
     {"code":"DOBPSB","start_time":1738477448.498426}
     ```
   - The **correct code is embedded in the JWT**.  

4. **Exploiting the JWT Code Leak**  
   - Restarted the instance.  
   - Opened **Developer Tools** (Ctrl+Shift+I → Application).  
   - Copied the **JWT token**, decoded it in **CyberChef**, and extracted the **actual code**.  
   - Entered the correct code within the 10-second window to retrieve the flag.  

---

### Flag:  
```
ECTF{Autom4t3d_PuZz13}
```

---

### Flag:  
```
ECTF{Autom4t3d_PuZz13}
```