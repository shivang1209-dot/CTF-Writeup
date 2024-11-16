## **Challenge Name: Spider**

### **Solves**

- **Solves**: 252
- **Points**: 84

### **Description**

Some paths are left deliberately unvisited, shielded from the spider’s web. But what’s intentionally hidden often holds the most valuable secrets.

**URL**: [http://microson.ctf.site:20080](http://microson.ctf.site:20080)

---

### **Approach**

1. **Clue Interpretation**: The description hinted at something hidden, and the mention of a "spider’s web" pointed towards `robots.txt`—a file often used to block web crawlers from accessing certain parts of a website.
2. **Checking robots.txt**: Based on the clue, I visited the `robots.txt` file at:
   [http://microson.ctf.site:20080/robots.txt](http://microson.ctf.site:20080/robots.txt).
3. **Hidden Endpoints**: Inside the file, several endpoints were listed, and one stood out as particularly interesting:
   [http://microson.ctf.site:20080/top_secret_experiments/](http://microson.ctf.site:20080/top_secret_experiments/).
4. **Flag Extraction**: Upon visiting this endpoint, I found a file named `flag1.txt`, which contained the flag.

**File**: [Flag File](./Resources/flag1.txt)

**Flag**: `EKO{classic_but_easy}`

---