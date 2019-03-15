import unittest
import requests
'''
用例编写
新建一个test_开头（必须）的.py文件，如test_user_login.py
导入unittest
编写一个Test开头（必须）的类，并继承unittest.TestCase，做为测试类
在类中编写一个test_开头（必须）的方法，作为用例
'''

"""
# test_user_login.py # 文件必须test_开头
class TestUserLogin(unittest.TestCase):  # 类必须Test开头，继承TestCase才能识别为用例类
    url = 'http://115.28.108.130:5000/api/user/login/'
    # url = 'http://192.168.23.230/phpmyadmin'
    def test_user_login_normal(self): # 一条测试用例，必须test_开头
        data = {"name": "张三", "password": "123456"}
        print(type(data))
        res = requests.post(url=self.url, data=data)
        print(res.text)
        self.assertIn('登录成功', res.text)  # 断言

    def test_user_login_password_wrong(self):
        data = {"name": "张三", "password": "1234567"}
        res = requests.post(url=self.url, data=data)
        self.assertIn('失败', res.text)  # 断言


if __name__ == '__main__':  # 如果是直接从当前模块执行（非别的模块调用本模块）
    unittest.main(verbosity=2)  # 运行本测试类所有用例, verbosity为结果显示级别
      
## 用例执行顺序：并非按书写顺序执行，而是按用例名ascii码先后顺序执行

"""

"""
用例断言
unittest提供了丰富的断言方法，常用为以下几种：

判断相等
assertEqual(a,b)/assertNotEqual(a,b): 断言值是否相等
assertIs(a,b)/assertIsNot(a,b): 断言是否同一对象（内存地址一样）
assertListEqual(list1, list2)/assertItemNotEqual(list1, list2): 断言列表是否相等
assertDictEqual(dict1, dict2)/assertDictNotEqual(dict1, dict2): 断言字典是否相等

是否为空
assertIsNone(a)/assertIsNotNone(a)

判断真假
assertTrue(a)/assertFalse(a)

是否包含
assertIn(a,b)/assertNotIn(a,b) # b中是否包含a


大小判断

assertGreater(a,b)/assertLess(a,b) : 断言a>b / 断言a<b
assertGreaterEqual(a,b)/assertLessEqual: 断言a>=b / 断言a<=b

类型判断
assertIsInstance(a,dict)/assertNotIsInstance(a,list) # 断言a为字典 / 断言a非列表

import unittest

case = unittest.TestCase()
case.assertEqual(1,2.0/2)  # 通过1=2.0/2
case.assertEqual(1, True)  # 通过
case.assertIs(1.0, 2.0/2)  # 失败，不是同一对象
case.assertListEqual([1,2],[1,2])  # 通过（顺序要一致）
case.assertDictEqual({"a":1,"b":2}, {"b":2,"a":1})  # 通过，字典本无序
case.assertIsNone({})  # 失败
case.assertFalse({}) # 通过，空字典为False
case.assertIn("h","hello") # 通过
case.assertGreater(3,2) # 通过，3>2
case.assertIsInstance({"a":1}, dict)  # 通过

## 断言是unittest.TestCase的一种方法，通过断言判断用例是否通过（Pass/Fail)
"""

"""
Test Fixtures(用例包裹方法)
Test Fixtures即setUp（用例准备）及tearDown（测试清理）方法，用于分别在测试前及测试后执行
按照不同的作用范围分为：

setUp()/tearDown(): 每个用例执行前/后执行一次
setUpClass()/tearDownClass(): 每个测试类加载时/结束时执行一次
setUpMoudle()/tearDownMoudle(): 每个测试模块（一个py文件为一个模块）加载/结束时执行一次

"""


