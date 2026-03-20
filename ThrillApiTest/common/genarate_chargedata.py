'''
  @Project ：JungleApiTest 
  @File ：genarate_chargedata.py
  @Author ：lin20 
  @Date ：2025/12/1 10:37 
  @Describe：生成支付中心数据
 '''
import re
import json
import base64
import hashlib
import random
import log
from urllib.parse import urlencode

class PaymentParam:
    def __init__(self,param):
        self.param=param
    def transform(self,value):
        """
        清理字符串首尾的特定空白字符，包括BOM和零宽空格。
        参数:
            value: 待处理的字符串
        返回:
            清理后的新字符串
        """
        # 修正正则表达式模式，使用 \u 前缀表示 Unicode 字符
        pattern = r'^[\s\uFEFF\u200B]+|[\s\uFEFF\u200B]+$'
        # re.sub() 若无匹配会返回原字符串，无需判断 None
        transformed_value = re.sub(pattern, '', value, flags=re.UNICODE)
        return transformed_value # 直接返回替换结果
    def striplist(self):
        escaped_dict = {}
        for key, value in self.param.items():
            if isinstance(value, str):
                escaped_value = self.transform(value)
                escaped_dict[key] = escaped_value
            elif isinstance(value, (list, dict)):
                for key, value in value.items():
                    # 使用json.dumps自动处理转义，然后去掉外层引号
                    escaped_value = json.dumps(value)[1:-1]
                escaped_dict[key] = escaped_value
            else:
                escaped_dict[key] = value
        return escaped_dict

    def genaralsignature(self,secret):


        self.sign_dict = {}  # 请求数据生成字典
        sign_str = ""  # 生成签名
        self.sr=""
        data2 = sorted(self.striplist().items(), key=lambda x: x[0], reverse=False)  # 按字典序排序
        for i, (key, value) in enumerate(data2):
            if isinstance(value, (list, dict)):
                value = json.dumps(value)
            self.sign_dict[key] = value

            encoded_key = base64.b64encode(str(key).encode('utf-8')).decode('utf-8')
            encoded_value = base64.b64encode(str(value).encode('utf-8')).decode('utf-8')
            encoded_str=encoded_key + encoded_value

            sign_str += encoded_str  # 这里添加了等号
            sign_str += "&"

        sign_str += secret
        self.sr+=secret
        signature = hashlib.md5(sign_str.encode()).hexdigest().lower()
        self.sign_dict['signature'] = signature

        return self.sign_dict

def safe_get(dictionary, *keys, default=None):
    """
    安全地获取嵌套字典中的值
    :param dictionary: 原始字典
    :param keys: 一系列的键
    :param default: 如果任何一层访问失败，返回的默认值
    :return: 获取到的值或默认值
    """
    current = dictionary
    for key in keys:
        try:
            current = current[key]
        except (TypeError, KeyError):
            return default
    return current

def get_chargeamount(json_string, target_id):
    '''

    :param json_string: 创建订单的返回数据
    :param target_id: 充值id
    :return:充值金额
    '''
    try:
        for i in range(0,len(json_string)):
            if int(json_string[i]['id'])==int(target_id):
                return json_string[i]['amount']
        # return None
    except json.JSONDecodeError:
        ("JSON格式错误")
        return None
    except KeyError as e:
        print(f"缺少必要的键: {e}")
        return None




def generate_readable_string(min_len=6, max_len=16):
    # 去除了容易混淆的字符，如数字'0'，字母'O','o','l','I'等
    readable_chars = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789'
    length = random.randint(min_len, max_len)
    return ''.join(random.choices(readable_chars, k=length))


