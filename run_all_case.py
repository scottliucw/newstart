# -*- coding: utf-8 -*-

import unittest
import os
import time
from common import HTMLTestRunner_api


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
                                               description="用例执行情况")
    runner.run(case)
    fp.close()

if __name__ == '__main__':
    cases = add_case()
    run_case(cases)
