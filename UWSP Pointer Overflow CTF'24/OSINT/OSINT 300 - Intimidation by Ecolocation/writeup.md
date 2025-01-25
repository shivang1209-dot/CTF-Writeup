## **Challenge Name: OSINT 300 - Intimidation by Ecolocation**

---

### **Description**

Your objective for this challenge will be in three parts:

1. **Find the user**:  
   Locate the user with the username `0tYGJH2E`. Do not contact anyone regarding this challenge, as the account used is not monitored.
   
2. **Find the location of the flag**:  
   Identify the correct URL.

3. **Find the password to access the flag**:  
   Decode the location indicated in the provided image. Look for a sign where the arrow points, and the words on the sign are the password.  
   Example: If the sign reads "Employee Parking Only," the password is `EmployeeParkingOnly`.

---

### **Approach**

#### **Part 1: Username Lookup**
1. Used the username `0tYGJH2E` to perform OSINT-based username searches via tools like `Sherlock`.
2. Discovered a profile on **Mastodon** (`mastodon.social`).
3. On the user's page, found a **map** and a **video** containing critical clues.

---

#### **Part 2: Locate the Flag**
1. In the video on the Mastodon page, noticed a URL:  
   **`https://pastebin.com/0tYGJH2E`**  
   The page initially displayed partial flag text:  
   `poctf{uwsp_`
   
2. Accessing the page prompted for a password, indicating further steps were needed.

---

#### **Part 3: Find the Password**
1. Analyzed the image in the challenge, focusing on the location of the arrow pointing toward a sign.
2. Researched location hints (`OldBalt.Rd`, `North Maryland`, etc.) using Google Maps.  
   Identified **West Old Baltimore Road** in Maryland.

3. Navigated Google Street View to find the exact location.  
   Discovered a sign with the text:  
   **`HOV LANE ENDS`**

4. Used the sign's text, formatted without spaces, as the password:  
   **`HOVLANEENDS`**

---

### **Unlocking the Flag**
1. Entered the password `HOVLANEENDS` on Pastebin.
2. Successfully accessed the full flag.

---

### **Flag**

`poctf{uwsp_1_4m_7h3_0n3_wh0_kn0ck5}`

---