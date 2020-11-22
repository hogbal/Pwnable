from pwn import *
context.log_level='debug'

n = remote('host3.dreamhack.games',7182)

n.interactive()
