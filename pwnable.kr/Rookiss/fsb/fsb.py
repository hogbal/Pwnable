from pwn import *
context.log_level='debug'

s = ssh('fsb','pwnable',port=2222,password='guest')
n = s.process('./fsb')

n.interactive()
