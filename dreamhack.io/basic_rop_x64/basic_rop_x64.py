from pwn import *
context.log_level='debug'

n = remote('host1.dreamhack.games',8392)
elf = ELF('./basic_rop_x64')
libc = ELF('./libc.so.6')

payload = b'A'*0x48

n.interactive()
