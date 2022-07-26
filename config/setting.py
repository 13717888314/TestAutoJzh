#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os,sys,requests,json
#去掉文件名,返回目录
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
# 配置文件,os.path.join(path1[, path2[, ...]])将多个路径组合后返回
TEST_CONFIG =  os.path.join(BASE_DIR,"database","config.ini")
# 测试用例模板文件
SOURCE_FILE = os.path.join(BASE_DIR,"database","dataNew.xlsx")
#提取字段文件
TEST_JSON =  os.path.join(BASE_DIR,"database","user.json")
# excel测试用例结果文件
TARGET_FILE = os.path.join(BASE_DIR,"report","excelReport","data.xlsx")
# 测试用例报告
TEST_REPORT = os.path.join(BASE_DIR,"report")
# 测试用例程序文件
TEST_CASE = os.path.join(BASE_DIR,"testcase")

