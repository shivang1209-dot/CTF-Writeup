# Challenge Name: The Professors Files

## Description

A professor uploaded their ethics report for review, but something about it seems… off. The document's formatting feels inconsistent, almost like it was edited by hand rather than exported normally. The metadata looks strange too, and there's a rumor that the professor hides sensitive data in plain sight.

**Files:**
- `OSU_Ethics_Report.docx` - The document to analyze

---

## Writeup

### Step 1: Understanding DOCX Format

A DOCX file is essentially a ZIP archive containing XML files and other resources. We can extract it like any ZIP file.

### Step 2: Extracting the DOCX Contents

Extract the DOCX file using any ZIP extraction tool:

```bash
7z x OSU_Ethics_Report.docx
# or
unzip OSU_Ethics_Report.docx
```

This reveals the internal structure:
```
OSU_Ethics_Report.docx/
├── [Content_Types].xml
├── _rels/
├── docProps/
│   ├── app.xml
│   ├── core.xml
│   └── custom.xml
└── word/
    ├── _rels/
    ├── document.xml
    ├── document.xml.rels
    ├── fontTable.xml
    ├── settings.xml
    ├── styles.xml
    └── theme/
        └── theme1.xml
```

### Step 3: Searching for the Flag

Since the description mentions the professor hides data "in plain sight" and the metadata looks strange, we should check:
- XML comments
- Hidden text in XML files
- Metadata files
- Theme files

### Step 4: Finding the Flag

The flag is hidden in a comment within the `theme1.xml` file. Open the file and look for comments:

```xml
<!-- bctf{docx_is_zip} -->
```

---

## Flag

```
bctf{docx_is_zip}
```

---

