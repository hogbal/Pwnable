from pwn import *
#context.log_level='debug'

s = ssh('random','pwnable.kr',port=2222,password='guest')
p = s.process('./random')

random_value = 0x6b8b4567
key = int(random_value ^ 0xdeadbeef)

print(key)
pause()

p.sendline(str(key))
p.interactive()
