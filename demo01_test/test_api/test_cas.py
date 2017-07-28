#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
#----------------------------------------------
# Copyright (python) 
# FileName: test_cas.py
# Version: 0.0.2
# Author : baiyang
# LastChange: 2017/7/28  10:25
# Desc:
# History:
#--------------------------------------------
"""

import json
import requests

from calculator import Count
import unittest


def md5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()


class TestAdd(unittest.TestCase):
    def setUp(self):
        print ("test case API start")

    def tearDown(self):
        print ("test case API  stop")

    def testapi_cas(self):
        url = 'http://192.168.10.231:8822/api/cas/login'
        data = {"username": "CIBN", "password": md5("123456")}
        res = requests.post(url=url, data=json.dumps(data))
        self.assertEqual(res.status_code, 200)


# data = {"username": "CIBN", "password": md5("123456")}
# print type(json.dumps(data))
# # res=urllib2.urlopen(url=url,data=data)
# res = requests.post(url=url, data=json.dumps(data))
# print res.status_code
# print json.dumps(res.json(), sort_keys=True, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    unittest.main()
