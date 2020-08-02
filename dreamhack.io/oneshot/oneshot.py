from pwn import *
context.log_level='debug'

n = remote('host1.dreamhack.games',8395)
libc = ELF('./libc.so.6')

n.interactive()
