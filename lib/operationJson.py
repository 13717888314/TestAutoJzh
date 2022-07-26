#!/user/bin/env python
#-*- coding:utf-8-*-
import json,os,sys
from config import setting
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
class operetionJson:
    def read_data(self):
        self.file_path = setting.TEST_JSON
        try:
            with open(self.file_path, "r", encoding='utf-8') as json_file:
                data = json.load(json_file)
                json_file.close()
                return data
        except Exception as error:
            return"读取json文件异常"
    def get_data(self,id):
        """
        根据关键字获取json文件中数据
        :param id:json文件中对应的key
        :return: json文件中key对应的value
        """

        try:
            self.data = self.read_data()
            return self.data[id]
        except Exception as error:
            return "根据关键字:{}获取json文件中数据value失败,请检查json文件中是否存在key={}的字段".format(id,id)
    def write_data(self,data):
        """
        将字典写入json文件中
        :param data:
        :return:
        """
        try:
            json_data=self.read_data()
            json_data.update(data)
            with open(self.file_path,'w') as fp:
                fp.write(json.dumps(json_data))
        except Exception as  error:
            return "文件写入失败,报错信息为:{}".format(error)