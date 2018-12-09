import unittest

# 1 发现并收集用例得到一个测试集合
suite=unittest.defaultTestLoader.discover(".")  #discover是寻找并搜集用例，得到一个测试集合，.代表在当前路径下搜索
# 2 使用文本测试运行器 运行这个测试集合
unittest.TextTestRunner(verbosity=2).run(suite)
