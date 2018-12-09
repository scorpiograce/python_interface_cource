# 1.组装邮件正文
# 2.组装邮件头
# 3.连接STMP服务器并发送

import smtplib # 连接smtp服务器并发送邮件
from email.mime.text import MIMEText

# 1.组装邮件正文
body=MIMEText('python发送的邮件','plain','utf-8')
# 2.组装邮件头
body['From']='test_results@sina.com'
body['To']='superhin@126.com'
body['Subject']="from python"
# 3.连接stmp服务器并发送
smtp=smtplib.SMTP_SSL("smtp.sina.com") #.SMTP()是普通方法，.SMTP()是加密方法
smtp.login("test_results@sina.com","hanzhichao123") #登录邮箱，没有报错说明密码是对的
smtp.sendmail("test_results@sina.com","superhin@126.com",body.as_string())
