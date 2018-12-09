import unittest
import requests
from day3.db import check_user,del_user

# 声明一个测试类 基础 unittest.TestCase
class TestLogin(unittest.TestCase):
    def test_reg_normal(self):
        url="http://115.28.108.130:5000/api/user/reg/"
        data={"name":"薛凌3","password":"123456"}
        res=requests.post(url=url,json=data)
        res_dict=res.json()  #json形式的返回结果
        self.assertIn("成功",res_dict["msg"])
        self.assertEqual(check_user("薛凌3"),True)
        #清洗数据
        del_user("薛凌3")

    def test_reg_password_wrong(self):
        url="http://115.28.108.130:5000/api/user/reg/"
        data={"name":"薛凌1","password":"123456"}
        res=requests.post(url=url,json=data)
        res_dict=res.json()
        self.assertIn("用户已存在",res_dict["msg"])
        self.assertEqual('100001',res_dict["code"])

# 如果用其他的编译器，就要用下述这段执行上面的用例
if __name__ == "__main__":
    unittest.main(verbosity=2)  # 可以指定显示级别

