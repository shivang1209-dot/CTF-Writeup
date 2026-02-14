#!/usr/bin/env python3
"""
Extract the embedded Excalidraw scene from the PNG and save as a .excalidraw file.
Open the output in https://excalidraw.com (drag & drop or File → Open).
"""
import json
import zlib
import sys
from pathlib import Path


def extract_excalidraw_from_png(png_path: Path) -> bytes:
    """Extract the Excalidraw JSON payload from PNG tEXt chunk."""
    data = png_path.read_bytes()
    i = 8
    while i < len(data):
        if i + 12 > len(data):
            break
        length = int.from_bytes(data[i : i + 4], "big")
        ctype = data[i + 4 : i + 8]
        if ctype == b"tEXt":
            payload = data[i + 8 : i + 8 + length]
            null = payload.find(b"\x00")
            text = payload[null + 1 :]
            break
        i += 8 + length + 4
    else:
        raise ValueError("No tEXt chunk found")

    marker = b'"encoded":"'
    start = text.find(marker) + len(marker)
    end = text.rfind(b'"}')
    if start < len(marker) or end == -1:
        raise ValueError("Could not find encoded payload bounds")
    encoded_slice = text[start:end]
    return _decode_json_string(encoded_slice)


def _decode_json_string(s: bytes) -> bytes:
    result = bytearray()
    i = 0
    escapes = [
        (b"\\\\", 92),
        (b'\\"', 34),
        (b"\\n", 10),
        (b"\\b", 8),
        (b"\\f", 12),
        (b"\\r", 13),
        (b"\\t", 9),
    ]
    while i < len(s):
        if i + 2 <= len(s) and s[i : i + 2] == b"\\u" and i + 6 <= len(s):
            try:
                code = int(s[i + 2 : i + 6].decode("ascii"), 16)
                result.append(code)
                i += 6
                continue
            except (ValueError, UnicodeDecodeError):
                pass
        for esc, byte in escapes:
            if i + len(esc) <= len(s) and s[i : i + len(esc)] == esc:
                result.append(byte)
                i += len(esc)
                break
        else:
            result.append(s[i])
            i += 1
    return bytes(result)


def main():
    png_path = Path(__file__).resolve().parent / "file.png"
    out_path = Path(__file__).resolve().parent / "scene.excalidraw"

    if not png_path.exists():
        print("file.png not found", file=sys.stderr)
        sys.exit(1)

    raw_encoded = extract_excalidraw_from_png(png_path)
    decompressed = zlib.decompress(raw_encoded)
    scene = json.loads(decompressed.decode("utf-8"))

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(scene, f, indent=2, ensure_ascii=False)

    print(f"Extracted scene saved to: {out_path}")
    print("Open it at https://excalidraw.com (drag & drop or File → Open).")


if __name__ == "__main__":
    main()
