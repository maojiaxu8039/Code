#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/30 11:41
# @Author  : maojx
# @Site    : 
# @File    : mail.py
# @Software: PyCharm

# -*- coding: utf-8 -*-
import smtplib
import os.path

from email.encoders import encode_base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

From = "maojiaxu@yeah.net"
To = "452212889@qq.com"
file_name = "E:/123.txt"  # 附件名

server = smtplib.SMTP("smtp.yeah.net")
server.login("maojiaxu@yeah.net", "!mjx452212889")  # 仅smtp服务器需要验证时

# 构造MIMEMultipart对象做为根容器
main_msg = MIMEMultipart()

# 构造MIMEText对象做为邮件显示内容并附加到根容器
text_msg = MIMEText("我this is a test text to text mime", _charset="utf-8")
main_msg.attach(text_msg)

# 构造MIMEBase对象做为文件附件内容并附加到根容器
contype = 'application/octet-stream'
maintype, subtype = contype.split('/', 1)

# 构造MIMEBase对象做为文件附件内容并附加到根容器
data = open(file_name, 'rb')
file_msg = MIMEText(maintype, subtype,"utf-8")
file_msg.set_payload(data.read( ))
data.close( )
encode_base64(file_msg)

## 设置附件头
basename = os.path.basename(file_name)
file_msg.add_header('Content-Disposition', 'attachment', filename=basename)  # 修改邮件头
main_msg.attach(file_msg)

# 设置根容器属性
main_msg['From'] = From
main_msg['To'] = To
main_msg['Subject'] = "attach test "
main_msg['Date'] = formatdate()

# 得到格式化后的完整文本
fullText = main_msg.as_string()

# 用smtp发送邮件
try:
    server.sendmail(From, To, fullText)
finally:
    server.quit()
