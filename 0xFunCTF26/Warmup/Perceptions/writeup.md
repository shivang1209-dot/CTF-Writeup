# Challenge Name: Perceptions

## Description

**Category:** Warmup

> Take a look at the blog I created! It has a neat backend and, interestingly, seems to use fewer ports.

**Challenge URL:** `http://chall.0xfun.org:56932`

**Flag format:** `0xfun{...}`

---

## Writeup

### Step 1: Exploring the Application

The site serves blog pages at paths like `/<TOKEN>/page.html`. A `/name` endpoint returns the blog owner's name (e.g. "Charlie"). Different tokens lead to different content.

### Step 2: Finding the Secret Path

By following links or enumerating tokens, we discover a path that reveals a "secret" page. One such path contains a reference to a directory or file like `secret_flag_333`.

### Step 3: Accessing the Secret Directory

Request the secret path. The backend appears to be a minimal Linux environment (e.g. container) with "generic Linux remote access."

![Challenge mystery page](Resources/mystery.jpg)

### Step 4: Reading the Flag

From the secret path we can access a file such as `secret_flag_333/flag.txt`. Reading that file yields the flag.

![Flag screenshot](Resources/flag.png)

---

## Resources

- **[Resources/mystery.jpg](Resources/mystery.jpg)** — Screenshot of the mystery/blog page.
- **[Resources/flag.png](Resources/flag.png)** — Screenshot showing the flag.

---

## Flag

```
0xfun{p3rsp3c71v3.15.k3y}
```
