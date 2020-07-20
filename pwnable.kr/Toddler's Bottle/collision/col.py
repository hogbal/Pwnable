from pwn import *
#context.log_level='debug'

payload = p32(0x6c5cec8) * 4 + p32(0x6c5cecc)

s = ssh('col' ,'pwnable.kr' ,password='guest', port=2222)
p = s.process(executable='./col', argv=['col',payload])
flag = p.recv()
log.success("Flag: " + str(flag))
