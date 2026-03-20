'''
  @Project ：JungleApiTest
  @File ：test_charge.py
  @Author ：lin20
  @Date ：2025/10/27 11:00
  @Describe：接口：创建订单
 '''
import pytest
from common import readconfigfile
from common import logconf
from common import readexceldata
from common import route
from common import generaterequestdata
import json
import traceback



loging = logconf.Getlog()
chargedata = readexceldata.doExcel(route.datafile)
rconf = readconfigfile.ReadConfig(route.conffile)

#case_createdata 返回一个列表；这里需要第 2至11 行的用例对象
case_createdata = chargedata.charge_data('charge', 2, 11)
#case_channelquery 返回一个列表；这里需要第 12至21 行的用例对象
case_channelquery = chargedata.charge_data('charge', 12, 21)
# channelcreatedata 返回一个列表；这里只需要第 22 行的单个用例对象
case_channelcreatedata = chargedata.charge_data('charge', 22, 22)[0]
#case_chargequery 返回一个列表；这里需要第 23至28 行的用例对象
case_chargequery = chargedata.charge_data('charge', 23, 26)
#case_cardquery 返回一个列表；这里需要第 23至28 行的用例对象
case_cardquery = chargedata.charge_data('charge', 27, 27)



common_data=eval(rconf.get_value('data', 'common_data'))


class TestChargeCreate:
    @pytest.mark.usefixtures('guest_login')
    @pytest.mark.parametrize('item', case_createdata)
    @pytest.mark.chargecreate
    def test_chargecreate(self, guest_login, item):
        self.guest_dict = guest_login

        loging.info("__开始执行：Id:{0}_title:{1}__".format(item.category, item.title))
        # 修复：将item.data从字符串转换为字典后再更新
        item_data = json.loads(item.data) if isinstance(item.data, str) else item.data
        common_data.update(item_data)

        try:
            newdata = generaterequestdata.get_gps(userid=self.guest_dict["user_id"], gps=item.gpsinfo, data_dict=common_data)
            req_chargecreate = generaterequestdata.GenerateRequestData(data=newdata, url=item.url, authorize=self.guest_dict["authorization"],
                                                                       method=item.method)
            resp=req_chargecreate.reqapi()
            loging.info(f"{item.category}--API响应状态码: {resp.status_code}")
            loging.info(f"{item.category}--API响应内容: {resp.text}")
            result_chargecreate = resp.json()
            loging.info(f"{item.category}--API响应成功:{result_chargecreate}")

            #断言
            result_message = result_chargecreate['message']
            expect_message = json.loads(item.expect)['message']
            result_code = result_chargecreate['code']
            expect_code = json.loads(item.expect)['code']
            loging.info(
                f"expect:code-{expect_code},message-{expect_message},result:code-{result_code},message-{result_message}")

            try:
                assert result_message == expect_message
                assert result_code == expect_code
                loging.info(f'{item.category}断言通过')
                chargedata.write_chargedata(sheet='charge', w_row=item.id + 1, actual=str(result_chargecreate),
                                            result='pass')
                loging.info(f"写入{item.category}结果:pass")
            except AssertionError as e:
                loging.error(f'{item.category}断言出错：{e}')
                chargedata.write_chargedata(sheet='charge', w_row=item.id + 1, actual=str(result_chargecreate),
                                            result='fail')
                loging.info(f"写入{item.category}结果：fail")
                raise e


        except Exception as e:
            loging.error(f"{item.category}失败:{e}".format(e))
            loging.error(f"{item.category}详细错误信息: {traceback.format_exc()}")
            raise e  # 抛出异常以便测试失败时能及时发现
        loging.info("__结束：Id:{0}_title:{1}__".format(item.category, item.title))







    @pytest.mark.usefixtures('guest_login')
    @pytest.mark.parametrize('item', case_channelquery)
    @pytest.mark.chargecreate
    def test_channelquery(self, guest_login, item):
        self.guest_dict = guest_login

        # 修复：将item.data从字符串转换为字典后再更新
        item_data = json.loads(item.data) if isinstance(item.data, str) else item.data
        common_data.update(item_data)
        loging.info("__开始执行：Id:{0}_title:{1}__".format(item.category, item.title))

        try:
            newdata = generaterequestdata.get_gps( gps=item.gpsinfo, data_dict=common_data)
            req_channelquery = generaterequestdata.GenerateRequestData(data=newdata, url=item.url, authorize=self.guest_dict["authorization"],
                                                                       method=item.method)
            resp=req_channelquery.reqapi()
            loging.info(f"{item.category}--API响应状态码: {resp.status_code}")
            loging.info(f"{item.category}--API响应内容: {resp.text}")
            result_channelquery = resp.json()
            loging.info(f"{item.category}--API响应成功:{result_channelquery}")

            # 断言
            result_message = result_channelquery['message']
            expect_message = json.loads(item.expect)['message']
            result_code = result_channelquery['code']
            expect_code = json.loads(item.expect)['code']
            loging.info(
                f"expect:code-{expect_code},message-{expect_message},result:code-{result_code},message-{result_message}")

            try:
                assert result_message == expect_message
                assert result_code == expect_code
                loging.info(f'{item.category}断言通过')
                chargedata.write_chargedata(sheet='charge', w_row=item.id + 1, actual=str(result_channelquery),
                                            result='pass')
                loging.info(f"写入{item.category}结果:pass")
            except AssertionError as e:
                loging.error(f'{item.category}断言出错：{e}')
                chargedata.write_chargedata(sheet='charge', w_row=item.id + 1, actual=str(result_channelquery),
                                            result='fail')
                loging.info(f"写入{item.category}结果：fail")
                raise e


        except Exception as e:
            loging.error(f"{item.category}失败:{e}")
            loging.error(f"{item.category}详细错误信息: {traceback.format_exc()}")
            raise e  # 抛出异常以便测试失败时能及时发现
        loging.info("__结束：Id:{0}_title:{1}__".format(item.category, item.title))







    @pytest.mark.usefixtures('guest_login')
    @pytest.mark.parametrize('item', case_chargequery)
    @pytest.mark.chargecreate
    def test_chargequery(self, guest_login, item):
        self.guest_dict = guest_login

        # 修复：将item.data从字符串转换为字典后再更新
        item_data = json.loads(item.data) if isinstance(item.data, str) else item.data
        common_data.update(item_data)
        loging.info("__开始执行：Id:{0}_title:{1}__".format(item.category, item.title))

        try:
            req_chargequery = generaterequestdata.GenerateRequestData(data=common_data, url=item.url, authorize=self.guest_dict["authorization"],
                                                                       method=item.method)
            resp=req_chargequery.reqapi()
            loging.info(f"{item.category}--API响应状态码: {resp.status_code}")
            loging.info(f"{item.category}--API响应内容: {resp.text}")

            result_chargequery = resp.json()
            loging.info(f"{item.category}--API响应成功:{result_chargequery}")

            # 取值
            result_message = result_chargequery['message']
            expect_message = json.loads(item.expect)['message']
            result_code = result_chargequery['code']
            expect_code = json.loads(item.expect)['code']
            loging.info(
                f"expect:code-{expect_code},message-{expect_message},result:code-{result_code},message-{result_message}")


            if expect_code > 0 :
                result_error = result_chargequery['errors']
                expect_error = json.loads(item.expect)['errors']
                loging.info(f"expect:error-{expect_error},result:error-{result_error}")

            # 断言
            try:
                assert result_message == expect_message
                assert result_code == expect_code
                if expect_code > 0 :
                    assert result_error == expect_error

                loging.info(f'{item.category}断言通过')
                chargedata.write_chargedata(sheet='charge', w_row=item.id + 1, actual=str(result_chargequery),
                                            result='pass')
                loging.info(f"写入{item.category}结果:pass")
            except AssertionError as e:
                loging.error(f'{item.category}断言出错：{e}')
                chargedata.write_chargedata(sheet='charge', w_row=item.id + 1, actual=str(result_chargequery),
                                            result='fail')
                loging.info(f"写入{item.category}结果：fail")
                raise e


        except Exception as e:
            loging.error(f"{item.category}失败:{e}")
            loging.error(f"{item.category}详细错误信息: {traceback.format_exc()}")
            raise e  # 抛出异常以便测试失败时能及时发现
        loging.info("__结束：Id:{0}_title:{1}__".format(item.category, item.title))








