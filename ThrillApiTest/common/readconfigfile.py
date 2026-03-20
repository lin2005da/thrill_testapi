'''
  @Project ：JungleApiTest 
  @File ：readconfigfile.py 
  @Author ：lin20 
  @Date ：2025/9/19 11:50 
  @Describe：读取配置文件
 '''
from configparser import ConfigParser
class ReadConfig:
    def __init__(self,file):
        self.cf=ConfigParser()
        self.cf.read(file,encoding='utf_8')
    def get_value(self,section,option):
        return self.cf.get(section,option)
    def get_int(self,section,option):
        return self.cf.getint(section,option)
    def get_fload(self,section,option):
        return self.cf.getfloat(section,option)
    def get_booloan(self,section,option):
        return self.cf.getboolean(section,option)