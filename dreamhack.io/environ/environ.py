from pwn import *
context.log_level='debug'

n = remote('host1.dreamhack.games',8367)
elf = ELF('./environ')
libc = ELF('./libc.so.6')

n.recvuntil('stdout: ')
stdout = n.recvuntil('\n')[:-1]

log.info('stdout : '+stdout)


n.interactive()
