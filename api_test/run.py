import unittest
from conf import config
from lib.HTMLTestRunner_PY3 import HTMLTestRunner
from lib.send_email import send_email

# 遍历指定文件夹下及子包下的所有测试用例  test_
#all = unittest.defaultTestLoader.discover("testcase")
# 绝对路径法：
import os
config_path = os.path.abspath(__file__)  # __file__当前文件  os.path.abspath() 绝对路径
project_path = os.path.dirname(config_path)  # os.path.dirname() 所在文件夹即项目的路径
# testcase目录
data_file = os.path.join(project_path, 'testcase')
all = unittest.defaultTestLoader.discover(data_file)


if __name__ == "__main__":
    # unittest.TextTestRunner(verbosity=2).run(all)  # 两个不能同时使用
    config.logging.info("测试开始" + "=" * 50)
    with open(config.report_file, "wb") as f:  # 二进制写模式
        HTMLTestRunner(stream=f, title="User接口测试报告", description="测试报告").run(all)

    if config.is_send_email:
        send_email()
        config.logging.info("发送邮件成功")

    config.logging.info("测试结束" + "=" * 50)