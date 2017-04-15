#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/29 16:34
# @Author  : maojx
# @Site    : 
# @File    : EmaliHelper.py
# @Software: PyCharm
"""

"""
import os
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.encoders import encode_base64


class email:
    """
    发件人：senders
    发件人密码：senderspassword
    收件人：recipient
    邮件内容：content
    主题：theme
    附件：attachments
    """

    def __init__(self, senders, password, recipient, theme, content="", attachments=[]):
        self.mail_senders = senders
        self.mail_password = password
        self.mail_recipient = recipient
        self.mail_theme = theme
        self.mail_content = content
        self.mail_attachments = attachments
        self.smtp_host = "smtp.yeah.net"
        self.smtp_port = 25

    def send_mail(self):
        # 声明一个邮件对象
        msg = MIMEMultipart()
        # 发件人地址
        msg['From'] = self.mail_senders
        # 收件人地址
        msg['To'] = ";".join(self.mail_recipient)  # 将收件人列表以;分隔
        # 邮件主题
        msg['Subject'] = self.mail_theme
        # 邮件正文
        msg.attach(MIMEText(self.mail_content, 'plain', 'utf-8'))
        # 判断是否有附件
        if len(self.mail_attachments) > 0:
            # 遍历附件路径
            for mail_attachment in self.mail_attachments:
                # 附件添加到邮寄对象
                msg.attach(self.get_attachment(mail_attachment))
        # 调用SMTP
        server = smtplib.SMTP(self.smtp_host, self.smtp_port)
        # 登陆邮件服务器
        server.login(self.mail_senders, self.mail_password)
        # 发送邮件
        server.sendmail(self.mail_senders, self.mail_recipient, msg.as_string())
        # 发送完成
        server.quit()

    # 判断附件类型并返回附件
    def get_attachment(self, file_name):
        content_type, encoding = mimetypes.guess_type(file_name)
        if content_type is None or encoding is not None:
            content_type = "application/octet-stream"
        main_type, sub_type = content_type.split('/', 1)
        file = open(file_name, "rb")
        attachment = MIMEBase(main_type, sub_type)
        attachment.set_payload(file.read())
        encode_base64(attachment)
        file.close()
        attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_name))
        return attachment

"""
def test():
    mail = email("maojiaxu@yeah.net", "!mjx452212889", ['maojiaxu@yeah.net'], "Python邮件测试", "邮件内容1",
                 ["E:/123.txt", "E:/456.png"])
    mail.send_mail()


if __name__ == '__main__':
    test()
"""
