from pwn import *
context.log_level='debug'

p = process(['./environ'],env={'LD_PRELOAD':'./libc.so.6'})

p.interactive()
