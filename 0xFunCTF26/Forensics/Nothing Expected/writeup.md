# Challenge Name: Nothing Expected

## Description

Here's a small drawing I put together. There isn't really anything in it, as you can tell.

---

## Writeup

### Step 1: Inspecting the PNG

We are given [Resources/file.png](Resources/file.png). Check type and metadata:

```bash
file Resources/file.png
exiftool Resources/file.png
```

ExifTool shows a **tEXt** (or similar) chunk with key **applicationvndexcalidrawjson** and a long value. So the PNG embeds **Excalidraw** scene data (JSON with `encoding: "bstring"`, `compressed: true`, and an `encoded` field containing binary/zlib data).

### Step 2: Extracting the Excalidraw Scene

The embedded data is **zlib-compressed** and possibly stored with JSON escapes. Use the provided **[Resources/extract_excalidraw.py](Resources/extract_excalidraw.py)** (or equivalent) to:

- Parse the PNG chunks and read the Excalidraw JSON.
- Decompress and decode the `encoded` field.
- Write a valid **.excalidraw** file (e.g. **scene.excalidraw**).

### Step 3: Opening in Excalidraw

Open [Resources/scene.excalidraw](Resources/scene.excalidraw) in [Excalidraw](https://excalidraw.com/) (web or desktop). The canvas contains text or shapes that spell the flag.

### Step 4: Reading the Flag

The flag is visible in the drawing (e.g. text elements or labels).

---

## Resources

- **[Resources/file.png](Resources/file.png)** — Challenge PNG with embedded Excalidraw JSON.
- **[Resources/extract_excalidraw.py](Resources/extract_excalidraw.py)** — Script to extract and build the .excalidraw file.
- **[Resources/scene.excalidraw](Resources/scene.excalidraw)** — Output file to open in Excalidraw.

---

## Flag

```
0xfun{th3_sw0rd_0f_k1ng_4rthur}
```

---
