'''
  @Project ：JungleApiTest 
  @File ：conftest.py 
  @Author ：lin20 
  @Date ：2025/10/24 17:25 
  @Describe：
 '''
import time
import pytest
from common import readconfigfile
from common import logconf
from common import route
from common import generaterequestdata
from common import genarate_chargedata
from common import queryms
import requests
import traceback
import json

rconf = readconfigfile.ReadConfig(route.conffile)
loging = logconf.Getlog()
common_data = eval(rconf.get_value('data', 'common_data'))

@pytest.fixture(scope='session', autouse=True)
def guest_login():
    loging.info("-------------{0}开始--------------".format(time.time()))
    guest_dict={}
    
    try:
        # 游客登录
        guest_data=common_data

        req_data= eval(rconf.get_value('data', 'guest_data'))
        guest_data.update(req_data)
        guest_url = "/user/guest"
        req_guest = generaterequestdata.GenerateRequestData(url=guest_url, data=guest_data, method="POST")
        resp = req_guest.reqapi()
        loging.info(f"GUEST-API响应状态码: {resp.status_code}")
        loging.info(f"GUEST-API响应内容: {resp.text}")

        result_guest = resp.json()
        loging.info("GUEST登录成功:{0}".format(result_guest))
    except Exception as e:
        loging.error("GUEST登录失败:{0}".format(e))
        loging.error(f"GUEST详细错误信息: {traceback.format_exc()}")
        raise e  # 抛出异常以便测试失败时能及时发现


        # 验证API响应数据结构
    if result_guest["message"] =="success":
        # 提取用户信息
        guest_dict["user_id"] = result_guest['data']['user']['user_id']  # 用户id
        guest_dict["register_time"] = result_guest['tag']['register_time']  # register_time
        guest_dict["last_login_ip"] = result_guest['data']['user']['last_login_ip']  # last_login_ip

        user_id=guest_dict["user_id"]
        guest_dict["account_id"] = 'bingojungle_' + str(user_id)  # account_id
        
        # 验证嵌套字段
        guest_dict["character_name"] = result_guest['data']['user']['user_info']['name']  # character_name
        guest_dict["level"] = result_guest['data']['user']['level']['level']
        guest_dict["vip_level"] = result_guest['data']['user']['vip']['level']
        guest_dict["email"] = result_guest['data']['user']['account']
        guest_dict["total_game_count"] = result_guest['data']['other']['count']['game_end_count']
        guest_dict["total_win_count"] = result_guest['data']['other']['count']['game_win_count']

        total_win_count = guest_dict["total_win_count"]
        total_game_count = guest_dict["total_game_count"]
        guest_dict["winning_rate"] = round(int(total_win_count) / int(total_game_count), 6) if int(total_game_count) > 0 else 0
        guest_dict["language"] = guest_data['language']
        guest_dict["authorization"] = result_guest['data']['user']['authorization']


        loging.info('guest_login_cache:{0}'.format(guest_dict))

    yield guest_dict
    loging.info("-------------结束--------------")


@pytest.fixture(scope='module')
def charge_channel(guest_login):

    guest_dict = guest_login

    channel_data=common_data
    req_data=eval(rconf.get_value('data', 'channel_data'))
    channel_data.update(req_data)
    channel_url = "/charge_center/channel"
    channel_gps = {"name": "H334+MP7", "thoroughfare": "益州大道中段", "locality": "成都市", "subLocality": "武侯区",
                   "administrativeArea": "四川省", "postalCode": "610212", "ISOcountryCode": "CN", "country": "中国"}


    try:
        # 重新生成带gps的数据
        channel_data = generaterequestdata.get_gps(channel_gps, channel_data)
        # 正确获取authorization
        channel_request = generaterequestdata.GenerateRequestData(url=channel_url, data=channel_data, method="POST", authorize=guest_dict['authorization'])
        resp=channel_request.reqapi()


        # 正确更新channel_list
        loging.info(f"CHANNEL-API响应状态码: {resp.status_code}")
        loging.info(f"CHANNEL-API响应内容: {resp.text}")
        channel_result = resp.json()
        loging.info("查询CHANNEL成功:{0}".format(channel_result))
    except Exception as e:
        loging.error("查询CHANNEL失败:{0}".format(e))

        loging.error(f"CHANNEL详细错误信息: {traceback.format_exc()}")
        raise e  # 抛出异常以便测试失败时能及时发现
    if channel_result["message"] =="success":
        channel_dict={}
        channel_dict["channel_list"] = list(channel_result.get('data', {}).get('channel_info', {}).keys())

    return channel_dict

