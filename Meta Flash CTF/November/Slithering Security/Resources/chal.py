
SECRET_FLAG=b"\x54\x57\x56\x30\x59\x55\x4e\x55\x52\x6e\x74\x6b\x4d\x47\x34\x33\x58\x7a\x64\x79\x64\x58\x4d\x33\x58\x32\x4e\x73\x4d\x57\x34\x33\x63\x31\x39\x33\x61\x54\x64\x6f\x58\x33\x4d\x7a\x59\x33\x49\x7a\x4e\x33\x4e\x7a\x63\x33\x4e\x7a\x63\x33\x4e\x39"
HASHED_PASSWORD = b'\x12\x1eW\x98\x00\xc1C\xff\xe3\xa9\x15\xde\xd9\x00\x9b\xc9'

from base64 import b64decode
from hashlib import md5

def check_password(password):
    m = md5()
    m.update(password)
    return m.digest() == HASHED_PASSWORD

def main():
    while True:
        inp = input("Please enter your passssssword: ").encode()
        if check_password(inp):
            print(f"Well done, your flag isssssss {b64decode(SECRET_FLAG).decode()}")
            exit()
        else:
            print("Passsssssword incorrect, please try again.")

if __name__ == "__main__":
    main()