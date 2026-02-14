# Challenge Name: Insanity 1

## Description

**Category:** Misc

> Use the Discord API to query user roles for the given channel ID. Join the 0xFUN CTF Discord server; there is no access to chat history and a fake flag may be shown. **One of the roles** (for the user or channel) is the real flag.

---

## Writeup

### Step 1: Join the Discord Server

Join the 0xFUN CTF Discord server (link from [CTFtime](https://ctftime.org/event/3081) or the challenge).

### Step 2: Identify the Channel

Locate the channel or user referenced in the challenge (channel ID may be given or discoverable).

### Step 3: Query Roles via Discord API

Use the Discord API to query **user roles** for the relevant channel or server. The flag is one of the role names returned.

![Discord role list](Resources/insanity1.png)

### Step 4: Submit the Flag

The correct role name that matches `0xfun{...}` is the flag.

---

## Resources

- **[Resources/insanity1.png](Resources/insanity1.png)** — Screenshot of the Discord role list.

---

## Flag

The flag is one of the Discord roles, in the format `0xfun{...}`.
