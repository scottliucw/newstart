# -*- coding: utf-8 -*-

import unittest
import os


case_path = os.path.join(os.getcwd(), 'case')

discover = unittest.defaultTestLoader.discover(start_dir=case_path,
                                               pattern='test*.py',
                                               top_level_dir=None)

print(discover)


unittest.TextTestRunner().run(discover)