# encoding: utf-8

import xlrd
import os
import time

# data = xlrd.open_workbook('D:\\test\\testcase.xlsx')
# table = data.sheet_by_name('Sheet1')

# keys = table.row_values(0)

# print(keys)

# a = list(range(5))
# print(a)

# for i in list(range(2)):
#    print(i)

# print(type(list(range(2))))

# i = '%s%d' % ('a', 2)
# print(i)

# print(type(chr(97)))

curpath = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(curpath, "report")
print(report_path)

