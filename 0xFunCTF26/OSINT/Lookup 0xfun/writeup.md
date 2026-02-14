# Challenge Name: Lookup 0xfun

## Description

This event takes place on **ctf.0xfun.org**, but you can easily find it by searching.

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

There may also be a record such as `v=spf1 include:mailgun.org ~all`. The flag is in the first record above.

---

## Flag

```
0xfun{4ny_1nfo_th4ts_pub1cly_4cc3ss1bl3_1s_0S1NT}
```

---
