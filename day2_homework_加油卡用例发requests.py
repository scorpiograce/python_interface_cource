import requests
import json

#特殊用例-业务ID无效
"""
url="http://115.28.108.130:8080/gasStation/process"
data={"dataSourceId":"c2hhbmRvbmc=","methodId":"05A","CardInfo":{"cardNumber":"xlyxlyxly"}}
print(data)
res=requests.post(url=url,json=data)
print(res.text)
print(res.json())
code=res.json()["code"]
assert code == 199
msg=res.json()["msg"]
assert msg == "业务ID无效"
success=res.json()["success"]
assert success == False
#assert success == True
"""

#添加卡失败-卡已经添加过
"""
url="http://115.28.108.130:8080/gasStation/process"
data={
 "dataSourceId":"c2hhbmRvbmc=",
 "methodId":"00A",
 "CardInfo":{"cardNumber":"xlyxlyxly"}
}
res=requests.post(url=url,json=data)
print(res.text)
print(res.json())
code=res.json()["code"]
assert code == 5000
msg=res.json()["msg"]
assert msg == "该卡已添加"
success=res.json()["success"]
assert success == False
"""
