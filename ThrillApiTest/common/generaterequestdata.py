'''
  @Project ：JungleApiTest 
  @File ：generaterequestdata.py
  @Author ：lin20 
  @Date ：2025/9/22 11:51 
  @Describe：封装-request请求、token加密、gps解析、账号密码加密
 '''
import hashlib
import requests
import time
# Support running as package or as a standalone script in the common directory
try:
    # when imported as package
    from . import route
    from . import readconfigfile
except Exception:
    # when executed directly from the common/ directory
    import route
    import readconfigfile

rconf = readconfigfile.ReadConfig(route.conffile)
class GenerateRequestData:

    def __init__(self, data, url, method, authorize=None):
        '''

        :param data: json数据
        :param authorize: token值
        '''
        self.data = dict(data)
        self.authorize = authorize
        self.url = url
        self.method = method

    def sortjson(self):
        if 'timestamp' in self.data and self.data['timestamp']=='':
            self.data['timestamp'] = str(int(time.time()))

        data2 = sorted(self.data.items(), key=lambda x: x[0], reverse=False)  # 按字典序排序
        s = ""
        data3 = {}
        for i in range(0, len(data2)):
            if i < len(data2) - 1:
                s = s + str(data2[i][0]) + "=" + str(data2[i][1]) + "&"
            else:
                s = s + str(data2[i][0]) + "=" + str(data2[i][1])  # 排序后的字符串

            data3[data2[i][0]] = data2[i][1]  # 排序后的请求参数
        # print(data3)
        # print(s)
        return [data3, s]

    def getsign(self):
        auth_key = "e5FQ94A5f2N38ae563490U8523b7e0DS"#THRILL

        if self.authorize is None:
            self.authorize = ""
        splicstr = self.authorize + self.sortjson()[1] + auth_key  # 数据拼接
        encrypted = hashlib.sha1(splicstr.encode("utf-8")).hexdigest()  # 加密
        reqdata = self.sortjson()[0]
        reqdata["signature"] = encrypted  # 请求参数增加签名
        # print(reqdata)
        return reqdata

    def header(self):
        self.header = {'Authorization': ""}
        if self.authorize is None:
            return self.header
        else:
            self.header['Authorization'] = self.authorize  # 请求头新增token
            return self.header

    def reqapi(self):
        # req = requests.session()
        method = (self.method or '').lower()
        self.url = rconf.get_value('api', 'pre_url') + self.url
        print(self.url)
        try:
            if method == 'get':
                resp = requests.get(url=self.url, headers=self.header(), params=self.getsign())
            elif method == 'post':
                resp = requests.post(self.url, headers=self.header(), json=self.getsign())
            elif method == 'put':
                resp = requests.put(self.url, headers=self.header(), json=self.getsign())
            elif method == 'delete':
                resp = requests.delete(self.url, headers=self.header(), json=self.getsign())
            else:
                raise ValueError(f"Unsupported HTTP method: {self.method}")
        except requests.RequestException as e:
            # raise a clearer runtime error for the caller to handle
            raise RuntimeError(f"HTTP request failed: {e}")

        return resp








def sp_pwd(pwd, email, data_dict):
    '''

    :param pwd: 明文密码
    :param email: 已存在的邮箱地址
    :param data_dict: 请求通用数据，字典
    :return:接口请求数据
    '''
    password = email + pwd
    sp_pwd = hashlib.sha1(password.encode("utf-8")).hexdigest()
    data_dict['password'] = sp_pwd
    data_dict['email'] = email
    return data_dict


def get_gps(gps, data_dict,userid=None):
    '''

    :param userid: 用户id，从登录数据中['data']['user']['user_id']中取
    :param gps: 字典，定位信息 {"name": "H334+MP7", "thoroughfare": "益州大道中段", "locality": "成都市", "subLocality": "武侯区", "administrativeArea": "四川省", "postalCode": "610212", "ISOcountryCode": "CN", "country": "中国"}
    :param data_dict: 请求通用数据，字典
    :return:接口请求数据
    '''

    import time
    import base64
    import json
    if isinstance(data_dict, str):
        data_dict=json.loads(data_dict)
    if isinstance(gps, str):
        gps = json.loads(gps)

    gps_info = base64.b64encode(str(gps).encode()).decode()
    data_dict['gps'] = gps_info

    if userid is not None:
        sessionid = str(userid) + "_" + str(int(time.time()))
        data_dict['session_id'] = sessionid
    return data_dict

if __name__ == '__main__':

    url="https://supportcenter-test.winnerstudio.vip/api/v1/test/index"
    #游客登录
    guestdata={
        "udid": "BRGP_1beceb551bb7acc06ddfb627ab103813",
        "version": "66",
        "bundle_id": "com.bingo.skill.free.win.battle.gp",
        "timestamp": "",
        "gps": "eyJuYW1lIjoiSDMzNCtNUDciLCJ0aG9yb3VnaGZhcmUiOiLnm4rlt57lpKfpgZPkuK3mrrUiLCJsb2NhbGl0eSI6IuaIkOmDveW4giIsInN1YkxvY2FsaXR5Ijoi5q2m5L6v5Yy6IiwiYWRtaW5pc3RyYXRpdmVBcmVhIjoi5Zub5bed55yBIiwicG9zdGFsQ29kZSI6IjYxMDIxMiIsIklTT2NvdW50cnlDb2RlIjoiQ04iLCJjb3VudHJ5Ijoi5Lit5Zu9In0=",
        "gps_address": "30.5544878,104.056959",
        "last_login_noplay": "1",
        "timezone": "Asia/Shanghai",
        "language": "zh",
        "device_info": "{'name':'<unknown>','os':'Android OS 13 / API-33 (TP1A.221005.002.B2/9382335)'}",
        "distinct_id": "1615e934-50e9-4598-8fdf-db30b1e663df",
        "appsflyer_id": "NONE",
        "is_organic": "0",
    }
    guesturl='/user/guest'
    #login
    guest=GenerateRequestData(data=guestdata,url=guesturl,method='post')
    guest_result = guest.reqapi().json()

    syn=guest_result['data']['user']['authorization']
