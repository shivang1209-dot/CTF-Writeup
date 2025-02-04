## **Challenge Name**: Definitely not in the PDF

---

### Description

The challenge description hinted that the flag was "not among those ones" in the provided PDF, implying that the flag may be hidden elsewhere, possibly within the file itself or through steganography techniques.

We are provided with a ZIP file named `[Stega_-_Definitely_not_in_the_PDF.zip](Resources/Stega_-_Definitely_not_in_the_PDF.zip)` that contains a PDF file called `world_flags.pdf`. The flag format is `ECTF{...}`.

### Files Provided:

- [Stega_-_Definitely_not_in_the_PDF.zip](Resources/Stega_-_Definitely_not_in_the_PDF.zip)

---

### Solution

1. **Unzip the File**:
   We begin by unzipping the provided `Stega_-_Definitely_not_in_the_PDF.zip` archive.

   ```bash
   unzip Stega_-_Definitely_not_in_the_PDF.zip
   ```

   This will extract the `world_flags.pdf` file.

2. **Examine the Content**:
   After extracting the ZIP, we are left with a PDF file (`world_flags.pdf`). The name itself suggests that it may contain some sort of hidden information, but the flag is *not* directly visible in the PDF. At this point, we can try some common steganography techniques like checking the file metadata, hidden messages, or examining the file with tools that can reveal hidden content.

3. **Steganography Check**:
   We can try to run some steganography tools or inspect the PDF using `pdf-parser` or `strings` to see if there is anything unusual in the document that could point us towards the flag. However, in this case, there are no immediate clues found through these techniques, and the challenge directly leads us to the next step.

4. **Check the Extracted Flag**:
   Interestingly, after unzipping the archive, the terminal itself shows the flag:

   ```plaintext
   ECTF{W3lL_d0nE_652651663616263}
   ```

   This is the correct flag, and it was revealed in the output from the unzipping process itself.

---

### Flag

`ECTF{W3lL_d0nE_652651663616263}`

---
