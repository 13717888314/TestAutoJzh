#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import re,sys,warnings,urllib3,os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest,requests,json
from config import myddt
from lib.readExcel import ReadExcel
from lib.run_method import RunMethod
from lib.operationDict import openrationDict
from lib.operationJson import operetionJson
testData = ReadExcel().read_data()
@myddt.ddt
class C_master_api(unittest.TestCase):
    def setUp(self):
        self.op_dict=openrationDict()
        self.op_json=operetionJson()
    @myddt.data(*testData)
    def test_api(self,data):
        #通过warnings库来忽略掉相关告警,去掉提示信息ResourceWarning...
        warnings.simplefilter("ignore", ResourceWarning)
        if re.findall(r"[$]{(.+?)}", str(data)):#判断请求数据中有要更新的数据
            data=self.op_dict.update_request_data(data)
        self.url=data['url']
        self.case_name=data['case_name']
        self.method=data['method']
        self.header=data["header"]
        self.body=eval(data['body'])
        self.extract_data=data['getResponseData']#提取字段
        self.readData_code =data["code"]  # 获取excel表格数据的状态码
        if self.header=="":
            self.header=None
        else:
            self.header=eval(self.header)
        requests.packages.urllib3.disable_warnings()#解决Python3控制台输出InsecureRequestWarning的问题
        print("******* 正在执行用例 ->{0} *********".format(self.case_name))
        print("请求方式: {0}，请求URL: {1}".format(self.method, self.url))
        print("请求数据类型为:{0} 请求header为:{1}".format(type(self.header), self.header))
        print("请求数据类型为:{0} 请求body为:{1}".format(type(self.body), self.body))
        self.re = RunMethod().run_main(self.method,self.url,self.body,self.header)# 发送请求
        if self.re.status_code == 200:#网页正常访问,要执行的操作
            print("页面返回信息：%s" % json.dumps(self.re.json(), ensure_ascii=False, indent=4))
            self.assertIn(self.readData_code,self.re.text,"返回实际结果是->:%s" % self.re.json())
            if self.extract_data:
                self.op_dict.get_response_date(self.re,self.extract_data)
        else:
             self.assertEqual(self.re.status_code, 200,"返回状态码status_code:{}".format(str(self.re.status_code)))
if __name__=='__main__':
    unittest.main()