@pytest.fixture(scope='module')
def configalone(guest_login):
    guest_dict = guest_login
    configalone_data = eval(rconf.get_value('data', 'common_data'))
    configalone_url = "/configs_alone"



    try:

        configalone = generaterequestdata.GenerateRequestData(data=configalone_data, url=configalone_url, method='post',
                                                              authorize=guest_dict["authorization"])
        resp=configalone.reqapi()
        loging.info(f"CONFIG-API响应状态码: {resp.status_code}")
        loging.info(f"CONFIG-API响应内容: {resp.text}")

        configalone_result = resp.json()
        loging.info("查询CONFIG成功:{0}".format(configalone_result))


    except Exception as e:
        loging.error("查询CONFIG失败:{0}".format(e))

        loging.error(f"CONFIG详细错误信息: {traceback.format_exc()}")
        raise e

    if configalone_result["message"] =="success":
        configalone_dict = {}
        # (configalone)payment
        charge_list = configalone_result['data']['charge']['charge_configs']
        configalone_dict["charge_id"] = charge_list[0]['id']

        charge_id=configalone_dict["charge_id"]
        configalone_dict["amount"] = genarate_chargedata.get_chargeamount(charge_list,charge_id)  # game_item_amount  amount
        configalone_dict["payment_charge_id"] = 'bingojungle_' + str(charge_id)  # charge_id
        loging.info("配置数据:{0}".format(configalone_dict))

    return configalone_dict


@pytest.fixture(scope='module')
def chargecreate(configalone, guest_login):
    configalone_dict = configalone
    guest_dict = guest_login

    chargecreate_dict={}
    # 创建订单

    createdata = eval(rconf.get_value('data', 'common_data'))
    req_data = eval(rconf.get_value('data', 'createdata'))
    createdata.update(req_data)
    createdata["charge_id"] = configalone_dict["charge_id"]

    gpsmsg = {"name": "H334+MP7", "thoroughfare": "益州大道中段", "locality": "成都市", "subLocality": "武侯区",
              "administrativeArea": "四川省", "postalCode": "610212", "ISOcountryCode": "CN", "country": "中国"}
    createurl = "/charge_center/create"


    try:
        # create
        setcreatedata = generaterequestdata.get_gps(gpsmsg, createdata)
        create = generaterequestdata.GenerateRequestData(data=setcreatedata, url=createurl, method='post',
                                                         authorize=guest_dict["authorization"])
        resp=create.reqapi()
        loging.info(f"CREATE-API响应状态码: {resp.status_code}")
        loging.info(f"CREATE-API响应内容: {resp.text}")
        create_result = resp.json()
        loging.info("订单CREATE成功:{0}".format(create_result))

    except Exception as e:
        loging.error("订单CREATE失败：{0}".format(e))
        loging.error(f"订单CREATE详细错误信息: {traceback.format_exc()}")
        raise e
    if create_result["message"] =="success":
        chargecreate_dict = {}

        # create:payment
        chargecreate_dict["app_order_id"] = create_result['data']['order_info']['app_order_id']  # app_order_id
        chargecreate_dict["callback_url"] = create_result['data']['order_info']['callback_url']  # callback_url
        chargecreate_dict["charge_center_app_key"] = create_result['data']['order_info'][
            'charge_center_app_key']  # charge_center_app_key
        chargecreate_dict["country"] = create_result['data']['order_info']['country']  # country
        chargecreate_dict["state"] = create_result['data']['order_info']['state']
        chargecreate_dict["white_list"] = create_result['data']['order_info']['white_list']
        loging.info("CREATE数据:{0}".format(chargecreate_dict))
    return chargecreate_dict


