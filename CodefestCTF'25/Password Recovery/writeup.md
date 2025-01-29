# Challenge Name: Password Recovery

## Description
> "Back in 2019, I wrote a secret and encrypted it using a password on Republic Day of India. Now I forgot the password :( I only have the passgen utility I used and the encrypted file. Can you help me?"

**Files Provided:**  
- [`encrypted.zip`](./attachment/encrypted.zip)
- [`passgen`](./attachment/passgen)

## Writeup

### Binary Analysis
Decompiling the `passgen` utility in Ghidra reveals critical password generation logic:

```c
// Simplified C code snippet
int main() {
    char charset[] = "abcdefghijklmnoqprstuvwyzxABCDEFGHIJKLMNOQPRSTUYWVZX0123456789";
    srand(time(0));
    
    char password[16];
    for(int i = 0; i < 15; i++) {
        password[i] = charset[rand() % 62];
    }
    password[15] = '\0';
    printf("Password: %s\n", password);
}
```

**Key Insights:**
1. Password length: 15 characters
2. Character set: 62 alphanumeric characters (a-z, A-Z, 0-9)
3. Seed based on current timestamp (`srand(time(0))`)

### Attack Strategy
Since the password was generated on **26th January 2019** (Republic Day):
1. Calculate epoch time range:
   - Start: 1548441000 (2019-01-26 00:00:00 IST)
   - End: 1548527400 (2019-01-27 00:00:00 IST)
2. Total possibilities: 86,400 (24h × 60m × 60s)

### Wordlist Generation
```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    const char charset[] = "abcdefghijklmnoqprstuvwyzxABCDEFGHIJKLMNOQPRSTUYWVZX0123456789";
    const long start_epoch = 1548441000;
    FILE *fp = fopen("wordlist.txt", "w");

    for(long ts = start_epoch; ts < start_epoch + 86400; ts++) {
        srand(ts);
        char pwd[16];
        for(int i=0; i<15; i++) {
            pwd[i] = charset[rand() % 62];
        }
        pwd[15] = '\n';
        fwrite(pwd, 16, 1, fp);
    }
    fclose(fp);
    return 0;
}
```

Compile and execute:
```bash
gcc wordlist.c -o wordlist && ./wordlist
```

### Password Cracking
1. Extract hash:
```bash
zip2john encrypted.zip > hash.txt
```

2. Run John the Ripper:
```bash
john --wordlist=wordlist.txt hash.txt
```

**Successful Output:**
```
kFEbD1Pzxyu69Yw  (encrypted.zip/flag.txt)
```

### Flag Extraction
Unzip with recovered password:
```bash
unzip -P kFEbD1Pzxyu69Yw encrypted.zip
cat flag.txt
```

## Flag
`CodefestCTF{rand_15_n07_4c7ua11y_r4nd0m}`

---
