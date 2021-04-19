from pwn import *
context.log_level = 'debug'

hosts = 'host1.dreamhack.games'
port = 22370

p = remote(hosts,port)

p.interactive()
