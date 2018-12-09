import requests
import unittest

class TestJiayouka(unittest.TestCase):
    def test_businessIdWrong(self):
        url="http://115.28.108.130:8080/gasStation/process"
        data={"dataSourceId":"c2hhbmRvbmc=","methodId":"05A","CardInfo":{"cardNumber":"xlyxlyxly"}}
        res=requests.post(url=url,json=data)
        print(res.text)
        print(res.json())
        code=res.json()["code"]
        self.assertEqual(code, 199, "返回码不合预期")
        msg=res.json()["msg"]
        #self.assertEqual(msg,'业务ID无效',"返回消息有误")
        self.assertIn("无效", msg, "返回消息有误")
        success=res.json()["success"]
        #self.assertEqual(success,False,"返回成功状态有误")
        #self.assertTrue(success, True)
        self.assertFalse(success,False)

    def test_addCardFailed(self):
        url = "http://115.28.108.130:8080/gasStation/process"
        data = {
            "dataSourceId": "c2hhbmRvbmc=",
            "methodId": "00A",
            "CardInfo": {"cardNumber": "xlyxlyxly"}
        }
        res = requests.post(url=url, json=data)
        print(res.text)
        print(res.json())
        code = res.json()["code"]
        self.assertEqual(code, 5000, "返回码不合预期")
        msg = res.json()["msg"]
        #self.assertEqual(msg, '该卡已添加', "返回消息有误")
        self.assertIn("已添加",msg,"返回消息有误")
        success = res.json()["success"]
        #self.assertEqual(success, False, "返回成功状态有误")
        # self.assertTrue(success, True)
        self.assertFalse(success, False)
    """
    def test_addCardSucceed(self):
        url = "http://115.28.108.130:8080/gasStation/process"
        data = {
             "dataSourceId":"c2hhbmRvbmc=",
             "methodId":"00A",
             "CardInfo":{"cardNumber":"xlyxlyxly03"}
         }
        res = requests.post(url=url, json=data)
        print(res.text)
        print(res.json())
        code = res.json()["code"]
        self.assertEqual(code, 200, "返回码不合预期")
        msg = res.json()["msg"]
        self.assertEqual(msg, '添加卡成功', "返回消息有误")
        success = res.json()["success"]
        self.assertEqual(success, True, "返回成功状态有误")
    """
# 如果用其他的编译器，就要用下述这段执行上面的用例
if __name__ == "__main__":
    unittest.main(verbosity=2)  # 可以指定显示级别