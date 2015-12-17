# data_mongoToOracle.py

import cx_Oracle
import mongoToOracle_settings as settings
import pymongo
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'