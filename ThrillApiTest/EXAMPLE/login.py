'''  
  @Project ：ThrillApiTest 
  @File ：login.py 
  @Author ：lin20 
  @Date ：2026/2/24 上午5:51 
  @Describe：游客登录、账号登录、自动登录
 '''
from common import generaterequestdata
from common import route
from common import logconf
from typing import Optional, Dict, Any

req_cache = {"authorization": "", "getoriginaluser": {}, "login_data": {}}



# 默认传参
common_data = {"bundle_id": "com.game.solitairethrill", "carrier_name": "\u65e0\u8fd0\u8425\u5546",
               "client_version": "18", "country_code": "CN", "system_language": "zh-Hans-CN",
               "time_zone": "Asia/Shanghai", "udid": "49C59AD0-457B-4CF0-9429-9C3CB3A91271",
               "version": "44",
               "timestamp": ""}

param_getoriginaluser = {"idfa": "7C40B7D4-5F8C-49C8-9E08-79E6B63B2211"}

param_autologin = {"address": "China;Sichuan", "appsflyer_id": "1770188407693-3080160",
                   "device_info": "iPhone 7(15.2)",
                   "idfa": "7C40B7D4-5F8C-49C8-9E08-79E6B63B2211", "install_vx": "0", "install_zfb": "0",
                   "signature": "da0dda7f246d9f8fcc8aaa685f71eb8a8bd1c400"}

param_guest = {"agree_protocol": 1, "city": "", "country": "China", "head_pic": "103",
               "headpic_box": "",
               "nick_name": "Ailis", "state": "Sichuan",
               "ta_dist_id": "","idfa": "7C40B7D4-5F8C-49C8-9E08-79E6B63B2211","device_info": "iPhone 7(15.2)"}

param_accountlogin = {"address": "", "appsflyer_id": "1771918767270-1937804", "device_info": "iPhone 7(15.2)",
                      "email": "103961@qq.com", "idfa": "7C40B7D4-5F8C-49C8-9E08-79E6B63B2211", "install_vx": "0",
                      "install_zfb": "0", "password": "111111"}


class Login:

    def __init__(self, commonparam=None, getoriginaluser=None, autologin=None, guestlogin=None,accountlogin=None):

        # 1. 初始化实例属性，拷贝全局默认值，避免直接修改
        self.common_data = {**common_data, **(commonparam or {})}
        self.param_getoriginaluser = {**param_getoriginaluser, **(getoriginaluser or {})}
        self.param_autologin = {**param_autologin, **(autologin or {})}
        self.param_guest = {**param_guest, **(guestlogin or {})}
        self.param_accountlogin = {**param_accountlogin, **(accountlogin or {})}
        # 2. 状态缓存作为实例属性
        self.req_cache = {"authorization": "", "getoriginaluser": {}, "login_data": {}}
        self.param_cache = {}
        self.loging = logconf.Getlog()  # 避免全局变量

    def _make_request(self, url_path: str, param: Dict[str, Any], auth_token: Optional[str] = None) -> Any:
        try:
            request_data = {**param, **(self.common_data)}
            req = generaterequestdata.GenerateRequestData(url=url_path, data=request_data, method="POST",
                                                          authorize=auth_token)
            response = req.reqapi()
            resp = response.json()
            self.loging.info(f"{url_path} 请求，状态码: {resp['code']}")
            return resp
        except Exception as e:
            self.loging.error(f"{url_path} 请求失败：{str(e)}")
            return None

    def guestlogin(self) -> Any:
        url_guest = "/api/account/guest_login"
        resp = self._make_request(url_path=url_guest, param=self.param_guest)
        if resp:
            self.loging.info(f"{url_guest}请求成功：响应码: {resp['code']}")
            if resp.get('code') == 0:
                self.req_cache["login_data"].update(resp.get("data", {}))
                self.req_cache['authorization'] = resp['data']['authorization']
            else:
                self.loging.error(f"{url_guest}请求失败：{resp}")
        return resp

    def autologin(self) -> Any:
        url_autologin = "/api/account/autologin"
        resp = self._make_request(url_path=url_autologin, param=self.param_autologin, authorize=self.req_cache["authorization"])
        if resp:
            self.loging.info(f"{url_autologin}请求成功：响应码: {resp['code']}")
            if resp.get("code") == 0:
                self.req_cache["login_data"].update(resp.get('data', {}))
                self.req_cache["login_data"].update(resp.get('tag', {}))
        return self.req_cache

    def accountlogin(self) -> Any:
        url_accountlogin = "/api/account/login"
        resp = self._make_request(url_path=url_accountlogin , param=self.param_accountlogin)
        if resp:
            self.loging.info(f"{url_accountlogin}请求成功：响应码: {resp['code']}")
            if resp.get("code") == 0:
                self.req_cache["login_data"].update(resp.get('data', {}))
                self.req_cache["login_data"].update(resp.get('tag', {}))
                self.req_cache['authorization'] = resp['data']['authorization']
        return self.req_cache

    def getoriginaluser(self) -> Any:
        '''

        :param data: 需要拼接param_getoriginaluser、common_data，其中idfa、udid可修改
        :return:
        '''
        url_getoriginaluser = "/api/account/get_original_user"

        resp = self._make_request(url_path=url_getoriginaluser, param=self.param_getoriginaluser)
        if resp:
            self.loging.info(f'{url_getoriginaluser}请求成功：响应码: {resp["code"]}')
            self.req_cache["getoriginaluser"]["code"] = resp["code"]
            if resp["code"] == 0 :
                self.req_cache["getoriginaluser"].update(resp["data"])

            elif resp["code"] == 1100:
                self.req_cache["authorization"] = ""
                self.req_cache["getoriginaluser"] = {"code": 1100}  # 失败时清空缓存

            else:
                self.loging.error(
                    f"{url_getoriginaluser}请求失败：错误码--{resp.get('code')}，错误提示--{resp.get('data')}")
                self.req_cache["getoriginaluser"] = {"code": resp.get('code')}  # 失败时清空缓存
        else:
            self.loging.error(f"{url_getoriginaluser}请求失败：响应为None")
            self.req_cache["getoriginaluser"] = {"code": None}
        return self.req_cache

    def login_success(self) -> dict:
        self.getoriginaluser()

        code = self.req_cache["getoriginaluser"].get("code")
        data = self.req_cache["getoriginaluser"].get("data")
        token = self.req_cache["authorization"]
        if code == 1100:
            self.loging.info("使用账号密码登录")
            self.accountlogin()
        elif code == 0:
            if not data:
                self.loging.info("使用游客登录")
                self.guestlogin()
            else:
                self.loging.info("自动登录")
                self.loging.info(f"token:{token}")
                self.autologin()
        else:
            self.loging.error(f"获取原始用户失败，code: {code}")
        return self.req_cache

    # req_cache=Login().login_success()


if __name__ == '__main__':
    # logindata
    # user_id=
    a=Login().login_success()
    print(a)