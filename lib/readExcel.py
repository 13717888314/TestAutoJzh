#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import xlrd,json,re
from config import setting
from lib.getRandomData import RandomNumber
class ReadExcel():
    """读取excel文件数据"""
    def __init__(self,fileName=None, sheet_id=None):
        self.rn=RandomNumber()
        if fileName:
            self.fileName=fileName
            self.sheet_id=sheet_id
        else:
            sheet_id=0
            fileName=setting.SOURCE_FILE
        self.data = xlrd.open_workbook(fileName)
        self.table = self.data.sheet_by_index(sheet_id)
        # 获取总行数、总列数
        self.nrows = self.table.nrows
        self.ncols = self.table.ncols
    def read_data(self):
        if self.nrows > 1:
            # 获取第一行的内容，列表格式
            keys = self.table.row_values(0)
            listApiData = []
            # 获取每一行的内容，列表格式
            for col in range(1, self.nrows):
                values = self.table.row_values(col)
                # keys，values组合转换为字典
                api_dict = dict(zip(keys, values))
                # print(api_dict)
                if api_dict['is_run']=="yes":
                    listApiData.append(api_dict)
                    # print(api_dict)
            return listApiData
        else:
            print("表格是空数据!")
            return None