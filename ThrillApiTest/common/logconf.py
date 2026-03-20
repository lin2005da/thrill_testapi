'''
  @Project ：JungleApiTest 
  @File ：logconf.py 
  @Author ：lin20 
  @Date ：2025/9/19 11:40 
  @Describe：生成日志格式，当前定义级别为debug
 '''
import logging
import logging.handlers
from common import route
import os
import datetime
class Getlog:
    def __init__(self):
        self.log = logging.getLogger('web')
        self.log.setLevel(logging.DEBUG)

        # avoid log propagation to root (prevents duplicate messages when root handlers exist)
        self.log.propagate = False

        # only add handlers once — if Getlog() is instantiated multiple times, avoid adding duplicate handlers
        if not self.log.handlers:
            formatter = logging.Formatter('%(asctime)s-%(levelname)s-line:%(lineno)d-日志信息:%(message)s')

            file_name = os.path.join(route.log_dir, "log_{0}".format(datetime.datetime.now().strftime('%Y%m%d')))

            file_log = logging.handlers.RotatingFileHandler(filename=file_name, maxBytes=20*1024*1024, backupCount=10, encoding='utf_8')
            file_log.setLevel(logging.INFO)
            file_log.setFormatter(formatter)
            self.log.addHandler(file_log)

            # console 日志
            stream_log = logging.StreamHandler()
            stream_log.setLevel(logging.DEBUG)
            stream_log.setFormatter(formatter)
            self.log.addHandler(stream_log)
    def info(self,msg):
        return self.log.info(msg)
    def warning(self,msg):
        return self.log.warning(msg)
    def debug(self,msg):
        return self.log.debug(msg)
    def error(self,msg):
        return self.log.error(msg)
    def critical(self,msg):
        return self.log.critical(msg)

if __name__ == '__main__':
    s=Getlog()
    s.info('这是一条info')
    s.warning('这是一条info')
    s.debug('这是一条info')
    s.error('这是一条info')
    s.critical('这是一条info')