#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
#----------------------------------------------
# Copyright (python) 
# FileName: calculator.py
# Version: 0.0.2
# Author : baiyang
# LastChange: 2017/7/27  14:52
# Desc:
# History:
#--------------------------------------------
"""


class Count:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b
