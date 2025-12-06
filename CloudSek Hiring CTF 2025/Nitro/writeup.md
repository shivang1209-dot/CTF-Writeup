# Nitro - 100 Points

**Challenge Description:** Ready your scripts! Only automation will beat the clock and unlock the flag.

**Challenge URL:** http://15.206.47.5:9090

## Overview

This challenge requires automated script execution to solve within a strict time limit. Manual attempts will fail due to the timer constraints.

## Initial Reconnaissance

Visiting the challenge homepage reveals the following instructions:

```
Nitro Automation Brief
When you visit the hidden API at /task, it hands back an HTML snippet containing the current random string. Reverse the string, base64-encode the reversed value, wrap it as CSK__{{payload}}__2025, and POST the result to /submit before the timer expires. Manual attempts miss the window—only code will do.

You'll receive either the flag or a "too slow" message. Build a loop that fetches fresh prompts, transforms them, and submits the formatted answer immediately. The server keeps you honest with a strict per-session timer.

Tip: Use raw text or form fields; the endpoint only cares about the value being exact. Watch your encodings.

Can your automation keep up?
```

## Understanding the Challenge

The challenge requires:
1. Fetching a random string from `/task` endpoint
2. Reversing the string
3. Base64-encoding the reversed string
4. Wrapping it in the format: `CSK__{{base64_encoded}}__2025`
5. POSTing the result to `/submit` endpoint
6. Repeating this process until the flag is received

## Solution Approach

### Step 1: Manual Testing

First, let's understand the flow with an example:

**Input string:** `OJvBMWophx6z`

1. **Reverse:** `OJvBMWophx6z` → `z6xhpoWMBvJO`
2. **Base64 encode:** `z6xhpoWMBvJO` → `ejZ4aHBvV01CdkpP`
3. **Wrap:** `CSK__ejZ4aHBvV01CdkpP__2025`

### Step 2: Automation Script

Since manual attempts are too slow, we need to automate the entire process:

- Use a session to maintain cookies and timer state
- Continuously fetch from `/task`, extract the string, transform it, and submit
- Stop when the flag is received

The key points:
- The `/submit` endpoint accepts raw text with `Content-Type: text/plain`
- The server uses a strict per-session timer
- The response contains the flag when successful

## Solution

See [solve.py](./Resources/solve.py) for the automation script.

## Flag

```
ClOuDsEk_ReSeArCH_tEaM_CTF_2025{ab03730caf95ef90a440629bf12228d4}
```