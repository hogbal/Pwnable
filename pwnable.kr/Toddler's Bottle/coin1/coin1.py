from pwn import *
import re
 
def check (start, end, weight) :
    num = (end - start)
    print ("[!] check : num is %d" % num)
    if (10 * num == weight) :
        return 1
    else :
        return 0
 
def main () :
    r = remote("pwnable.kr", 9007)
    data = r.recvuntil("sec... -\n")
    print data
    sleep(3)
    r.recv(1024)
    # start game!
    for i in range (0, 100) :
        print ("[+] recving data..."),
        sleep(0.1)
        #    r.recv(1024)
        data = r.recv(1024)
        print (": Done, data is %s" % data),
        print ("[*] data parsing..."),
        arr = re.findall("\d+", data)
        N = int(arr[0])
        C = int(arr[1])
        print (": Done, N is %d, C is %d" % (N, C))
        # data has been parsed
 
        start = 0
        end = N
        while (start <= end) :
            msg = ""
            mid = (start + end) / 2
            print ("[+] sending msg start...")
            for j in range (start, mid + 1) :
                msg += str(j) + " "
            msg += '\n'
            r.send(msg)
            print ("[*] msg : %s" % msg),
            dt = r.recv(100)
            print ("[*] dt : %s" % dt),
            if (dt.find("Correct") != -1) :
                break
            #    sleep(3)
            weight = int(dt)
            print ("[+] weight : %d" % weight)
            #    sleep(3)
            ck = check(start, mid+1, weight)
            if (ck == 1) :
                print ("[*] counterfeit coin not found")
                start = mid + 1
            elif (ck == 0) :
                print ("[*] counterfeit coin found")
                end = mid
        print ("[+] Done, counterfeit coin has been found")
    while True :
           data = r.recvline ()
        print data
        if (data.find("bye!") != -1) :
            break
 
if __name__ == "__main__" :
    main ()
 

