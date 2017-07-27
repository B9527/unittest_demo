#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
#----------------------------------------------
# Copyright (python) 
# FileName: runtest_fast.py
# Version: 0.0.2
# Author : baiyang
# LastChange: 2017/7/27  15:09
# Desc:
# History:
#--------------------------------------------
"""

import unittest

# 定义测试用例的目录为当前目录,要加载testcases下的目录，需要在其下面加__init_.py文件


test_dir = './'
# discover(start_dir,pattern='test*.py',top_level_dir=NOne)
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(discover)
