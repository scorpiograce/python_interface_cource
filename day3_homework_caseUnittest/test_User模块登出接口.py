import requests
import unittest

class TestLogout(unittest.TestCase):
    def test_login_normal(self):
        url="http://115.28.108.130:5000/api/user/login/"
        data={"name":"薛凌","password":"123456"}
        res=requests.post(url=url,data=data)
        self.assertEqual(res.text,'<h1>登录成功</h1>',"登录失败")  #第三个参数可选，是如果断言失败，即不相等时，输出的错误提示语
    def test_logout_normal(self):
        url="http://115.28.108.130:5000/api/user/logout/"
        res=requests.get(url)
        self.assertIn("<h1>退出登录成功</h1>", res.text, "登出失败")

# 如果用其他的编译器，就要用下述这段执行上面的用例
if __name__ == "__main__":
    unittest.main(verbosity=2)  # 可以指定显示级别