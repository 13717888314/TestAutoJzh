#!/user/bin/env python
#-*- coding:utf-8-*-
#获取随机数
import string,random,datetime
class RandomNumber:
    #这是一个随机生成邮箱,身份证号,手机号的类
    def mobile(self):
        """随机生成手机号"""
        mobile_head = ['134', '135', '188', '185', '172', '152']
        mobile_tail=''.join(random.sample(string.digits,8))
        mobile=random.choice(mobile_head)+mobile_tail
        return mobile
    def email(self):
        """随机生成邮箱"""
        h_email=['@qq.com','@163.com','@199.com']
        email_head = str(random.randint(111111, 999999))
        user_email=email_head+random.choice(h_email)
        return user_email
    def idCard(self):
        """随机生成身份证号"""
        icard_head = str(random.randint(111111,999999))
        icard_tail = str(random.randint(11111,99999))
        icard = icard_head+ str(1993020)+icard_tail
        return icard
    def randomNumber(self):
        """随机随机数"""
        randomData=str(random.randint(11111111, 99999999))
        return randomData
    def getRandomDate(self,random_name):
        if random_name=="mobile":
            randoms =self.mobile()
        elif random_name=="email":
            randoms =self.email()
        elif random_name=="idCard":
            randoms=self.idCard()
        else:
            randoms =self.randomNumber()
        return randoms