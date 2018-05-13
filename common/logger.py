# encoding: utf-8

import logging
import os

cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path), 'logs')
log_name = os.path.join(log_path, 'aa')

print(log_path)

logger = logging.getLogger()
logger.setLevel(level=logging.INFO)

handler = logging.FileHandler(log_name)
handler.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(filename)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
# handler.close()
logger.info('start print log')
logger.debug('Do something')
logger.warning('Something maybe fail')
logger.info('Finish')