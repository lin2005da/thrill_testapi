'''
  @Project ：JungleApiTest 
  @File ：1.py 
  @Author ：lin20 
  @Date ：2025/10/27 15:25 
  @Describe：
 '''
import time

# import random
#
# # 生成一个随机的6位数字
# x=[]
# for i in range(100):
#     print('第{0}轮'.format(i))
#     random_number = random.randint(10, 99)
#     if random_number in x:
#         print('重复数字:{0}'.format(random_number))
#     else:
#         x.append(random_number)
#         print('新增数字：{0}'.format(random_number))
#
# print(x)


# import configparser
# from common import route
#
# # 创建配置解析器对象
# config = configparser.ConfigParser()
#
# # 添加一个section
# config.add_section('Settings')
# config.
# # 设置参数
# config.set('Settings', 'param1', 'value4')
#
#
# # 写入文件
# with open(route.existfile, 'a+') as configfile:
#     config.write(configfile)

#
# a={
#     "code": 0,
#     "time": 1670920695,
#     "message": "success",
#     "io_log": [
#         "enter io function ChargeCenterService#queryChannelByUserID",
#         "   add return channel_info",
#         "   check conditions",
#         "   init log param",
#         "      log_param:[]",
#         "   init in items:[]",
#         "   check in items:[]",
#         "   init out items:[]",
#         "   begin add items []",
#         "      begin transaction",
#         "         exec cache",
#         "   init returns:[]",
#         "   exec cache"
#     ],
#     "data": {
#         "channel_info": {
#             "credit_card": [
#                 "rapyd_credit_api"
#             ],
#             "paypal": [
#                 "paypal_wallet_slave"
#             ]
#         }
#     }
# }
#
# s=list(a['data']['channel_info'].keys())
# print(s[0])

#
# # 解码
# import base64
# import gzip
# import json
#
#
# # 您提供的编码字符串（示例）
# # encoded_str = "H4sIAAAAAAAAE+1Su27DMAz8F2X1YMvvrNag3WMRGIaitkL9CGw3S5B\/r49U7DZAx25dTuLxeKZI38R4sYMb3hrTTudZHG9iXkbz0VxcZ8XxRahcBKJOV9AlIEMYr6DA1ZEkDAmRp6vGVUGqIlwrqicninUBSBADFJwVmVJInpk4BcKM3Wc\/RGhER\/HOSDB1fsDHqnLnY\/BVFHNC0qGKPZ9wPqSETg\/cN8truetS0iVc\/7DLfci2en3Jps9IX3gB21cZ2zJbeZPvVTm9ovRV3tW7s1xLX+WPR4udNYsbaTA\/CPlMxM8EJnC6B1j71IKYWfHqhrb75Sf4X8QfLqI1785eLYa+7aSZzTitVBiIxfV2C1f5ZPvWDfbcIAHqC6vIBcfCAwAA"
# # {"opening_cards": {"stock_pile": ["D7", "S5", "H9", "H6", "S3", "D5", "S12", "S10", "S1", "H10", "H1", "D6", "D11", "C5", "H7", "S11", "H8", "H4", "S4", "D9", "D3", "D4", "D2", "S6"], "column1": ["H13"], "column2": ["S7#0", "C9"], "column3": ["C13#0", "C2#0", "D8"], "column4": ["C10#0", "H5#0", "S13#0", "S2"], "column5": ["C4#0", "D13#0", "C7#0", "D12#0", "H11"], "column6": ["C8#0", "D10#0", "C6#0", "S8#0", "C3#0", "C11"], "column7": ["S9#0", "D1#0", "H12#0", "H3#0", "H2#0", "C1#0", "C12"], "collection1": [], "collection2": [], "collection3": [], "collection4": []}, "operations": [], "final_cards": {"stock_pile": [], "column1": ["H13"], "column2": ["S7#0", "C9"], "column3": ["C13#0", "C2#0", "D8"], "column4": ["C10#0", "H5#0", "S13#0", "S2"], "column5": ["C4#0", "D13#0", "C7#0", "D12#0", "H11"], "column6": ["C8#0", "D10#0", "C6#0", "S8#0", "C3#0", "C11"], "column7": ["S9#0", "D1#0", "H12#0", "H3#0", "H2#0", "C1#0", "C12"], "collection1": [], "collection2": [], "collection3": [], "collection4": []}, "achieve": {"operation_score": 0, "time_score": 0}, "remained_time": 0}
# encoded_str = "H4sIAAAAAAAAE6tWSkosTo0vSi1PLEopVrIy0FFKzkjMyUnNS0cVLU7NSU0uyczPU7IyrAUAk+AB2TYAAAA="
#
# # 1. Base64解码
# decoded_bytes = base64.b64decode(encoded_str)
# # 2. GZIP解压
# decompressed_bytes = gzip.decompress(decoded_bytes)
# # 3. 反序列化（假设是JSON）
# original_data = json.loads(decompressed_bytes.decode('utf-8'))
#
# print(original_data)
#
# # 加密
# import json
# import gzip
# import base64
#
# # 您的原始数据
# original_data = {'base_rewards': 0, 'challenge_rewards': 0, 'selection': 1}
# # 1. JSON序列化
# json_str = json.dumps(original_data)
#
# # 2. GZIP压缩
# # 注意：这里将字符串编码为bytes再进行压缩
# compressed_bytes = gzip.compress(json_str.encode('utf-8'))
#
# # 3. Base64编码
# base64_str = base64.b64encode(compressed_bytes).decode('ascii')
#
# print(base64_str)
# # 输出应与您提供的字符串一致


# import base64, gzip, json
# str_a = "H4sIAAAAAAAAE6tWSkosTo0vSi1PLEopVrIy0FFKzkjMyUnNS0cVLU7NSU0uyczPU7IyrAUAk+AB2TYAAAA="
# str_b = "H4sIAEaRjmkC/6tWSkosTo0vSi1PLEopVrJSMNBRUErOSMzJSc1LRxcvTs1JTS7JzM8D8g1rAcB4KAs7AAAA"

# def decode_str(s):
#     decoded = base64.b64decode(s)
#     decompressed = gzip.decompress(decoded)
#     # 假设是JSON数据
#     return json.loads(decompressed.decode('utf-8'))

# data_a = decode_str(str_a)
# data_b = decode_str(str_b)
# print("Data A:", type(data_a),data_a)
# print("Data B:", type(data_b),data_b)
# # 比较两者差异

