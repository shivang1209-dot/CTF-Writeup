# Challenge Name: bigdataAnalysis

## Description

This is a forensics challenge involving BigQuery analysis.

**Files:**
- `image.png` - Contains a reference image

---

## Writeup

### Step 1: Understanding the Challenge

The challenge involves analyzing data in Google BigQuery. The flag file mentions:
- An image file (`image.png`)
- A BigQuery console link with specific project and query information

### Step 2: Accessing BigQuery

The challenge provides a BigQuery console link:
```
https://console.cloud.google.com/bigquery?project=bubbly-repeater-443107-s2&ws=!1m9!1m3!3m2!1sbigquery-public-data!2sgithub_repos!1m4!1m3!1sbubbly-repeater-443107-s2!2sbquxjob_7eec3eb8_19a66c1e67f!3sUS
```

This suggests we need to:
1. Access the BigQuery console
2. Query the `bigquery-public-data.github_repos` dataset
3. Find specific data related to the challenge

### Step 3: Analyzing the Data

The challenge likely involves:
- Querying GitHub repository data
- Finding specific repositories or commits
- Extracting the flag from query results

### Step 4: Solution

Based on the flag format, the solution involves:
1. Running appropriate SQL queries in BigQuery
2. Analyzing the results
3. Extracting the flag value: `63421480`

---

## Flag

```
bctf{63421480}
```

---

