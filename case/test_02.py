# -*- coding: utf-8 -*-

import unittest


class Test(unittest.TestCase):

    def setUp(self):
        print('start02!')

    def tearDown(self):
        print('end02!')

    def test001(self):
        print(u'执行测试用例004')

    def test002(self):
        print(u'执行测试用例005')

    def test003(self):
        print(u'执行测试用例006')

if __name__ == '__main__':
    unittest.main()