class TestChargeChannelCreate:
    @pytest.mark.chargecreate
    def test_chargechannelcreate(self, charge_channel,guest_login):
        """按 charge_channel fixture 返回的渠道列表逐个执行创建订单测试。

        说明：不能在装饰器中直接使用 fixture（会在收集阶段被视为函数对象），
        所以在测试运行时从 fixture 获取 channel_list 并迭代执行断言。
        """
        self.channel_dict = charge_channel
        self.guest_dict = guest_login

        # 对每个渠道执行一次请求与断言，遇到异常会直接抛出并使测试失败
        result = {}

        for channel in self.channel_dict["channel_list"]:
            loging.info("开始执行渠道：{0}".format(channel))
            # Excel 中data以字符串形式存储，解析为 dict 再修改
            data_dict = json.loads(case_channelcreatedata.data)

            # 为每个渠道创建common_data的副本，避免数据污染
            channel_data=common_data.copy()
            channel_data.update(data_dict)
            # 修改用例数据中的渠道类型
            channel_data['client_pay_type'] = channel
            # 传入 userid 以便 get_gps 生成 session_id
            try:
                newdata = generaterequestdata.get_gps(gps=case_channelcreatedata.gpsinfo, data_dict=channel_data, userid=self.guest_dict["user_id"])
                req_chargecreate = generaterequestdata.GenerateRequestData(data=newdata, url=case_channelcreatedata.url,
                                                                       authorize=self.guest_dict["authorization"],method=case_channelcreatedata.method)
                resp=req_chargecreate.reqapi()

                loging.info(f"{channel}--API响应状态码: {resp.status_code}")
                loging.info(f"{channel}--API响应内容: {resp.text}")
                result_chargecreate = resp.json()
                loging.info(f"{channel}--API响应成功:{result_chargecreate}")

                query_info = result_chargecreate['data']['query_info']
                loging.info(f"查询订单状态：{query_info}")


                # 断言
                result_message = result_chargecreate['message']
                expect_message = json.loads(case_channelcreatedata.expect)['message']
                result_code = result_chargecreate['code']
                expect_code = json.loads(case_channelcreatedata.expect)['code']
                result_status = result_chargecreate['data']['query_info']['status']
                expect_status = json.loads(case_channelcreatedata.expect)['data']['query_info']['status']




                loging.info(
                    f"expect:code-{expect_code},message-{expect_message},status-{expect_status},result:code-{result_code},message-{result_message},status-{result_status}")

                try:
                    assert result_message == expect_message
                    assert result_code == expect_code
                    assert result_status == expect_status

                    result[channel]="success"

                    loging.info(f"渠道{channel}，创建订单成功")
                except AssertionError as e:
                    # 失败时记录并重新抛出以标记该测试为失败
                    result[channel]="fail"

                    loging.info(f"渠道{channel}，创建订单失败:{e}")
                    raise e
            except Exception as e:
                loging.error(f"{channel}订单-创建失败:{e}")
                loging.error(f"{channel}订单-详细错误信息: {traceback.format_exc()}")
                raise e  # 抛出异常以便测试失败时能及时发现


        if 'fail' in result.values():
            chargedata.write_chargedata(sheet='charge', w_row=case_channelcreatedata.id, actual=str(result),
                                        result='fail')
            loging.info(f'{case_channelcreatedata.category}写入数据：fail')
        elif 'fail' not in result.values():

            chargedata.write_chargedata(sheet='charge', w_row=case_channelcreatedata.id, actual=str(result),
                                        result='pass')
            loging.info(f'{case_channelcreatedata.category}写入数据：pass')
        else:
            chargedata.write_chargedata(sheet='charge', w_row=case_channelcreatedata.id, actual=str(result),
                                        result='nt')
            loging.info(f'{case_channelcreatedata.category}写入数据：nt')




