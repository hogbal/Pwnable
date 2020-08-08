from pwn import *
#context.log_level='debug'

s = ssh('fsb','pwnable.kr',port=2222,password='guest')
n = s.process('./fsb')
elf = ELF('./fsb')



n.interactive()
