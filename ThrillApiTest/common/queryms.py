'''
  @Project ：JungleApiTest 
  @File ：queryms.py 
  @Author ：lin20 
  @Date ：2025/9/19 13:34 
  @Describe：调用数据库查询数据
 '''
from common.readconfigfile import ReadConfig
from common import route

_HAS_PYMYSQL = True
try:
    import pymysql
    import pymysql.cursors
except Exception:
    _HAS_PYMYSQL = False


class MSql:                        #调用数据库
    def __init__(self,result_dict=False):
        if not _HAS_PYMYSQL:
            raise ImportError("pymysql 未安装，请运行: pip install pymysql")

        y = ReadConfig(route.conffile)
        host = y.get_value('db', 'host')
        user = y.get_value('db', 'user')
        password = y.get_value('db', 'pwd')
        port = int(y.get_value('db', 'port'))
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=port)
        if result_dict:
            self.curser = self.mysql.cursor(pymysql.cursors.DictCursor)  # 生成列表
        else:
            self.curser = self.mysql.cursor()   # 生成元组
    def fetch_one(self,sql):
        self.curser.execute(sql)         #读取sql语句
        result=self.curser.fetchone()       #返回结果
        return result
    def fetch_all(self,sql):
        self.curser.execute(sql)         #读取sql语句
        result=self.curser.fetchall()       #返回结果
        return result
    def close(self):
        self.curser.close()
        self.mysql.close()
if __name__ == '__main__':
    t = MSql(result_dict=False)
    sql = 'SELECT * FROM bingo_jungle.users_other_charge WHERE id=300158 ;'
    y = t.fetch_all(sql)
    print(y)