# channelcreatedata 返回一个列表；这里只需要第 12 行的单个用例对象
case_channelcreatedata = chargedata.charge_data('charge', 13, 13)[0]
class TestChargeSuccess_Creditcard:
    @pytest.mark.usefixtures('payment_credit')
    @pytest.mark.parametrize('item', case_cardquery)
    @pytest.mark.smoke
    def test_chargechannelsuccess(self, guest_login,chargecreate,item):
        """这个测试类目前存在问题，先注释掉有错误的测试方法，保留类结构供后续修复"""
        self.guest_dict = guest_login
        self.chargecreate_dict = chargecreate



        # 修复：将item.data从字符串转换为字典后再更新
        item_data = json.loads(item.data) if isinstance(item.data, str) else item.data
        item_data["app_order_id"]=self.chargecreate_dict["app_order_id"]

        common_data.update(item_data)
        loging.info("__开始执行：Id:{0}_title:{1}__".format(item.category, item.title))

        try:
            req_chargequery = generaterequestdata.GenerateRequestData(data=common_data, url=item.url,
                                                                      authorize=self.guest_dict["authorization"],
                                                                      method=item.method)
            resp = req_chargequery.reqapi()
            loging.info(f"{item.category}--API响应状态码: {resp.status_code}")
            loging.info(f"{item.category}--API响应内容: {resp.text}")

            result_chargequery = resp.json()
            loging.info(f"{item.category}--API响应成功:{result_chargequery}")

            # 取值
            result_message = result_chargequery['message']
            expect_message = json.loads(item.expect)['message']
            result_code = result_chargequery['code']
            expect_code = json.loads(item.expect)['code']
            loging.info(
                f"expect:code-{expect_code},message-{expect_message},result:code-{result_code},message-{result_message}")

            # 断言
            try:
                assert result_message == expect_message
                assert result_code == expect_code

                loging.info(f'{item.category}断言通过')
                chargedata.write_chargedata(sheet='charge', w_row=item.id + 1, actual=str(result_chargequery),
                                            result='pass')
                loging.info(f"写入{item.category}结果:pass")
            except AssertionError as e:
                loging.error(f'{item.category}断言出错：{e}')
                chargedata.write_chargedata(sheet='charge', w_row=item.id + 1, actual=str(result_chargequery),
                                            result='fail')
                loging.info(f"写入{item.category}结果：fail")
                raise e


        except Exception as e:
            loging.error(f"{item.category}失败:{e}")
            loging.error(f"{item.category}详细错误信息: {traceback.format_exc()}")
            raise e  # 抛出异常以便测试失败时能及时发现
        loging.info("__结束：Id:{0}_title:{1}__".format(item.category, item.title))









if __name__ == '__main__':
    pytest.main()
