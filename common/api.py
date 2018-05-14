# encoding: utf-8

import json
import requests
from common.readexcel import ExcelUtil
from common.wirteexcel import copy_excel, Write_excel

def send_requests(s, testdata):
    method = testdata['method']
    url = testdata['url']
    try:
        params = eval(testdata['params'])
    except:
        params = None
    try:
        headers = eval(testdata['headers'])
        print('请求头部: %s' % headers)
    except:
        headers = None
    type = testdata['type']

