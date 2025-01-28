## **Challenge Name: Reverse 300 - Beef-Witted Mushrumps**  

---

### **Description**  

For this challenge, I wanted to do something in the vein of simplified memory operations in a simulated virtual machine, and I ended up with this. The binary here takes in custom bytecode, executes it, and prints the output. It won't look like much if you run it, but that doesn't matter for this type of challenge.

Wave 15 update: I've updated the binary. Same operations, but now the program decodes the first five characters of the flag before it halts.

#### **File Provided**  
- [Reverse300-3](Resources/Reverse300-3)  

---

### **Approach**  

.data (PROGBITS) section started  {0x404020-0x40404d}
00404020  __data_start:
00404020  00 00 00 00 00 00 00 00                          ........
00404028  __dso_handle:
00404028                          00 00 00 00 00 00 00 00          ........

00404030  int64_t flag = 0x1760156e087c1f70
00404038  int64_t data_404038 = 0x1f7827147c4b1464

00404040  2b 46 75 2a 1b                                   +Fu*.

00404045  char data_404045[0x4] = ".qE#" 2e 71 45 23

00404049                             13 23 14 69                    .#.i
.data (PROGBITS) section ended  {0x404020-0x40404d}


0x404080 <memory>:      0x1760156e087c1f70      0x1f7827147c4b1464
0x404090 <memory+16>:   0x45712e1b2a75462b      0x0000006914231323


undefined8 main(void)

{
  undefined8 local_38;
  undefined8 local_30;
  undefined8 local_28;
  undefined8 local_20;
  undefined8 local_10;
  
  local_38 = 0x101000601050001;
  local_30 = 0x305020100060205;
  local_28 = 0x6040503010006;
  local_20 = 0xff000605050401;
  local_10 = 0x20;
  initialize_memory();
  execute_vm(&local_38,local_10);
  return 0;
}

void initialize_memory(void)

{
  memset(memory,0,0x100);
  memory._0_8_ = flag;
  memory._8_5_ = (undefined5)DAT_00404038;
  memory._13_3_ = DAT_00404038._5_3_;
  memory._16_5_ = uRam0000000000404040;
  memory._21_8_ = DAT_00404045;
  puts("Memory initialized. Encoded flag loaded.");
  return;
}

void execute_vm(long param_1,ulong param_2)

{
  long lVar1;
  byte bVar2;
  byte bVar3;
  byte local_11;
  ulong local_10;
  
  local_10 = 0;
  local_11 = 0;
  puts("Decoding the flag...");
  while( true ) {
    if (param_2 <= local_10) {
      return;
    }
    lVar1 = local_10 + 1;
    bVar2 = *(byte *)(local_10 + param_1);
    local_10 = local_10 + 2;
    bVar3 = *(byte *)(lVar1 + param_1);
    if (6 < bVar2) break;
    switch(bVar2) {
    case 1:
      local_11 = memory[(int)(uint)bVar3];
      break;
    case 2:
      memory[(int)(uint)bVar3] = local_11;
      break;
    case 3:
      local_11 = local_11 + memory[(int)(uint)bVar3];
      break;
    case 4:
      local_11 = local_11 - memory[(int)(uint)bVar3];
      break;
    case 5:
      local_11 = local_11 ^ memory[(int)(uint)bVar3];
      break;
    case 6:
      putchar((uint)local_11);
      break;
    default:
      goto switchD_004011f2_caseD_6;
    }
  }
  if (bVar2 == 0xff) {
    puts("\nDone.");
    return;
  }
switchD_004011f2_caseD_6:
  printf("Unknown instruction: %02x\n",(ulong)bVar2);
  return;
}


void execute_vm(long param_1,ulong param_2)

{
  long lVar1;
  byte bVar2;
  byte bVar3;
  byte local_11;
  ulong local_10;
  
  local_10 = 0;
  local_11 = 0;
  puts("Decoding the flag...");
  while( true ) {
    if (param_2 <= local_10) {
      return;
    }
    lVar1 = local_10 + 1;
    bVar2 = *(byte *)(local_10 + param_1);
    local_10 = local_10 + 2;
    bVar3 = *(byte *)(lVar1 + param_1);
    if (6 < bVar2) break;
    switch(bVar2) {
    case 1:
      local_11 = memory[(int)(uint)bVar3];
      break;
    case 2:
      memory[(int)(uint)bVar3] = local_11;
      break;
    case 3:
      local_11 = local_11 + memory[(int)(uint)bVar3];
      break;
    case 4:
      local_11 = local_11 - memory[(int)(uint)bVar3];
      break;
    case 5:
      local_11 = local_11 ^ memory[(int)(uint)bVar3];
      break;
    case 6:
      putchar((uint)local_11);
      break;
    default:
      goto switchD_004011f2_caseD_6;
    }
  }
  if (bVar2 == 0xff) {
    puts("\nDone.");
    return;
  }
switchD_004011f2_caseD_6:
  printf("Unknown instruction: %02x\n",(ulong)bVar2);
  return;
}


