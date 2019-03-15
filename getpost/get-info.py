#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
import json

postData  = {'a':'aaa','b':'bbb','c':'ccc','d':'ddd'}
print(type(postData))
data = json.dumps(postData)

print(type(data))
print(data)

common = 'http://192.168.23.181:8005/eq-service/v1'
url = common +'/api'
# params = {"key":"ec961279f453459b9248f0aeb6600bbe", "info":"你好"} # 字典格式，单独提出来，方便参数的添加修改等操作
res = requests.get(url=url)
resdict = res.json()
print(resdict['data'])
url_equipment = common + '/equipment'
res = requests.get(url=url_equipment)
resdict = res.json()
print(resdict['data'])

url_post = common + '/equipment'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = {
    "eq_mac": "FF:FF:FF:FF:FF:FA","eq_type": 1,"eq_details": 1, "eq_lng": 110,"eq_lat": 110,"park_id":  110,"building_id": 110,"unit_id": 110,"eq_floor": 112,"eq_name": 'test',"eq_remark": "yzwtest"
}

res = requests.post(url=url_post, data=data,  headers=headers)  # 请求正文是application/x-www-form-urlencoded



'''
url = "http://openapi.tuling123.com/openapi/api/v2"
data = {
    "reqType": 0,
    "perception": {
        "inputText": {
            "text": "附近的美食"
        },
        "inputImage": {
            "url": "imageUrl"
        },
        "selfInfo": {
            "location": {
                "city": "",
                "province": "北京",
                "street": "信息路"
            }
        }
    },
    "userInfo": {
        "apiKey": "ec961279f453459b9248f0aeb6600bbe",
        "userId": "206379"
    }
}
res = requests.post(url=url, json=data) # JSON格式的请求，将数据赋给json参数
print(res.text)


import json # 需要导入JSON包

data = {'name': '张三', 'password': '123456', "male": True, "money": None} # 字典格式
str_data = json.dumps(data)  # 序列化，转化为合法的JSON文本（方便HTTP传输）
print(str_data)


res = requests.post("http://www.tuling123.com/openapi/api?key=ec961279f453459b9248f0aeb6600bbe&info=怎么又是你")
print(res.text) # 输出为一行文本
res_dict = res.json() # 将响应转为json对象（字典）等同于`json.loads(res.text)`
print(res_dict)
print(json.dumps(res_dict, indent=2, sort_keys=True, ensure_ascii=False))


# 使用回话保存

s = requests.session()
url = "https://demo.fastadmin.net/admin/index/login.html"
data = {"username": "admin", "password": "123456"}
print(type(data))
s.post(url, data)
res = s.get("https://demo.fastadmin.net/admin/dashboard?ref=addtabs") # 使用同一个会话发送get请求，可以保持登录状态
# print(res.text)

cookies = {
    "PHPSESSID": "06a44b0970a3922303aaaa82a93290ce",
    "PHPSESSID": "30ccf166a09b41c3d4b4bd1717ca7374"

}


url = "https://demo.fastadmin.net/admin/dashboard?ref=addtabs"
cookies = {"PHPSESSID": "9bf6b19ddb09938cf73d55a094b36726"}
res = requests.get(url=url, cookies=cookies) # 携带cookies发送请求
print(res.text)
'''