# encoding: utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def send_mail(sender, psw, receiver, smtpserver, report_file, port):
    with open(report_file, 'rb') as f:
        mail_body = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = u'自动化测试报告'
    msg['from'] = sender
    msg['to'] = receiver
    msg.attach(body)
    # 添加附件
    att = MIMEText(mail_body, 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename = "report.html"'
    msg.attach(att)

    try:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
    except:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, port)

    # 用户名密码
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print(u'邮件发送成功！')
