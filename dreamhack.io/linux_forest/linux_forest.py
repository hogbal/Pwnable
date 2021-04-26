from pwn import *
#context.log_level = 'debug'

hosts = 'host1.dreamhack.games'
port = 16711

p = remote(hosts,port)

p.interactive()