Analysing the pseudocode for a long time I realised it's just XORing itself by shifting one position and just adding a null byte at the start.

E.g. 0xdeadbeef being XORed with 0x00deadbe.

So, to reverse it we just need the encoded flag and we can XOR it back to get the flag.

Using gdb first disassemble the initialize_memory function to see the address of memory variable.

Added a breakpoint in the main function at execute_vm function after the memory value was initialized. After we hit breakpoint checked the value of the 
memory variable using x/20gx 0x404080.





Contructed Encoded Flag - 701f7c086e156017 64144b7c1427781f 2b46752a1b2e7145 2313231469

So, after understanding the functionality of this binary. We can determine that the current 2 bytes are being XORed with previous 2 bytes and hence when the program is run normally it only produces `octf{` instead of `poctf` which is the standard format. This happens because the first byte is being XORed with null. So the actual first byte gets skipped. 

We'll do the same, XOR the Encoded flag with the encoded flag itself and just removing the last 1 byte (`0x69`) from the key and appending `0x00` byte at the beginning...

Then we perform (701f7c086e15601764144b7c1427781f2b46752a1b2e71452313231469 ^ 00701f7c086e15601764144b7c1427781f2b46752a1b2e714523132314)

Flag - poctf{uwsp_7h3_g4m3_15_4f007}

---

### **Flag**  

`poctf{uwsp_7h3_g4m3_15_4f007}`  

---

## **Challenge Name: Reverse 300 - Beef-Witted Mushrumps**  

---

### **Challenge Overview**  

This challenge revolves around simulating simplified memory operations in a virtual machine. The provided binary file processes custom bytecode, executes operations, and prints output. The challenge's goal is to decode the first five characters of a flag before the program halts, which is what the binary performs after a Wave 15 update. At first glance, the output may not look significant, but this is a classic example of a reverse engineering challenge.

---

### **Files Provided**  

- **Reverse300-3**: This is the binary file provided for analysis.

---

### **Approach**

#### **Memory Layout Analysis**

Upon investigating the memory layout of the binary, we find the following:

- **Data Section (`.data`):**  
  The program starts by defining certain variables in memory:
  - **flag:** This is the primary variable that holds the encoded flag value (`0x1760156e087c1f70`).
  - **data_404038:** Another data variable initialized to `0x1f7827147c4b1464`.
  - **Memory Values:** The memory from address `0x404040` to `0x40404D` contains some byte sequences that are important for the execution.

This memory is initialized with specific data, including the encoded flag. After initialization, the program proceeds to execute instructions based on the bytecode.

#### **Function Breakdown**

1. **`initialize_memory` Function:**  
   This function initializes the memory by loading the flag and other variables into memory locations. It sets the memory to zero and loads the encoded flag and other values, preparing them for the virtual machine's execution.

2. **`execute_vm` Function:**  
   The virtual machine executes instructions encoded in the bytecode. These instructions perform simple memory operations like:
   - Loading and storing values in memory.
   - Performing arithmetic operations.
   - XORing values.
   - Printing characters to the screen.
   
   The function runs in a loop, reading pairs of bytes as instructions. Each byte pair determines the operation to be executed. When the program encounters a specific condition (`0xFF` byte), it halts.

3. **Decoding the Flag:**
   The virtual machine's operations are designed to decode the flag. The process involves XORing the bytes of the encoded flag in a particular manner. By analyzing the binary, it's clear that each byte of the encoded flag is XORed with the previous byte, and the first byte is XORed with a null byte (`0x00`).

#### **Reverse Engineering**

To reverse the encoding process, we must reverse the XOR operations applied to the encoded flag. Here's how:

1. **Examining Memory:**  
   Using **GDB**, we can examine the memory and understand the state of the variables. Setting a breakpoint at the `execute_vm` function allows us to inspect the memory when it's initialized.

2. **Extracting the Encoded Flag:** 
```bash 
0x404080 <memory>:      0x1760156e087c1f70      0x1f7827147c4b1464
0x404090 <memory+16>:   0x45712e1b2a75462b      0x0000006914231323
```   

   From the memory at address `0x404080`, we extract the following sequence and convert from little endian to big endian, which represents the encoded flag:
   ```
   701f7c086e156017 64144b7c1427781f 2b46752a1b2e7145 2313231469
   ```

1. **Understanding the XOR Process:**  
   The encoding process involves XORing each byte with the previous one. Since the first byte is XORed with `0x00`, it essentially gets skipped when decoded. We need to reverse this by XORing the entire encoded flag with itself, but removing the last byte (`0x69`) and appending `0x00` at the beginning.

2. **Reversing the XOR:**  
   To decode the flag:
   - Perform XOR between the encoded flag and the same flag, but with the last byte (`0x69`) removed and a `0x00` byte added at the start.
   - This will yield the original flag.

#### **Decoded Flag**

After performing the XOR operation as described above, we obtain the decoded flag:

```
poctf{uwsp_7h3_g4m3_15_4f007}
```

---

### **Flag**

`poctf{uwsp_7h3_g4m3_15_4f007}`  

---
