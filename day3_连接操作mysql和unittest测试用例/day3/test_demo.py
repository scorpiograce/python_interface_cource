import  unittest

def setUpModule():
    print("***setUpModule***")
def tearDownModule():
    print("***teatDownModule***")

class TestA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("===setUpClass===")
    @classmethod
    def tearDownClass(cls):
        print("===tearDownClass===")

    def setUp(self):
        print("---setUp---")
    def tearDown(self):
        print("---tearDown---")

    def test_a(self):
        print("a")
    def test_b(self):
        print("b")

# 如果用其他的编译器，就要用下述这段执行上面的用例
if __name__ == "__main__":
    unittest.main(verbosity=2)  # 可以指定显示级别