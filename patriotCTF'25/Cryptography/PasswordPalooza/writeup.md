## **Challenge Name: Password Palooza**

### **Description**

We were infiltrating a hacker's network to bring down their team, but we've run into a slight issue. We managed to find the manager's password hash, and through some OSINT efforts we discovered that their password was leaked in a popular password breach.

Their password also has two random digits following whatever password was leaked. An example would be password13.

Can you crack their password?

Hash: 3a52fc83037bd2cb81c5a04e49c048a2

The flag format will be pctf{password}

**Challenge author**: DJ Strigel

---

### **Approach**

1. **Initial Analysis**  
   - Provided with an MD5 hash: `3a52fc83037bd2cb81c5a04e49c048a2`
   - The password format: `<breached_password><two_digits>`
   - Example: `password13` (password + two digits)

2. **Identifying the Hash Algorithm**  
   - Analyzed the hash format
   - Confirmed it's an MD5 hash (32 hexadecimal characters)

3. **Understanding the Password Format**  
   - The password consists of:
     - A base password from a popular breach (likely in rockyou.txt)
     - Two random digits appended (00-99)

4. **Creating Custom John Rules**  
   - Created a custom John the Ripper configuration file (`myconfig.conf`)
   - Added a rule to append two digits (00-99) to each word:
     ```
     [List.Rules:Append00to99]
     Az"[00-99]"
     ```
   - This rule appends all two-digit combinations to each wordlist entry

5. **Cracking the Hash**  
   - Used John the Ripper with the custom rules:
     ```bash
     john --config=myconfig.conf \
          --format=raw-md5 \
          --wordlist=/usr/share/wordlists/rockyou.txt \
          --rules=Append00to99 \
          crack
     ```
   - Successfully cracked the hash
   - Found the password: `mr.krabbs57`

6. **Verification**  
   - The password `mr.krabbs57` matches the format:
     - Base password: `mr.krabbs` (from breach)
     - Two digits: `57`

---

### **Flag**

```
pctf{mr.krabbs57}
```

---

