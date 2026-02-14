# Challenge Name: Trapped

## Description

**Category:** Misc (Beginner) | **Points:** 50 | **Author:** x03e

```
Strict restrictions to earn the flag.

usr: trapped | pswd: password

Suffering ends in 27 minutes.
ssh -o StrictHostKeyChecking=no undefined@chall.0xfun.org -p24527
cd ctf
ssh -o StrictHostKeyChecking=no trapped@chall.0xfun.org -p24527
```

---

## Writeup

### Step 1: Initial access

We connect using the provided credentials:

```bash
ssh trapped@chall.0xfun.org -p24527
Password: password
```

Initially, the shell appears non-interactive or restricted. Forcing a proper TTY fixes it:

```bash
ssh -tt trapped@chall.0xfun.org -p24527
```

We now get a usable shell:

```
trapped@container:~$
```

---

### Step 2: Enumeration

Listing the home directory:

```bash
ls -la
```

Output:

```
----r-----+ 1 root root 27 flag.txt
```

Key observations:

* `flag.txt` is owned by `root`
* No read permission for `trapped`
* A `+` appears at the end of permissions

The `+` indicates **extended ACLs** are set.

Attempting to read the file:

```bash
cat flag.txt
```

Results in:

```
Permission denied
```

So normal UNIX permissions block access.

---

### Step 3: Check /etc/passwd

Check system users:

```bash
cat /etc/passwd
```

We notice something interesting:

```
secretuser:x:1001:1001:Unc0ntr0lled1234Passw0rd:/home/secretuser:/bin/sh
```

The **GECOS field** (comment field) contains:

```
Unc0ntr0lled1234Passw0rd
```

This is highly suspicious and clearly placed intentionally.

---

### Step 4: User pivot

Attempt switching to `secretuser`:

```bash
su secretuser
```

Password:

```
Unc0ntr0lled1234Passw0rd
```

Success:

```
secretuser@container:$
```

Verify:

```bash
id
```

```
uid=1001(secretuser)
```

---

### Step 5: Why this works

Earlier we saw:

```
----r-----+ flag.txt
```

The `+` indicated an **ACL**.

Looking at `/start.sh` in `/`:

```bash
setfacl -m u:$SECRET_USER:r /home/$USER1/flag.txt
```

This reveals:

* The flag file grants read permission to `$SECRET_USER`
* `$SECRET_USER` is `secretuser`
* `$USER1` is `trapped`

Therefore:

> `secretuser` has explicit ACL-based read permission on `/home/trapped/flag.txt`.

---

### Step 6: Read the flag

Now as `secretuser`:

```bash
cat /home/trapped/flag.txt
```

Output:

```
0xfun{4ccess_unc0ntroll3d}
```

---

## Resources

No local files; challenge is fully remote (SSH).

---

## Flag

```
0xfun{4ccess_unc0ntroll3d}
```

---

## Lessons learned

This beginner challenge teaches:

* Always enumerate `/etc/passwd`
* The GECOS field may contain sensitive data
* `+` in `ls -l` output means **ACLs**
* Not all access issues require privilege escalation
* Credential leakage is often easier than exploitation

No exploits were required — just proper enumeration and understanding Linux permissions.

---

