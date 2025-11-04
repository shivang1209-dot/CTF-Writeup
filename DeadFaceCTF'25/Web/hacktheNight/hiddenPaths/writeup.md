## **Challenge Name: hiddenPaths**

### **Description**

NVU claims that they need their site SEO-optimized and that their site needs to allow web crawlers to access certain directories. But we're almost certain this gave DEADFACE the intel they needed to plan their attack on the site. Find the flag associated with the document that web crawlers are meant to access.

Submit the flag as deadface{flag text}.

**Challenge URL**: `http://env01.deadface.io:8080`

---

### **Approach**

1. **Understanding the Hint**  
   - The description mentions "web crawlers" and "SEO-optimized"
   - This hints at the `robots.txt` file, which web crawlers use to understand which directories they can access

2. **Accessing robots.txt**  
   - Visited the robots.txt endpoint:
     ```
     http://env01.deadface.io:8080/robots.txt
     ```

3. **Finding the Flag**  
   - The robots.txt file contained:
     ```
     # Night Vale University - robots.txt
     # VULNERABILITY: Information disclosure via robots.txt (Easy)
     
     User-agent: *
     Disallow: /admin.php
     Disallow: /api/
     Disallow: /backup/
     Disallow: /config/
     Disallow: /.git/
     Disallow: /secret_files/
     
     # Flag: deadface{r0b0ts_txt_r3v34ls_h1dd3n_p4ths}
     
     # Development endpoints (should be removed in production)
     Disallow: /api/debug.php
     Disallow: /phpinfo.php
     
     # Sitemap
     Sitemap: https://nvu.edu/sitemap.xml
     ```
   - The flag was directly in the robots.txt file

---

### **Flag**

```
deadface{r0b0ts_txt_r3v34ls_h1dd3n_p4ths}
```

---

