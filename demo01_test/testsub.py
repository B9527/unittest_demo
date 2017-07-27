#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
#----------------------------------------------
# Copyright (python) 
# FileName: testsub.py
# Version: 0.0.2
# Author : baiyang
# LastChange: 2017/7/27  15:00
# Desc:
# History:
#--------------------------------------------
"""

from calculator import Count
import unittest


class TestSub(unittest.TestCase):
    def setUp(self):
        print ("test case start")

    def tearDown(self):
        print ("test case start")

    def testsub1(self):
        j = Count(2, 3)
        self.assertEqual(j.sub(), -1)

    def test_sub2(self):
        j = Count(41, 76)
        self.assertEqual(j.sub(), -35)


if __name__ == "__main__":
    unittest.main()
