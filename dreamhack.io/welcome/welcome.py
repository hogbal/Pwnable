from pwn import *
context.log_level='debug'

n = remote('host1.dreamhack.games',8367)

n.interactive()
