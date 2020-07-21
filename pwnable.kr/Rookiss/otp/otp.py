from pwn import *
#context.log_level='debug'

s = ssh('otp','pwnable.kr',port=2222,password='guest')

argvs = [str(i) for i in range(2)]
argvs[1] = 'AAAA'

p = process(executable='./otp',argv=argvs)

p.interactive()
