# 1.导入
from flask import Flask,request

# 2.用当前模块实例化一个Flask对象
app=Flask(__name__)

# 3.写个函数
@app.route("/app",method=[])
def add():
    a=request.values.get("a")
    b=request.values.get("b")
    sum
    return int(a)+int(b)

# 4.挂载接口路径，指定请求方法
# 5.运行