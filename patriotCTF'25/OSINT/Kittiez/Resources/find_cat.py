import os
import hashlib
from pathlib import Path

def calculate_md5(file_path):
    """Calculate MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def main():
    # Target hash to compare against
    target_hash = "9c5ca692da8d6e489beecd5b448ddb35"
    
    # Path to Cats folder
    cats_folder = Path("Cats.00003")
    
    # Check if Cats folder exists
    if not cats_folder.exists():
        print(f"Error: '{cats_folder}' folder not found!")
        return
    
    if not cats_folder.is_dir():
        print(f"Error: '{cats_folder}' is not a directory!")
        return
    
    # Find all files in Cats folder
    files = []
    for file_path in cats_folder.rglob("*"):
        if file_path.is_file():
            files.append(file_path)
    
    if not files:
        print(f"No files found in '{cats_folder}' folder.")
        return
    
    print(f"Found {len(files)} file(s). Checking hashes...\n")
    
    # Check each file's hash
    found_matches = []
    for file_path in files:
        try:
            file_hash = calculate_md5(file_path)
            # print(f"hash: {file_hash}")
            if file_hash == target_hash:
                found_matches.append(file_path)
                print(f"found {file_path.name}")
        except Exception as e:
            print(f"Error processing {file_path.name}: {e}")
    
    if not found_matches:
        print(f"\nNo files found with hash: {target_hash}")

if __name__ == "__main__":
    main()

