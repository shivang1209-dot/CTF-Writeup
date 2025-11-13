# Challenge Name: authman

## Description

This is a web challenge involving authentication mechanisms.

**Challenge URL:** `https://authman.challs.pwnoh.io`

**Files:**
- `cookies.txt` - Contains captured authentication data
- `solve.py` - Solution script

---

## Writeup

### Step 1: Understanding the Challenge

The challenge involves HTTP Digest Authentication. The `cookies.txt` file shows captured authentication headers:

```
Headers:
  Authorization: Digest username="keno", realm="authman", nonce="a93ddafd9bea19b78a902e05dfab749d", uri="/auth", response="acf94a53eab4fba8a59db4f7894d9522", qop="auth", nc=00000001, cnonce="d5645b4042bde0d5"
```

### Step 2: Analyzing the Captured Data

From the captured data, we can see:
- Username: `keno`
- Realm: `authman`
- Digest authentication response
- Cookie value that needs to be forwarded

### Step 3: Replaying the Authentication

The solution involves:
1. Using the captured Authorization header
2. Forwarding it with the appropriate cookie
3. Making a request to `/auth` endpoint

### Step 4: Solution Script

The `solve.py` script:
1. Connects to `authman.challs.pwnoh.io`
2. Sends a GET request to `/auth`
3. Uses the captured Authorization header with updated nonce and response
4. Includes the captured cookie value
5. Extracts the flag from the response

**Key Points:**
- The Authorization header needs to be updated with a new nonce from the server
- The cookie must be included in the request
- The response contains the flag

---

## Flag

The flag is returned in the response after successfully authenticating with the captured credentials.

`bctf{a_new_dog_learns_old_tricks}`

---

