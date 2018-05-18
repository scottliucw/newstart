# -*- coding: utf-8 -*-

import unittest
import os
import time
from common import HTMLTestRunner_api
from common import email
from config import readConfig


curpath = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(curpath, "report")
if not os.path.exists(report_path):
    os.mkdir(report_path)
case_path = os.path.join(curpath, "case")


def add_case(casepath=case_path, rule='test*.py'):
    discover = unittest.defaultTestLoader.discover(start_dir=casepath,
                                                   pattern=rule,
                                                   top_level_dir=None)
    return discover


def run_case(case, reportpath=report_path):
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    htmlreport = reportpath + '\\' + now + '_result.html'
    print("测试报告生成地址：%s" % htmlreport)
    fp = open(htmlreport, "wb")
    runner = HTMLTestRunner_api.HTMLTestRunner(stream=fp,
                                               verbosity=2,
                                               retry=5,
                                               title="测试报告",
                                               description="用例执行情况",
                                               save_last_try=True)
    runner.run(case)
    fp.close()


def get_report_file(report_path):
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    report_file = os.path.join(report_path, lists[-1])
    return report_file

if __name__ == '__main__':
    cases = add_case()
    run_case(cases)
    report_path = os.path.join(curpath, 'report')
    report_file = get_report_file(report_path)
    sender = readConfig.sender
    psw = readConfig.psw
    smtp_server = readConfig.smtp_server
    port = readConfig.port
    receiver = readConfig.receiver
    email.send_mail(sender, psw, receiver, smtp_server, report_file, port)
