from lib.operationJson import operetionJson
from lib.getRandomData import RandomNumber
import re
class openrationDict:
    """
    这是一个解析dict参数的类,
    可用于多参数的指定key,指定key集合解析key,更新指定key的值
    """
    def __init__(self):
        self.oj=operetionJson()
        self.rn=RandomNumber()
    def get_value(self,my_dict,key):
        """
        这是一个递归函数
        :param my_dict: 传入的字典
        :param key: 字典中的key
        :return:返回字典中某个key对应的值
        """
        try:
            if isinstance(my_dict,dict):
                if my_dict.get(key)or my_dict.get(key)==0 or my_dict.get(key)==''\
                        and my_dict.get(key) is False:
                    return my_dict.get(key)
                for my_dict_key in my_dict:
                    if self.get_value(my_dict.get(my_dict_key),key)or\
                        self.get_value(my_dict.get(my_dict_key),key)is False:
                        return self.get_value(my_dict.get(my_dict_key),key)
            if isinstance(my_dict,list):
                for my_dict_arr in my_dict:
                    if self.get_value(my_dict_arr,key)\
                        or self.get_value(my_dict_arr,key)is False:
                        return self.get_value(my_dict_arr,key)
        except Exception as el:
            print(el)
    def get_response_date(self,res,extract_data):
        """
        通过响应数据中的key,获取value并写入json文件
        :param res: 接口返回数据
        :param extract_data: 要提取的数据
        :return:返回一个字典
        """
        if isinstance(extract_data,str):
            extract_data=eval(extract_data)
        for key,extract_content in extract_data .items():
            global write_dict
            key_list=[]
            value_list=[]
            if key=="extractBody":
                for key ,value in extract_content.items():
                    key_list.append(value)
                    value_list.append(self.get_value(res,key))
                    print("获取提取字段:{0},提取值:{1}".format(key, self.get_value(res,key)))
                    write_dict = dict(zip(key_list, value_list))
                    print("写入.json文件成功,写入字段:{0},写入值:{1}".format(value, self.get_value(res, key)))
                self.oj.write_data(write_dict)#写入json文件
    def update_request_data(self,api_dict):
        """

        :param api_dict:原有请求入参
        :return:更新的的入参
        """
        extract_dict = re.findall(r"[$]{(.+?)}", str(api_dict))
        if len(extract_dict) > 0:
            for key in range(len(extract_dict)):
                extract_dict_key = extract_dict[key]
                old = "${" + extract_dict_key + "}"
                if "random" in extract_dict_key:
                    random_id = extract_dict_key.split("_")[1]
                    new = self.rn.getRandomDate(random_id)
                    api_dict = eval(str(api_dict).replace(old, str(new)))
                else:
                    new = self.oj.get_data(extract_dict_key)
                    api_dict = eval(str(api_dict).replace(old, str(new)))
            return api_dict