@pytest.fixture(scope='module')
def querysql():
    # query SQL data

    try:
        sq = queryms.MSql()
        platform_app_data = sq.fetch_all(
            "SELECT value FROM bingo_jungle.platform_app_configs WHERE `key` in ('charge_center_app_key','charge_center_app_secret','charge_center_client_secret');")
    except Exception as e:
        loging.error("查询platform_app_configs数据失败：{0}".format(e))
        loging.error(f"查询platform_app_configs详细错误信息: {traceback.format_exc()}")
        raise e
    querysql_dict = {}
    querysql_dict["app_key"] = platform_app_data[0][0]  # appkey
    querysql_dict["charge_center_app_secret"] = platform_app_data[1][0]  # 充值中心appsecret
    querysql_dict["charge_center_client_secret"] = platform_app_data[2][0]  # 充值中心clientsecret

    return querysql_dict


@pytest.fixture(scope='module')
def payment_credit(guest_login,configalone,chargecreate,querysql):
    guest_dict = guest_login
    configalone_dict = configalone
    chargecreate_dict = chargecreate
    querysql_dict = querysql

    nonce = genarate_chargedata.generate_readable_string()  # nonce
    timestamp = str(int(time.time()))

    # 使用信用卡支付
    card_paymentdata = {
        "amount": configalone_dict["amount"],
        "app_key": querysql_dict["app_key"],
        "app_order_id": chargecreate_dict["app_order_id"],
        "app_user_id": guest_dict["user_id"],
        "callback_url": chargecreate_dict["callback_url"],
        "card_number": "4200000000000000",
        "charge_center_app_key": chargecreate_dict["charge_center_app_key"],
        "country": chargecreate_dict["country"],
        "currency": "USD",
        "cvc": "566",
        "email": "xhxhfu@gmail.com",
        "extra_params": {
            "user_agent": "Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4 XL Build/TP1A.221005.002.B2)",
            "platform": "Android",
            "app_version": "1.2.0",
            "register_time": guest_dict["register_time"],
            "last_login_ip": guest_dict["last_login_ip"],
            "uuid": "bingojungle_1beceb551bb7acc06ddfb627ab103813",
            "charge_id": configalone_dict["charge_id"],
            "account_id": configalone_dict["payment_charge_id"],
            "character_name": guest_dict["character_name"],
            "player_level": guest_dict["level"],
            "game_name": "bingojungle",
            "game_item_amount": configalone_dict["amount"],
            "mobile_uid": "2c2901b9f3d59cfe121f6a6fc2c3bb1c4594800f0",
            "language": guest_dict["language"],
            "device_brand": "google",
            "device_model": "Pixel 4 XL",
            "region": "四川省",
            "city": "成都市",
            "zip": "610212",
            "past_orders_count": "1",
            "past_orders_amount": "100",
            "vip_level": guest_dict["vip_level"],
            "email": guest_dict["email"],
            "total_game_count": guest_dict["total_game_count"],
            "winning_game_count": guest_dict["total_win_count"],
            "winning_rate": guest_dict["winning_rate"],
            "kyc_status": "0"
        },
        "first_name": "Jguf",
        "last_name": "Ufu",
        "month": "01",
        "nonce": nonce,
        "state": chargecreate_dict["state"],
        "timestamp": timestamp,
        "timezone": "Asia/Shanghai",
        "white_list": chargecreate_dict["white_list"],
        "year": "2026"
    }

    credit_url = ' https://paymentcenter-test.winnerstudio.vip/api/v1/payments/credit_card'

    try:
        api = genarate_chargedata.PaymentParam(card_paymentdata).genaralsignature(
            querysql_dict["charge_center_client_secret"])

        api_response = requests.request(url=credit_url, method="post", data=api)
        credit_result = api_response.json()
        loging.info(f"信用卡支付请求结果：{credit_result}")
    except Exception as e:
        loging.error(f"信用卡支付请求报错：{e}")
        loging.error(f"信用卡支付请求参数：{card_paymentdata}")
        loging.error(f"信用卡支付响应结果：{credit_result}")
    return credit_result
