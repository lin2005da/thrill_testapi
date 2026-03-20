import time
import unittest
from common import readconfigfile
from common import logconf
from common import readexceldata
from common import route
from common import generaterequestdata
import json
from ddt import ddt,data




loging=logconf.Getlog()
chargedata=readexceldata.doExcel(route.datafile)
case_chargecreate=chargedata.charge_data('chargecreate')
rconf = readconfigfile.ReadConfig(route.conffile)

@ddt
class TestChargeCreate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        loging.info("-------------{0}开始--------------".format(time.time()))
        try:
            # 游客登录获取token

            cls.guestdata = eval(rconf.get_value('data', 'guest_data'))

            loging.info(cls.guestdata)

            cls.guest_url = "/user/guest"
            cls.req_guest = generaterequestdata.GenerateRequestData(url=cls.guest_url, data=cls.guestdata,method="POST")
            loging.info("游客登录成功")

            cls.result_guest= cls.req_guest.reqapi().json()
            loging.info(cls.result_guest)

            cls.token=cls.result_guest['data']['user']['authorization']
            loging.info('登录token:{0}'.format(cls.token))

            cls.user_id = cls.result_guest['data']['user']['user_id']
            loging.info('user_id:{0}'.format(cls.user_id))
        except Exception as e:
            loging.error("游客登录失败:{0}".format(e))



    @data(*case_chargecreate)
    def test_chargecreate(self,item):
        loging.info("__开始执行：Id:{0}_title:{1}__".format(item.id, item.title))

        self.newdata = generaterequestdata.get_gps(userid=self.user_id, gps=item.gpsinfo, data_dict=item.data)
        loging.info("请求参数：{0}".format(newdata))
        req_chargecreate=generaterequestdata.GenerateRequestData(data=self.newdata,url=item.url,authorize=self.token,method="POST")
        result_chargecreate=req_chargecreate.reqapi().json()
        loging.info("请求结果：{0}".format(result_chargecreate))
        result=result_chargecreate['message']
        expect=json.loads(item.expect)['message']
        loging.info("expect:message={0},result:message={1}".format(expect,result))

        try:
            self.assertEqual(expect,result)
            loging.info('执行通过')
            chargedata.write_chargedata(sheet='chargecreate', w_row=item.id+1, actual=str(result_chargecreate), result='pass')
            loging.info("写入结果")
        except AssertionError as e:
            loging.error('执行出错：{0}'.format(e))
            chargedata.write_chargedata(sheet='chargecreate', w_row=item.id+1, actual=str(result_chargecreate), result='fail')
            loging.info("写入结果")
            raise e

        loging.info("__结束：Id:{0}_title:{1}__".format(item.id, item.title))




    @classmethod
    def tearDownClass(cls):
        loging.info("-------------结束--------------")


if __name__ == '__main__':
    unittest.main()
