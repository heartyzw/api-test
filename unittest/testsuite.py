import unittest
'''
1 # 使用TestSuite来灵活的组织测试用例
from test_user_login import TestUserLogin
from test_user_reg import TestUserReg  # 从上面两个例子里导入测试类


suite = unittest.TestSuite()
suite.addTest(TestUserLogin('test_user_login_normal'))
suite.addTests([TestUserReg('test_user_reg_normal'), TestUserReg('test_user_reg_exist')])
# 运行测试集
unittest.TextTestRunner(verbosity=2).run(suite)  # verbosity显示级别，运行顺序为添加到suite中的顺序
'''
'''
#2 使用makeSuite来制作用例集2
from test_user_login import TestUserLogin

suite1 = unittest.makeSuite(TestUserLogin, 'test_user_login_normal') # 使用测试类的单条用例制作测试集
suite2 = unittest.makeSuite(TestUserLogin) # 使用整个测试类制作测试集合(包含该测试类所有用例)

unittest.TextTestRunner(verbosity=2).run(suite1)

'''
'''
3 # 使用TestLoader（用例加载器）生成测试集
from test_user_login import TestUserLogin

suite = unittest.TestLoader().loadTestsFromTestCase(TestUserLogin)
unittest.TextTestRunner(verbosity=2).run(suite)
'''
# 4.使用discover（用例发现）遍历所有的用例


suite = unittest.defaultTestLoader.discover("./")  # 遍历当前目录及子包中所有test_*.py中所有unittest用例
unittest.TextTestRunner(verbosity=2).run(suite)