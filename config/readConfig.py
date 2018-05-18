# encoding: utf-8

import os
import configparser

curpath = os.path.dirname(os.path.realpath(__file__))
configpath = os.path.join(curpath, "cfg.ini")
conf = configparser.ConfigParser()
conf.read(configpath)

smtp_server = conf.get('email', 'smtp_server')
sender = conf.get('email', 'sender')
psw = conf.get('email', 'psw')
receiver = conf.get('email', 'receiver')
port = conf.get('email', 'port')