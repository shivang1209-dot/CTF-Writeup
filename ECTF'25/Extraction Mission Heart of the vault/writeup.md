## **Challenge Name**: Extraction Mission: Heart of the Vault

---

### Description

The challenge revolves around a series of encrypted zip files, each containing another zip file, and the task is to decrypt them all to finally obtain the flag. The challenge provides encrypted zip files, and your mission is to crack through these vaults one by one. The challenge is divided into two parts, and in the second part, you need to read through the files for hints. The description suggests that we need to keep track of all the passwords, and there may be a pattern in how they are used.

---

### Steps to Solve

#### Part 1: Cracking the First Encrypted ZIP

1. **Initial ZIP File**:
   You are given an encrypted zip file. The first task is to crack its password. Using the `zip2john` tool, we extract the hash of the encrypted zip file:

   ```bash
   zip2john first.zip > first_hash.txt
   ```

2. **Cracking the Password**:
   Once we have the hash, we can use `john the ripper` with a wordlist like `rockyou.txt` to crack the password:

   ```bash
   john --wordlist=/path/to/rockyou.txt first_hash.txt
   ```

   This gives us the password for the first zip file. Upon cracking, we get the file `something_199.zip`, which is also encrypted.

---

#### Part 2: Automating the Decryption Process

3. **Automating with a Script**:
   Since there are 200 encrypted zip files, manually cracking each would be tedious. You can use the provided Python [script](Resources/script.py) to automate the decryption process. This script will:

   - Take the password cracked from the first zip.
   - Decrypt the next zip file.
   - Store all cracked passwords for future use.
   - Repeat the process until all 200 zip files are decrypted.

   The script essentially works by iterating through the zips, unzipping one after another, and obtaining new passwords.

   After running the script, we have the following two files:

   - `mining_report.txt`
   - `drop_pod.py`

   The passwords cracked during this process are stored in `cracked_passwords.txt`.

---

#### Part 3: Reversing the Logic in `drop_pod.py`

4. **Understanding drop_pod.py**:
   The `drop_pod.py` script is central to finding the flag, but we need to understand its logic first. The script relies on a list called `crew_list`, which is redacted. We now know that the `crew_list` contains the passwords cracked earlier.

5. **Using the Cracked Passwords**:
   Initially, the passwords in `cracked_passwords.txt` are in the order they were cracked. However, based on the hint, the order may be reversed (from 200 to 1).

   So, we create a new Python script, `solve.py`, which reverses the cracked passwords list and feeds it into `crew_list` in the `drop_pod.py` script.

   ```python
   # solve.py
   with open('cracked_passwords.txt') as f:
       passwords = f.readlines()

   # Reverse the passwords
   passwords = passwords[::-1]

   # Insert reversed passwords into drop_pod.py's logic
   # Assuming drop_pod.py uses passwords in a certain format, pass them here
   ```

6. **Running the Script**:
   Running `solve.py` after reversing the password list gives us the flag.

---

### Flag

The flag is: `ECTF{d1ggy_d1ggy_h0l3}`

---
