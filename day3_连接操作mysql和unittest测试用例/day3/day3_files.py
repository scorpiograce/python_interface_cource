import requests
import json
"""
url="https://api.github.com/user"
res=requests.get(url=url,auth=('superhin001','hanzhichao520'))
print(res.text)
"""

url = 'http://115.28.108.130:5000/api/user/uploadImage/'
f=open(r"D:\python_project\python_interfaceTest\day3\1.txt",encoding='utf-8')
files={"file":f}
r=requests.post(url=url,files=files)
print(r.text)