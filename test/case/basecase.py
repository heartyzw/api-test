#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
import requests
import unittest
import sys
sys.path.append("../..")   # 统一将包的搜索路径提升到项目根目录下

from lib.read_execl import *
from lib.case_log import log_case_info

class BaseCase(unittest.TestCase): # 继承unittest.TestCase
    @classmethod
    def setUpClass(cls):
        if cls.__name__ != 'BaseCase':
            cls.data_list = excel_to_list(data_file, cls.__name__)


    def get_case_data(self, case_name):
        return get_test_data(self.data_list, case_name)

    def send_request(self, case_data):
        case_name = get_test_data('case_name')
        url= case_data.get('url')
        args = case_data.get('args')
        headers = case_data.get('headers')
        expect_res = case_data.get('expect_res')
        method = case_data.get('method')
        data_type = case_data.get('data_type')

        if method.upper() == 'GET':
            res = requests.get(url=url, params=json.loads(args))

        elif data_type.upper == 'FROM':
            res = requests.post(url=url, data=json.loads(args), headers=json.loads(headers))
            log_case_info(case_name, url, args, expect_res, res.text)
            self.assertEqual(res.text, expect_res)

        else:
            res = requests.post(url=url, json=json.loads(args), headers=json.loads(headers))  # JSON格式请求
            log_case_info(case_name, url, args, json.dumps(json.loads(expect_res), sort_keys=True),
                          json.dumps(res.json(), ensure_ascii=False, sort_keys=True))
            self.assertDictEqual(res.json(), json.loads(expect_res))

