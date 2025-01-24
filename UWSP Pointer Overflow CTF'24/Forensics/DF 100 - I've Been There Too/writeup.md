### **Challenge Name: DF 100 - I've Been There Too**

---

### **Description**

Attached to this challenge is a **SQLite database** file. It's a simulated student database where someone has made a few modifications. While it's theoretical, this classic scenario involves tampering with records such as grades or credits. Your goal is to uncover the hidden changes within the database.

#### **File Provided**  
- [DF100-3.sqlite](https://pointeroverflowctf.com/static/DF100-3.sqlite)

---

### **Approach**

#### **Step 1: Analyzing the SQLite File**
1. Opened the SQLite file:
   ```bash
   sqlite3 DF100-3.sqlite
   ```

2. Listed the available tables:
   ```sql
   .tables
   ```
   **Output:**
   ```
   new_students
   ```

3. Viewed the schema of the `new_students` table:
   ```sql
   .schema
   ```
   **Output:**
   ```sql
   CREATE TABLE new_students (
       id INT PRIMARY KEY,
       name TEXT NOT NULL,
       photo BLOB NOT NULL,
       gpa FLOAT NOT NULL,
       has_covid_vaccine BOOLEAN NOT NULL,
       year_graduated INT NOT NULL
   );
   ```

#### **Step 2: Exploring the Table**
1. Queried all records in the `new_students` table:
   ```sql
   SELECT * FROM new_students;
   ```
   - Found part of the flag (`_dr34m}`) in the `name` field towards the end of the dataset.

2. Queried the `name` column for easier extraction:
   ```sql
   SELECT name FROM new_students;
   ```
   - Scrolled through the results to find all parts of the flag distributed across various entries.

---

### **Flag**

`poctf{uwsp_d0_4ndr01d5_dr34m}`

---
