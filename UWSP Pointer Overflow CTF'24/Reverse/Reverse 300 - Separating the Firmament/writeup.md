## **Challenge Name: Reverse 300 - Separating the Firmament**  

---

### **Description**  

I think it's time to mix things up a little bit. This time, I'm going to give you an application that will reveal the flag. All you have to do is guess the right key. Shouldn't be too hard - 22 characters, A-Z, a-z, 0-9, !-*

I know what you're thinking. "This isn't a crack challenge." I know, but I'm out of ideas for challenges and I'm phoning this one in. Just crack the stupid key. Your only other choice is to either decompile and reverse engineer the key (boring), or grab it from the running process when it validates (impossible.) Cracking passwords is way more fun (sigma gigachad move.)

#### **File Provided**  
- [Reverse300-1](Resources/Reverse300-1)  

---

### **Approach**  

The program is designed to encrypt a flag using a key and later decrypt it if the user provides the correct key. The solution requires understanding the steps the program takes to reconstruct the encryption key, validate it, and decrypt the flag.  

Let's look at main() first.

```c
int32_t main(int32_t argc, char** argv, char** envp)
{
    printf("Enter the key to decrypt the fla...");
    void var_28;
    __isoc99_scanf("%22s", &var_28);
    
    if (strlen(&var_28) != 0x16)
    {
        puts("Incorrect key length. Key must b...");
        return 1;
    }
    
    void var_48;
    reconstruct_key(&var_48);
    
    if (strcmp(&var_28, &var_48))
        puts("Incorrect key. Try again.");
    else
        decrypt_flag(&var_48);
    
    return 0;
}
```

The program first prompts the user to input a key. The key must be 22 characters long, as the encryption algorithm relies on processing exactly 22 bytes for generating the decryption key; otherwise, the program terminates with an error message. If the key is the correct length, the program reconstructs the expected key using the `reconstruct_key()` function and compares it to the user-provided key. If they match, the program decrypts and displays the flag using `decrypt_flag()`.

#### Key Reconstruction

The `reconstruct_key()` function generates the expected key by performing XOR operations on predefined values:

```c
void reconstruct_key(void* arg1)
{
    int32_t var_1d;
    __builtin_strncpy(&var_1d, "tsxvg", 5);
    int32_t var_22 = 0x3d3b1f08;
    char var_1e = 0x2f;
    int32_t var_27 = 0x1186a70;
    char var_23 = 0x50;
    int32_t var_2e = 0x656e1a66;
    var_2e = 0x734d1665;
    
    for (int32_t i = 0; i <= 4; i += 1)
        *(arg1 + i) = *(&var_1d + i) ^ 0x10;
    
    for (int32_t i_1 = 0; i_1 <= 4; i_1 += 1)
        *(arg1 + i_1 + 5) = *(&var_22 + i_1) ^ 0x5a;
    
    for (int32_t i_2 = 0; i_2 <= 4; i_2 += 1)
        *(arg1 + i_2 + 0xa) = *(&var_27 + i_2) ^ 0x20;
    
    for (int32_t i_3 = 0; i_3 <= 6; i_3 += 1)
    {
        char rsi_1;
        
        if (i_3 > 4)
            rsi_1 = 0;
        else
            rsi_1 = 0x30;
        
        *(arg1 + i_3 + 0xf) = rsi_1 ^ *(&var_2e + i_3);
    }
}
```

- The key is divided into four segments, each derived from a predefined value.
- Each segment is XORed with a specific constant to generate the key bytes.
- The function uses loops to process each segment.

#### Flag Decryption

The `decrypt_flag()` function decrypts the flag using the reconstructed key:

```c
int64_t decrypt_flag(char* arg1)
{
    int64_t var_38;
    __builtin_memcpy(&var_38, "\x14\x0c\x0b\x12\x11\x29\x30\x16\x14\x05\x0f\x7d\x50\x12\x2f\x21\x1a\x2c\x39\x42\x12\x42\x51\x3c\x5c\x39\x42\x65\x71\x57\x54\x08", 0x20);
    xor_encrypt(&var_38, 0x20, arg1, strlen(arg1));
    return printf("The flag is: %s\n", &var_38);
}
```

- The encrypted flag is stored in `var_38`.
- The `xor_encrypt()` function performs XOR operations on each byte of the encrypted flag using the reconstructed key.
- Finally, the decrypted flag is printed.

#### XOR Encryption

The `xor_encrypt()` function processes the encryption/decryption:

```c
void* xor_encrypt(int64_t arg1, int64_t arg2, int64_t arg3, int64_t arg4)
{
    void* i;
    
    for (i = nullptr; i < arg2; i += 1)
        *(i + arg1) ^= *(arg3 + COMBINE(0, i) % arg4);
    
    return i;
}
```

- Each byte of the input data (`arg1`) is XORed with the corresponding byte of the key (`arg3`).
- The key is cyclically repeated using the modulus operation (`% arg4`).
- The process ensures symmetric encryption and decryption.

Now, we'll use this [python script](Resources/script.py) to obtain the flag.

---

### **Flag**  

`poctf{uwsp_7h3_w0rlB5_4_57463}`  

---