### Ariekei

#### keyword 

docker, gobuster -f 

#### Information

```html
PORT     STATE SERVICE   VERSION
22/tcp   open  ssh       OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 a7:5b:ae:65:93:ce:fb:dd:f9:6a:7f:de:50:67:f6:ec (RSA)
|   256 64:2c:a6:5e:96:ca:fb:10:05:82:36:ba:f0:c9:92:ef (ECDSA)
|_  256 51:9f:87:64:be:99:35:2a:80:a6:a2:25:eb:e0:95:9f (ED25519)
443/tcp  open  ssl/https nginx/1.10.2
_http-server-header: nginx/1.10.2
|_http-title: 400 The plain HTTP request was sent to HTTPS port
|_ssl-date: TLS randomness does not represent time
| tls-alpn:
|_  http/1.1
| tls-nextprotoneg:
|_  http/1.1
1022/tcp open  ssh       OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   1024 98:33:f6:b6:4c:18:f5:80:66:85:47:0c:f6:b7:90:7e (DSA)
|   2048 78:40:0d:1c:79:a1:45:d4:28:75:35:36:ed:42:4f:2d (RSA)
|   256 45:a6:71:96:df:62:b5:54:66:6b:91:7b:74:6a:db:b7 (ECDSA)
|_  256 ad:8d:4d:69:8e:7a:fd:d8:cd:6e:c1:4f:6f:81:b4:1f (ED25519)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

#### is Docker ???

OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.8 -> trusty-ubuntu

penSSH 7.2p2 Ubuntu 4ubuntu2.2    ->  xenial-ubuntu



### 443 port

the url https://10.10.10.65/  have some interersting in the ceritficate! 

```json
Certificate Subject Alt Name{

​	Not Critical
​	DNS Name: calvin.ariekei.htb
​	DNS Name: beehive.ariekei.htb

}
```

let us put into hosts [/etc/hosts]()

```dart
10.10.10.65 beehive.ariekei.htb calvin.ariekei.htb
```



### gobuster paramter "-f"  !!

gobuster make the /cgi-bin to /cgi-bin/  by append parameter "-f". if not , the website will make the bad code 404.

```python
 curl -k --ssl https://10.10.10.65/cgi-bin
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL /cgi-bin was not found on this server.</p>
<hr>
<address>Apache/2.2.22 (Debian) Server at 10.10.10.65 Port 80</address>
</body></html>
root@ens:~/htb/Ariekei# curl -k --ssl https://10.10.10.65/cgi-bin/
    <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>403 Forbidden</title>
</head><body>
<h1>Forbidden</h1>
<p>You don't have permission to access /cgi-bin/
on this server.</p>
<hr>
<address>Apache/2.2.22 (Debian) Server at 10.10.10.65 Port 80</address>
</body></html>

```

curl -k --ssl https://10.10.10.65/cgi-bin

not same with

curl -k --ssl https://10.10.10.65/cgi-bin/

```
 gobuster -k  -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u  https://beehive.ariekei.htb  -f

=====================================================

# Gobuster v2.0.1              OJ Reeves (@TheColonial)

[+] Mode         : dir
[+] Url/Domain   : https://beehive.ariekei.htb/
[+] Threads      : 10
[+] Wordl`
```

