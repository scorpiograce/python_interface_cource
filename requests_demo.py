import requests
import json
"""
#06-获取token接口-发送get请求，并得到 响应对象
#url参数可以直接放到url字符里，也可以单独构造一个字典
params={
    "appid":"136425"
}
url="http://115.28.108.130:5000/api/user/getToken/?appid="+params['appid']
res = requests.get(url=url)
#res = requests.get(url="http://115.28.108.130:5000/api/user/getToken/?appid="+params['appid'],params=params)
#res = requests.get("http://115.28.108.130:5000/api/user/getToken/?appid=136425")  #不写就默认赋给url
#响应对象的文本数据
print(res.text) #打印响应文本
"""

#02-登录接口-post请求
"""
#不写header会自动给加上header
url="http://115.28.108.130:5000/api/user/login/"
data={"name":"张三","password":"123456"}
res=requests.post(url=url,data=data)
print(res.text)
"""
"""
#传header,反爬的或者需要cookie的，需要传headers
url="https://www.jianshu.com/p/c6380e393a04"
headers = {
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": 1,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cookie": "__yadk_uid=MS4CqGXvPK1KsaulkIHqGz4Znd5eATQ2; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221649eb9a31e8fd-0d8c5e493f787c-5393662-1327104-1649eb9a31f3b1%22%2C%22%24device_id%22%3A%221649eb9a31e8fd-0d8c5e493f787c-5393662-1327104-1649eb9a31f3b1%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1540005373,1540608350,1542509211,1542509349; _m7e_session=298a00260332f352a4b2adc52e8b02b3"
}
res=requests.post(url=url,headers=headers)
print(res.text)
"""
"""
#把返回数据（字符串）转成字典方法一：
url="http://115.28.108.130:5000/api/user/reg/"
data={
    "name":"李六",
    "password":"123456"
}
res=requests.post(url=url,json=data)
print(res.text)
data_dict=json.loads(res.text)
print(data)
print(type(data))
print(data["name"])
"""
"""
#把返回数据（字符串）转成字典方法二：
url="http://115.28.108.130:5000/api/user/reg/"
data={
    "name":"李九",
    "password":"123456"
}
res=requests.post(url=url,json=data)
print(res.text)
a=res.json()  #直接转成了json对象
print(a)
print(type(a))
print(a["data"]["name"])
"""
"""
url="http://115.28.108.130:5000/api/user/reg/"
data={
    "name":"李九",
    "password":"123456"
}
res=requests.post(url=url,json=data)
code=res.json()["code"]
assert code == "100001"
"""
"""
l=[
  {"name":"薛1","password":"123456"},
  {"name":"薛2","password":"123456"},
  {"name":"薛3","password":"123456"},
  {"name":"薛4","password":"123456"},
  {"name":"薛5","password":"123456"}
]
url="http://115.28.108.130:5000/api/user/reg/"
for data in l:
    res=requests.post(url=url,json=data)
    msg=res.json()["msg"]
    print(msg)
"""
"""
#5、#每次连接是生成新的独立的会话
r1=requests.post(url="http://115.28.108.130:5000/api/user/login/",data={"name":"薛1","password":"123456"})
print(r1.text)

r2=requests.get("http://115.28.108.130:5000/api/user/getUserList/")  #每次连接是生成新的独立的会话
print(r2.text)
"""

#5、session保持
session=requests.session()
r1=session.post(url="http://115.28.108.130:5000/api/user/login/",data={"name":"薛1","password":"123456"})
print(r1.text)

r2=session.get("http://115.28.108.130:5000/api/user/getUserList/")  #每次连接是生成新的独立的会话
print(r2.text)