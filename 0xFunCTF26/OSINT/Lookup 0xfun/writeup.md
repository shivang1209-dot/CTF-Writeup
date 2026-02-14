# Challenge Name: Lookup 0xfun

## Description

**Category:** OSINT

> This event takes place on **ctf.0xfun.org**, but you can easily find it by searching.

**Flag format:** `0xfun{...}`

---

## Writeup

### Step 1: DNS Lookup

Perform a **DNS TXT record** lookup for the domain `ctf.0xfun.org`:

```bash
nslookup -type=TXT ctf.0xfun.org
```

### Step 2: Reading the TXT Records

The response includes TXT records. One of them contains the flag in plain text:

```
ctf.0xfun.org   text = "0xfun{4ny_1nfo_th4ts_pub1cly_4cc3ss1bl3_1s_0S1NT}"
```

---

## Resources

No local files — this is a DNS-based challenge.

---

## Flag

```
0xfun{4ny_1nfo_th4ts_pub1cly_4cc3ss1bl3_1s_0S1NT}
```
