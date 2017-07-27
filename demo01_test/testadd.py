#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
#----------------------------------------------
# Copyright (python) 
# FileName: testadd.py
# Version: 0.0.2
# Author : baiyang
# LastChange: 2017/7/27  14:54
# Desc:
# History:
#--------------------------------------------
"""

from calculator import Count
import unittest


class TestAdd(unittest.TestCase):
    def setUp(self):
        print ("test case start")

    def tearDown(self):
        print ("test case start")

    def testadd1(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)

    def test_add2(self):
        j = Count(41, 76)
        self.assertEqual(j.add(), 117)


if __name__ == "__main__":
    unittest.main()
