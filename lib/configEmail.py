import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# from logs import logs
from config import setting
import configparser
# path = os.path.dirname(os.path.abspath(__file__))
# 获取上上级目录
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


# 查找最新的测试报告
def newReport():
    # 定义文件目录
    result_dir = path + '\\report'
    lists = os.listdir(result_dir)
    # 重新按时间对目录下的文件进行排序
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn))
    # print(('最新的文件为： ' + lists[-1]))
    file = os.path.join(result_dir, lists[-1])
    print(file)
    return file


# 上传附件
def att(path, name):
    sendfile = open(path, 'rb').read()
    att = MIMEText(sendfile, 'base64 ', 'utf-8')
    att['Content-type'] = 'application/octet-stream'
    # 附件在邮件中显示的名字
    att['Content-Disposition'] = 'attachment;filename= "' + name + '"'
    return att


def sendMail():
    cur_path = os.path.dirname(os.path.realpath(__file__))  # 当前文件的所在目录
    configPath = os.path.join(cur_path, "email_config.ini")  # 路径拼接：/config/email_config.ini
    conf = configparser.ConfigParser()
    conf.read(configPath, encoding='UTF-8')  # 读取/config/email_config.ini 的内容

    smtpserver = conf.get("email", "smtp_server")  # 发送者邮件服务器
    mailuser = conf.get("email", "user_name")  # 发送着邮件账户
    password = conf.get("email", "password") # 发送者邮件授权码
    receiver = conf.get("email", "receiver")  # 接收者邮件账户
    subject = conf.get("email", "subject")  # 邮件标题
    mailbody =  conf.get("email", "mailbody")  # 邮件正文
    reportAttachment = conf.get("email", "subject")  # 报告附件名称
    # AlllogAttachment = User.AlllogAttachment  # 所有日志附件名称
    # ErrorlogAttachment = User.ErrorlogAttachment  # 错误日志附件名称
    file1 = newReport()
    # file2 = path + '\\logs\\Error_Logs\\Errorlog.log'
    # file3 = path + '\\logs\\All_Logs\\Alllog.log'
    msg = MIMEMultipart()
    # 附件加入到邮件中
    msg.attach(att(file1, reportAttachment))
    # msg.attach(att(file2, AlllogAttachment))
    # msg.attach(att(file3, ErrorlogAttachment))
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = mailuser  # 之前没有写From和To,发送邮件出现554错误
    msg['To'] = receiver
    msg.attach(MIMEText(mailbody, 'plain', 'utf-8'))

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(mailuser, password)
    smtp.sendmail(mailuser, receiver, msg.as_string())
    # smtp.quit()
    # except Exception:
    #     logs.smtplib('Error')
    # else:
    #     logs.smtplib('Success')

