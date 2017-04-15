#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/29 15:54
# @Author  : maojx
# @Site    : 
# @File    : 发送邮件.py
# @Software: PyCharm

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

msg = MIMEMultipart()
msg = MIMEText("邮件内容", 'plain', 'utf-8')
msg['From'] = 'maojiaxu@yeah.net'
msg['To'] = '452212889@qq.com'
msg['Subject'] = "主题"
att1 = MIMEText(open('E:/123.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
msg.attach(att1)

server = smtplib.SMTP("smtp.yeah.net", 25)
server.login("maojiaxu@yeah.net", "!mjx452212889")
server.sendmail('maojiaxu@yeah.net', '452212889@qq.com', msg.as_string())
server.quit()

"""
SMTP是发送邮件的协议，Python内置对SMTP的支持,可以发送纯文本邮件、HTML邮件以及带附件的邮件。
Python对SMTP支持有smtplib和email两个模块,email负责构造邮件,smtplib负责发送邮件。
"""
from email.mime.text import MIMEText

msg = MIMEText('hello,send by Python...', 'plain', 'utf-8')
# 构造的MIMEText对象时,第一个参数就是邮件正文,第二个参数是MIME的subtype,传入‘plain’表示纯文本,最终的MIME就是'text/plain',最后一定要用utf-8编码保证多语言兼容性。
