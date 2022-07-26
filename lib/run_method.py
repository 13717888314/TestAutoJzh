#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os,sys,json,requests
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
class RunMethod:
    def __init__(self):
        # 实例化一个叫做session类,让session发送get,或者post等请求
        self.send = requests.session()
    def PostMethod(self,url,body,header):
        res = self.send.post(url=url, json=body, headers=header,verify=False)
        return res
    def GetMethod(self,url,body,header):
        res = self.send.get(url=url, params=body, headers=header,verify=False)
        return res
    def PutMethod(self,url,body,header):
        res = requests.put(url=url, data=body, headers=header,verify=False)
        return res
    def DeleteMethod(self,url,body,header):
        res = requests.delete(url=url, params=body,headers=header, verify=False)
        return res
    def run_main(self,method,url,body,headers):
        try:
            if method=="post":
                res= self.PostMethod(url,body,headers)
            elif method=="get":
                res=self.GetMethod(url,body,headers)
            elif method=="put":
                res=self.PutMethod(url,body,headers)
            else:
                res=self.DeleteMethod(url,body,headers)
            return res
        except Exception as  error:
            return error