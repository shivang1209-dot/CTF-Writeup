# Challenge Name: Big Chungus

## Description

There's wabbit twouble afoot

**Challenge URL:** `https://big-chungus.challs.pwnoh.io`

---

## Writeup

### Step 1: Understanding the Challenge

The challenge checks if `req.query.username.length > 0xB16_C4A6A5` (which equals 47,626,626,725 in decimal). This is an impossibly large number for a normal string length, as JavaScript strings have a maximum length of approximately 2^30 - 24 (~1.07 billion characters).

### Step 2: Identifying the Vulnerability

The vulnerability lies in how Express.js parses query parameters. Express uses the `qs` library, which supports bracket notation to create nested objects. By sending `?username[length]=<value>`, we can create an object where `req.query.username` is `{length: <value>}` instead of a string.

### Step 3: Exploiting Query Parameter Parsing

When the code checks `req.query.username.length`, if `username` is a string, it checks the string length. However, if `username` is an object with a `length` property, it will read that property value instead.

### Step 4: Solution

Send a query parameter using bracket notation to set the `length` property directly:

```
?username[length]=47626626726
```

This creates `req.query.username = {length: 47626626726}`, so when the code checks `req.query.username.length`, it evaluates to `47626626726`, which is greater than the threshold `0xB16_C4A6A5` (47626626725).

### Step 5: Getting the Flag

**URL:** `https://big-chungus.challs.pwnoh.io/?username[length]=47626626726`

This triggers the "BIG CHUNGUS" response page which displays the flag.

---

## Flag

```
bctf{b16_chun6u5_w45_n3v3r_7h15_b16}
```

---

