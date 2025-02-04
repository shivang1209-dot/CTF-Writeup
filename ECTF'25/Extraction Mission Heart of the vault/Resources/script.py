import subprocess
import os

def crack_zip_password(zip_file):
    # Step 1: Use zip2john to get the hash of the zip file
    zip2john_cmd = f"zip2john {zip_file} > zip_hash.txt"
    subprocess.run(zip2john_cmd, shell=True, check=True)

    # Step 2: Run john with the wordlist to crack the password
    john_cmd = f"john --wordlist=/usr/share/wordlists/rockyou.txt zip_hash.txt"
    subprocess.run(john_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

    # Step 3: Get the cracked password from john
    john_show_cmd = "john --show zip_hash.txt"
    result = subprocess.run(john_show_cmd, shell=True, capture_output=True, text=True)
    
    # Extract the password using the specified grep and cut
    output = result.stdout.strip()
    password = ""
    if output:
        # Apply the grep and cut to extract the password
        password_cmd = f"echo '{output}' | grep -oP ':(\\S+):' | cut -d: -f2"
        password_result = subprocess.run(password_cmd, shell=True, capture_output=True, text=True)
        
        # Get the password
        password = password_result.stdout.strip()
        print(f"Password: {password}")

        # Step 4: Extract the zip file using 7z with the cracked password
        extract_cmd = f"7z x {zip_file} -p{password}"
        extract_result = subprocess.run(extract_cmd, shell=True, capture_output=True, text=True)
        
        # Print out the files being unzipped
        if extract_result.returncode == 0:
            for line in extract_result.stdout.splitlines():
                if "Extracting" in line:
                    print(f"Unzipped file: {line.strip()}")
        else:
            print("Extraction failed!")

    # Clean up
    os.remove("zip_hash.txt")
    return password


def extract_misc_zip():
    zip_file = "Misc_5_-_dwarf_vault_200.zip"
    print(f"\nProcessing {zip_file}...")
    password = crack_zip_password(zip_file)
    return password


def batch_extract():
    # List to store cracked passwords
    passwords = []
    
    # Step 1: Extract Misc_5_-_dwarf_vault_200.zip first
    misc_password = extract_misc_zip()
    passwords.append(f'"{misc_password}"')

    # Step 2: Loop from 199 down to 2 for dwarf_vault_x.zip files
    for i in range(199, 0, -1):
        zip_file = f"dwarf_vault_{i}.zip"
        if os.path.exists(zip_file):
            print(f"\nProcessing {zip_file}...")
            password = crack_zip_password(zip_file)
            passwords.append(f'"{password}"')
        else:
            print(f"File {zip_file} does not exist!")

    # Step 3: Write passwords to a file
    with open("cracked_passwords.txt", "w") as f:
        f.write(",".join(passwords))

    # Step 4: Cleanup - Remove all .zip files in the current folder
    for file in os.listdir():
        if file.endswith(".zip"):
            os.remove(file)
            print(f"Removed {file}")

# Start the batch extraction
batch_extract()
