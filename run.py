import unittest,sys
from config import setting
sys.path.append(setting.BASE_DIR)#将模块的路径通过sys.path.append(路径)添加到主程序中
from BeautifulReport import BeautifulReport
import os
from lib.sendEmail import send_email
import yagmail
import datetime
from lib.configEmail import sendMail
from lib.configEmail import att
from bs4 import BeautifulSoup

# if __name__ == '__main__':
#     """
#     通过该类defaultTestLoader下面的discover()方法
#     可自动更具测试目录start_dir匹配查找测试用例文件（test*.py），
#     并将查找到的测试用例组装到测试套件
#     """
#     print(setting.BASE_DIR)
#     test_suite = unittest.defaultTestLoader.discover('testcase', pattern='test*.py')
#     result = BeautifulReport(test_suite)
#     result.report(filename='测试报告', description='接口自动化测试报告', log_path='report')



# 把测试报告作为附件发送到指定邮箱
def send_mail(report):
    yag = yagmail.SMTP(user="zihan.jia@goldentec.com", password="Xlueness@456", host='imap.exmail.qq.com')
    subject = "自动化测试报告"
    contents = "自动化用例已执行完毕，详细报告请查看附件"
    yag.send('zihan.jia@goldentec.com',subject,contents,report)
    print("邮件已经发送成功！")


# def send_mail(subject, report_file, file_names):
#     # 读取测试报告内容，作为邮件的正文内容
#     with open(report_file, "rb") as f:
#         mail_body = f.read()
#     send_email(subject, mail_body, file_names)

def get_report(report_path):
    list = os.listdir(report_path)
    list.sort(key=lambda x: os.path.getmtime(os.path.join(report_path, x)))
    print("测试报告：", list[-1])
    report_file = os.path.join(report_path, list[-1])
    return report_file



if __name__ == '__main__':
    root_dir = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
    # report_path = os.path.join(root_dir, "report")  # 测试报告路径
    # report_file = get_report(report_path)  # 测试报告文件
    # subject = "C端生产环境接口测试报告"  # 邮件主题
    # file_names = [report_file]  # 邮件附件
    # # 发送邮件
    # send_mail(subject, report_file, file_names)
# cur_path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')


# 加载测试用例：指定E:\\08PyCharmProject\\Case1\\test_case目录，“test*.py”匹配指定目录下所有test开头的.py文件
#     test_suite = unittest.defaultTestLoader.discover('E:\\UI test\\UnittestProject\\TestCases', pattern='test*.py')

    test_suite = unittest.defaultTestLoader.discover("./testcase", 'testApi.py')
    # 获取当前时间，用于命名测试报告标题
    now = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    # 将用例加到对象中
    result = BeautifulReport(test_suite)
    # report方法实现了用例的执行、用例执行结束的结果统计、生成测试报告等操作
    # ：filename -> 测试报告名称, 如果不指定默认文件名为report.html，description -> 测试报告用例名称展示，report_dir-> 报告文件写入路径
    # result.report(filename='C端自动化测试报告'+str(now), description='C端自动化测试报告', report_dir='D:\\TestAutoJzh\\report')
    # result.report(filename='C端自动化测试报告', description='C端自动化测试报告', report_dir='D:\\TestAutoJzh\\report')
    result.report(filename='C-master-api-AutoTestReport', description='C-master-api-AutoTestReport', report_dir='C:\\Users\\zihan.jia\\.jenkins\\workspace\\C-master-api-AutoTest')
    html_report = root_dir+ '/report/C端自动化测试报告'+'.html' # 这个要注意要带目录路径，如果直接附文件名，程序会找不到路径
    # send_mail(html_report)
    # 发送邮件
    # sendMail()

'''
filename:报告标题
description：报告描述
theme：主题    
report_dir：存放路径
'''
# result.report(
#     filename="C端自动化测试报告",
#     description="C端自动化测试报告",
#     theme="theme_default",
#     report_dir=root_dir+'\\report\\'
# )

