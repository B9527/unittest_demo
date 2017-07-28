#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
#----------------------------------------------
# Copyright (python) 
# FileName: demo2_test.py
# Version: 0.0.2
# Author : baiyang
# LastChange: 2017/7/27  18:02
# Desc:
# History:
#--------------------------------------------
"""
import copy


list_01 = [{"key": "1", "value": "a"}, {"key": "2", "value": "b"}, {"key": "3", "value": "c"},
           {"key": "4", "value": "d"}]

list_02 = copy.deepcopy(list_01)
for iteam in list_02:
    print "qian", iteam
    list_01.remove(iteam)
    print "hou", iteam
