#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
#----------------------------------------------
# Copyright (python) 
# FileName: test_skip.py
# Version: 0.0.2
# Author : baiyang
# LastChange: 2017/7/27  15:21
# Desc:
# History:
#--------------------------------------------
"""
import unittest




class MyTest(unittest.TestCase):
    def setUp(self):
        print ("test case start")

    def tearDown(self):
        print ("test case start")

    @unittest.skip("直接跳过测试")   # 无条件跳过测试，括号说过跳过测试的原因
    def test_skip(self):
        print ("test aaa")

    @unittest.skipIf(3>2,"当条件为True时跳过测试")   # 如果条件为真时跳过测试，
    def test_skip_if(self):
        print ("test bbb")

    @unittest.skipUnless(3 > 2, "当条件为True时执行测试")    # 只有在条件为真施执行测试
    def test_skip_unless(self):
        print ("test ccc")

    @unittest.expectedFailure   # 测试标记为失败，不管执行结果是否失败，统一标记为失败
    def test_expcted_failyre(self):
        assertEqual(2.3)


if __name__=="__main__":
    unittest.main()