# Challenge Name: awklet

## Description

Well this is awkward...

**Challenge URL:** `https://awklet.challs.pwnoh.io`

---

## Writeup

### Step 1: Understanding the Application

The application uses an AWK script (`awklet.awk`) to process requests. It takes parameters:
- `name` - A name parameter
- `font` - A font file path

The application appends `.txt` extension to the font path.

### Step 2: Identifying the Vulnerability

The vulnerability is a **Local File Inclusion (LFI)** issue:
- We control the `font` parameter
- The application reads files based on this parameter
- However, it appends `.txt` extension, which limits what we can read

### Step 3: Bypassing the Extension Check

To bypass the `.txt` extension, we can use a null byte or special character. The solution uses `%` at the end of the path, which can nullify further processing in some contexts.

### Step 4: Exploiting LFI

We can read files from the server, such as:
- `/proc/self/environ` - Environment variables (may contain flags or secrets)
- Other sensitive files

**Payload:**
```bash
curl "https://awklet.challs.pwnoh.io/cgi-bin/awklet.awk?name=test&font=/proc/self/environ%" --output out
```

The `%` at the end helps bypass the `.txt` extension check.

### Step 5: Extracting the Flag

Reading the output file reveals environment variables, which contain the flag.

---

## Flag

```
bctf{n3xt_t1m3_1m_wr171ng_1t_1n_53d}
```

---

