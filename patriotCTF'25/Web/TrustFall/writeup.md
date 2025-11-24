## **Challenge Name: Trust Fall**

### **Description**

This website is a trust exercise! We've given you the username and password, and we trust you'll be able to find the flag.

**Challenge author**: Sid Kumar

**Challenge URL**: `http://18.212.136.134:3000/`

---

### **Approach**

1. **Initial Access**  
   - Accessed the login page at the challenge URL
   - Found a login form with username and password fields
   - The hint suggests credentials are provided: `testuser:pass123`

2. **Authentication**  
   - Logged in with the provided credentials: `testuser:pass123`
   - Successfully authenticated and accessed the product catalog dashboard

3. **Exploring the Dashboard**  
   - Found a product catalog interface with an admin console link
   - Attempted to access the admin console but received a 403 Forbidden error:
     ```
     HTTP/1.1 403 Forbidden
     Unauthorized
     ```
   - The admin console requires elevated privileges

4. **Discovering Backup Files**  
   - Noticed hints about backup files in error messages
   - Attempted to access backup files using URL encoding:
     ```
     http://18.212.136.134:3000/assets/%C0.bak
     ```
   - Received error messages revealing application structure

5. **API Endpoint Enumeration**  
   - Explored the application's API endpoints
   - Discovered a user information endpoint at `/api/users/0`
   - Made a request to this endpoint:
     ```bash
     curl http://18.212.136.134:3000/api/users/0
     ```
   - Successfully retrieved the flag from the API response

---

### **Flag**

```

```

---

