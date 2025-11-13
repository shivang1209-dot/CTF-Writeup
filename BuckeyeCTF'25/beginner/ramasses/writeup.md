# Challenge Name: ramasses

## Description

This is a good web challenge to start with. Use the help button to ask for a hint if you get stuck.

Do you dare enter the tomb of Pharaoh Dave Ramesses?

**Challenge URL:** `https://ramesses.challs.pwnoh.io`

---

## Writeup

### Step 1: Exploring the Application

The challenge is a web application themed around an Egyptian tomb. We can log in with any credentials, which suggests the authentication might be weak or the session management is flawed.

### Step 2: Inspecting the Cookie

After logging in, we receive a cookie. Let's examine it:

```
eyJuYW1lIjogIiR7ezcqN319IiwgImlzX3BoYXJhb2giOiBmYWxzZX0=
```

This looks like Base64-encoded JSON. Decoding it reveals:
```json
{"name": "${{7*7}}", "is_pharaoh": false}
```

The name field contains a template injection attempt (`${{7*7}}`), but more importantly, we can see the cookie structure.

### Step 3: Cookie Manipulation

The cookie contains:
- `name`: The username
- `is_pharaoh`: A boolean flag indicating if the user is a pharaoh

To get the flag, we need to:
1. Change `name` to `"admin"`
2. Change `is_pharaoh` to `true`

Creating the new cookie:
```json
{"name": "admin", "is_pharaoh": true}
```

Base64 encoding:
```
eyJuYW1lIjogImFkbWluIiwgImlzX3BoYXJhb2giOiB0cnVlfQ==
```

### Step 4: Getting the Flag

Modify the cookie value in the browser (or using a tool like Burp Suite) and refresh the page. The application will recognize us as the pharaoh and display the flag.

---

## Flag

```
bctf{s0_17_w45_wr177en_50_1t_w45_d0n3}
```

---

