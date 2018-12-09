import unittest
import requests

# 声明一个测试类 基础 unittest.TestCase
class TestLogin(unittest.TestCase):
    def test_login_normal(self):
        url="http://115.28.108.130:5000/api/user/login/"
        data={"name":"张三","password":"123456"}
        res=requests.post(url=url,data=data)
        self.assertEqual(res.text,'<h1>登录成功</h1>',"返回结果不合预期")  #第三个参数可选，是如果断言失败，即不相等时，输出的错误提示语
    def test_login_password_wrong(self):
        url="http://115.28.108.130:5000/api/user/login/"
        data={"name":"张三","password":"11111"}
        res=requests.post(url=url,data=data)
        self.assertIn("<h1>失败，用户名或密码错误</h1>",res.text,"登陆失败")

#TestLogin()
#case1=TestLogin()
#case1.test_login_normal()

# 如果用其他的编译器，就要用下述这段执行上面的用例
if __name__ == "__main__":
    unittest.main(verbosity=2)  # 可以指定显示级别
