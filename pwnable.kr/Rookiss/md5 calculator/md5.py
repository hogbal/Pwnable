from pwn import *
context.log_level = 'debug'

n = remote('pwnable.kr',9002)

n.recvuntil('Are you human? input captcha : ')
captcha = n.recvline()
n.sendline(captcha)

n.interactive()
