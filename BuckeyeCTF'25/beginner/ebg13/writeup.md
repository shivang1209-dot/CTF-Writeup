# Challenge Name: ebg13

## Description

This is a good web challenge to start with. Use the help button to ask for a hint if you get stuck.

**Challenge URL:** `https://ebg13.challs.pwnoh.io`

---

## Writeup

### Step 1: Understanding the Application

The challenge name "ebg13" is a hint - it's ROT13 encoded "rot13". The application has an endpoint `/ebj13` that:
- Takes a URL parameter
- Fetches the content from that URL
- Applies ROT13 encoding to text nodes in the HTML
- Returns the ROT13-encoded result

### Step 2: Identifying the Vulnerability

The application has a Server-Side Request Forgery (SSRF) vulnerability:
- The `/ebj13` endpoint fetches any URL without proper validation
- There's an `/admin` endpoint that only returns the flag when accessed from localhost (127.0.0.1)

### Step 3: Exploiting SSRF

The flag name hints at using the website on itself. We can:
1. Use `/ebj13` to make the server fetch its own `/admin` endpoint
2. Since the fetch happens server-side, the request appears to come from localhost
3. The `/admin` endpoint will return the flag
4. The response is ROT13-encoded, so we need to decode it

### Step 4: Solution

**Payload:**
```
https://ebg13.challs.pwnoh.io/ebj13?url=http://127.0.0.1:3000/admin
```

The response will be ROT13-encoded. Decode it to extract the flag.

**Solution Script:**
The `solve.py` script automates this process:
1. Makes a request to `/ebj13` with the localhost admin URL
2. Receives the ROT13-encoded response
3. Decodes the ROT13 encoding
4. Extracts the flag using regex

---

## Flag

```
bctf{what_happens_if_i_use_this_website_on_itself}
```

---

