# 1.组装邮件正文
# 2.组装邮件头
# 3.连接STMP服务器并发送

import smtplib # 连接smtp服务器并发送邮件
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart #混合格式
"""
# 1.组装邮件正文
msg=MIMEMultipart() # 混合格式消息体
body=MIMEText('python发送的邮件','plain','utf-8')
msg.attach(body) # 将正文添加到msg对象中
# 2.组装邮件头
msg['From']='test_results@sina.com'
msg['To']='superhin@126.com'
msg['Subject']="from python"
# 4.附件
with open("../report/report.html","rb") as f:
    att_file=f.read()
att=MIMEText(att_file,'base64','utf-8') #指定传输编码格式和解码格式
att["Content-Type"]='application/octet-stream' #声明附件的内容格式 MIME数据流格式
att["Content-Disposition"]="attachment;filename='report.html'" #附件描述信息 filename是附件显示的文件名
msg.attach(att)  #将附件添加到消息对象中
# 3.连接stmp服务器并发送
smtp=smtplib.SMTP_SSL("smtp.sina.com") #.SMTP()是普通方法，.SMTP()是加密方法
smtp.login("test_results@sina.com","hanzhichao123") #登录邮箱，没有报错说明密码是对的
smtp.sendmail("test_results@sina.com","superhin@126.com",body.as_string())
"""
# 1.组装邮件正文
msg=MIMEMultipart() # 混合格式消息体
body=MIMEText('python发送的邮件','plain','utf-8')
msg.attach(body) # 将正文添加到msg对象中
# 2.组装邮件头
msg['From']='scorpiograce@163.com'
msg['To']='scorpiograce@163.com'
msg['Subject']="from python"
# 4.附件
with open("../report/report.html","rb") as f:
    att_file=f.read()
att=MIMEText(att_file,'base64','utf-8') #指定传输编码格式和解码格式
att["Content-Type"]='application/octet-stream' #声明附件的内容格式 MIME数据流格式
att["Content-Disposition"]='attachment;filename="report.html"' #附件描述信息 filename是附件显示的文件名
msg.attach(att)  #将附件添加到消息对象中
# 3.连接stmp服务器并发送
smtp=smtplib.SMTP_SSL("smtp.163.com") #.SMTP()是普通方法，.SMTP()是加密方法
smtp.login("scorpiograce@163.com","grace327530") #登录邮箱，没有报错说明密码是对的
smtp.sendmail("scorpiograce@163.com","scorpiograce@163.com",msg.as_string())
