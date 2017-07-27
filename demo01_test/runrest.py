#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
#----------------------------------------------
# Copyright (python) 
# FileName: runrest.py
# Version: 0.0.2
# Author : baiyang
# LastChange: 2017/7/27  15:01
# Desc:
# History:
#--------------------------------------------
"""
'''一般构造测试集，这样操作比较繁琐，需要重复打入测试用例'''

import unittest
import testadd
import testsub

# 构造测试集
suite = unittest.TestSuite()
suite.addTest(testadd.TestAdd("testadd1"))
suite.addTest(testadd.TestAdd("test_add2"))
suite.addTest(testsub.TestSub("testsub1"))
suite.addTest(testsub.TestSub("test_sub2"))

if __name__ == "__main__":
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
