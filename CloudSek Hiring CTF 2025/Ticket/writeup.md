# Ticket - CTF Writeup

## Challenge Description

Strike Bank recently discovered unusual activity in their customer portal. During a routine review of their Android app, several clues were uncovered. Your mission is to investigate the information available, explore the associated portal, and uncover the hidden flag. Everything you need is already out there! Connect the dots and complete the challenge.

**Android Package:** `com.strikebank.netbanking`  
**Security Review Platform:** bevigil.com  
**Report URL Format:** `https://bevigil.com/report/<package_name>`

---

## Step 1: Accessing the Security Report

The challenge mentions a security review via bevigil.com. We access the security report for the Android package:

**Report URL:** `https://bevigil.com/report/com.strikebank.netbanking`

The report contains security findings, API endpoints, URLs, and other information extracted from the Android app.

---

## Step 2: Extracting Hardcoded Strings

From the bevigil report, we access the `strings.xml` file:

**URL:** `https://bevigil.com/src/com.strikebank.netbanking/source%2Fresources%2Fres%2Fvalues%2Fstrings.xml`

![Strings](./Resources/strings.png)

**Critical Strings Found:**

1. **Base URL:**
   ```xml
   <string name="base_url">http://15.206.47.5.nip.io:8443/</string>
   ```

2. **Internal Credentials:**
   ```xml
   <string name="internal_username">tuhin1729</string>
   <string name="internal_password">123456</string>
   ```

3. **JWT Secret (Base64 Encoded):**
   ```xml
   <string name="encoded_jwt_secret">c3RyIWszYjRua0AxMDA5JXN1cDNyIXMzY3IzNw==</string>
   ```
   **Base64 Decoded:** `str!k3b4nk@1009%sup3r!s3cr37`

---

## Step 3: Accessing the Portal

We navigate to the portal using the discovered base URL:

![Assets](./Resources/assets.png)

**Portal URL:** `http://15.206.47.5.nip.io:8443/`

This reveals a login portal for the STRIKE Netbanking system.

---

## Step 4: Initial Login

Using the hardcoded credentials, we log in:

**Credentials:**
- Username: `tuhin1729`
- Password: `123456`

**Response:**
```
HTTP/1.1 302 Found
Set-Cookie: auth=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InR1aGluMTcyOSIsImV4cCI6MTc2NTAwMDQ2M30.9BhunerACR821eSmlwRGpa1QU2nOUEIeFa0cOtOtLGo
Location: index.php
```

The server sets a JWT token in the `auth` cookie. The JWT contains the username `tuhin1729`.

---

## Step 5: Forging Admin JWT Token

Since we have the JWT secret key, we can forge our own JWT tokens. We create a new JWT with admin privileges:

![JWT Secret](./Resources/secret-key-verified.png)

**JWT Payload:**
- Algorithm: `HS256`
- Payload: `{"username": "admin", "exp": <future_epoch_timestamp>}`
- Secret: `str!k3b4nk@1009%sup3r!s3cr37`

Using a JWT encoding tool (jwt.io), we generate a new admin JWT token.

![JWT Admin Token](./Resources/admin-token-obtained.png)

---

## Step 6: Admin Access and Flag Retrieval

We intercept the request using Burp Suite and replace the `auth` cookie value with our forged admin JWT token.

**Result:** Successfully authenticated as admin, granting access to the admin panel where the flag is located.

![Admin Token Obtained](./Resources/received-flag.png)

---

## Flag

```
ClOuDsEk_ReSeArCH_tEaM_CTF_2025{ccf62117a030691b1ac7013fca4fb685}
```

---

## Solution Script

See [solve.py](./Resources/solve.py) for an automated solution script.
