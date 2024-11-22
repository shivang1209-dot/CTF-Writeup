## **Challenge Name: BASEic Encryption 101**  

### **Solves**  
- **Solves**: 20
- **Points**: 300  

---

### **Description**  
We intercepted this message from a secure CyberCorp communications channel. Unfortunately, it looks like it's encoded in some weird format. Can you help us out?

661916610223539415142000000634030248871388513406397818523288057308

Oh, one last thing. Not sure what it means, but you might find this message useful too. It was sent together with the one above.

0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~¢£¤¥¦§¨
---

### **Approach**  

The given string when looked at first looks like some encoding, i tried Base62, and then tried to convert Decimal to ASCIi but it didn't work.

Then, i looked at the second string provided, which probably is the character set from which the message has been made, there are 94 unique characters there and if we split the given encoded string into pairs of 2, none of them would exceed that value. So, maybe it's just simple mapping?

So, I jotted down a python script to do the same thing. But, that didn't yield any fruitful result -  "&jgZ2nR£fek006y32M_d`Py6D<iQw`5-8".

---

### **Answer**  
```

```  