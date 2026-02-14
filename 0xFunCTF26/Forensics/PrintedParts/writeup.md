# Challenge Name: PrintedParts

## Description

A friend of mine 3D printed something interesting.

---

## Writeup

### Step 1: Recognizing the File

The challenge provides a **G-code** file: [Resources/3D.gcode](Resources/3D.gcode). The toolpath and layers can form text or shapes when viewed from the right angle.

### Step 2: Visualizing the G-code

Load the G-code in a slicer or viewer that supports **preview mode**, e.g. [PrusaSlicer](https://prusaslicer.net/#download). Use preview (not necessarily slice) to see the path and layers.

### Step 3: Reading the Flag

In the preview, part of the flag may be visible as text (e.g. `0xfun{this`). Some segments can be inside or along a figure. Move the view (e.g. cursor/camera to the right or rotate) to see more. The toolpath lines spell out something like **this_monkey_has_a_flag**.

### Step 4: Assembling the Flag

Combine the visible parts into the full flag: `0xfun{this_monkey_has_a_flag}`.

---

## Resources

- **[Resources/3D.gcode](Resources/3D.gcode)** — Challenge G-code file.

---

## Flag

```
0xfun{this_monkey_has_a_flag}
```

---