'''
import unittest


def setUpModule(): # 当前模块执行前只执行一次
    print("=====setUpModule====")


def tearDownModule(): # 当前模块执行后只执行一次
    print("====tearDownMoudle ====")


class TestClass1(unittest.TestCase):
    @classmethod   # 声明为类方法（必须
    def setUpClass(cls):  # 类方法，注意后面是cls，整个类只执行一次
        print('---- setUpClass-----')

    @classmethod
    def tearDownClass(cls):
        print('---- tearDownClass-----')

    def setUp(self):   # 该类中每个测试用例执行一次
        print('...... setUp ....... ')

    def tearDown(self):
        print('..... tearDown ...')

    def test_a(self):  # 大写B的ascii比小写a靠前，会比test_a先执行
        print("a")

    def test_B(self):  # 大写B的ascii比小写a靠前，会比test_a先执行
        print('B')


class TestClass2(unittest.TestCase): # 该模块的另一个测试类
    def test_A(self):
        print('A')


if __name__ == '__main__':
    unittest.main()


'''


import unittest
import requests
# 获取连接方法
import pymysql


# 获取连接方法
def get_db_conn():
    conn = pymysql.connect(host='115.28.108.130',
                           port=3306,
                           user='test',
                           passwd='123456',
                           db='api_test',
                           charset='utf8')  # 如果查询有中文，需要指定测试集编码

    return conn


# 封装数据库查询操作
def query_db(sql):
    conn = get_db_conn()  # 获取连接
    cur = conn.cursor()  # 建立游标
    cur.execute(sql)  # 执行sql
    result = cur.fetchall()  # 获取所有查询结果
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接
    return result  # 返回结果


# 封装更改数据库操作
def change_db(sql):
    conn = get_db_conn()  # 获取连接
    cur = conn.cursor()  # 建立游标
    try:
        cur.execute(sql)  # 执行sql
        conn.commit()  # 提交更改
    except Exception as e:
        conn.rollback()  # 回滚
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接


# 封装常用数据库操作
def check_user(name):
    # 注意sql中''号嵌套的问题
    sql = "select * from user where name = '{}'".format(name)
    result = query_db(sql)
    return True if result else False


def add_user(name, password):
    sql = "insert into user (name, passwd) values ('{}','{}')".format(name, password)
    change_db(sql)


def del_user(name):
    sql = "delete from user where name='{}'".format(name)
    change_db(sql)





# 数据准备
NOT_EXIST_USER = '范冰冰'
EXIST_USER = '张三'


class TestUserReq(unittest.TestCase):
    url = 'http://115.28.108.130:5000/api/user/reg/'

    def test_user_reg_normal(self):
        # 环境检查
        if check_user(NOT_EXIST_USER):
            del_user(NOT_EXIST_USER)

        # 发送请求
        data = {'name': NOT_EXIST_USER, 'password': '123456'}
        res = requests.post(url=self.url, json=data)

        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        except_res = {
            "code": "100000",
            "msg": "成功",
            "data": {
                "name": NOT_EXIST_USER,
                "password": "e10adc3949ba59abbe56e057f20f883e"
            }
        }

        # 响应断言（整体断言）
        self.assertDictEqual(res.json(), except_res)

        # 数据库断言
        self.assertTrue(check_user(NOT_EXIST_USER))

        # 环境清理（由于注册接口向数据库写入了用户信息）
        del_user(NOT_EXIST_USER)

    def test_user_reg_exist(self):
        # 环境检查
        if not check_user(EXIST_USER):
            add_user(EXIST_USER)

        # 发送请求
        data = {'name': EXIST_USER, 'password': '123456'}
        res = requests.post(url=self.url, json=data)
        print(res.text)

        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        except_res = {
            "code": "100001",
            "msg": "失败，用户已存在",
            "data": {
                "name": EXIST_USER,
                "password": "e10adc3949ba59abbe56e057f20f883e"
            }
        }

        # 响应断言（整体断言）
        self.assertDictEqual(res.json(), except_res)

        # 数据库断言(没有注册成功，数据库没有添加新用户)

        # 环境清理（无需清理）


if __name__ == '__main__':
    unittest.main(verbosity=2)  # 运行所有用例


# unittest.main() 用来加载整个测试用了。同时我们可以是用TestSuite 来灵活的组织要运行的测试集