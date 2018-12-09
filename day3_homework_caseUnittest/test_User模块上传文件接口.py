import requests
import unittest

class TestUploadFile(unittest.TestCase):
    def test_upload_succeed(self):
        url="http://115.28.108.130:5000/api/user/uploadImage/"
        f = open(r"D:\python_project\python_interfaceTest\day3_homework_caseUnittest\1.txt", encoding='utf-8')
        files = {"file": f}
        res = requests.post(url=url, files=files)
        self.assertEqual(res.text,'<h1>上传成功</h1>',"上传失败")  #第三个参数可选，是如果断言失败，即不相等时，输出的错误提示语

# 如果用其他的编译器，就要用下述这段执行上面的用例
if __name__ == "__main__":
    unittest.main(verbosity=2)  # 可以指定显示级别