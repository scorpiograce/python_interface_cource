import json

"""
#序列化：字典转字符串
data={
    "name":"zhangsan",
    "age":123
}
str_data=json.dumps(data)
print(str_data)
print(type(str_data))
"""

#反序列化：字符串转字典
res_text='''
{
  "code":"100001",
  "data":{
    "name":"张三四",
    "password":"123456"
  },
  "msg":"失败"
}
'''
res_dict=json.loads(res_text)
print(res_dict)
print(type(res_dict))
print(res_dict["data"]["name"])