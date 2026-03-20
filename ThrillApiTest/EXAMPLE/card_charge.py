'''
  @Project ：ThrillApiTest 
  @File ：card_charge.py 
  @Author ：lin20 
  @Date ：2026/3/2 上午9:53 
  @Describe：
 '''

common_data = {"bundle_id": "com.game.solitairethrill", "carrier_name": "\u65e0\u8fd0\u8425\u5546",
               "client_version": "18", "country_code": "CN", "system_language": "zh-Hans-CN",
               "time_zone": "Asia/Shanghai", "udid": "49C59AD0-457B-4CF0-9429-9C3CB3A91271",
               "version": "44",
               "timestamp": ""}
login_data = {
    "code": 0,
    "time": 1770794541,
    "message": "success",
    "tag": {
        "language_group": "en",
        "user_id": 104189,
        "index": 344,
        "version": "44",
        "country": "CN",
        "active_date": "20260210",
        "register_time": 1770794539,
        "login_time": 1770794539
    },
    "data": {
        "user_id": 104189,
        "user_code": 256703023,
        "authorization": "104189_N8J1LuotphngN2ZMVlW1WBHpXXxqkgy5KGVwj3W4qwKkxDxFWiT4UwQ6Pb6ZHbTsJUyaE4LqWrhHPMM3ZYuHQ3RYbS9BGuJ6r5sf",
        "date": "20260210",
        "country": "CN",
        "country_code": 86,
        "use_new_guide": true,
        "game_count": 0,
        "ad_chips_daily_count": 0,
        "gps_illegal": false,
        "balance": {"money": 0, "chips": 250, "bonus_money": 0},
        "game_left_num": [
            {"room_id": 30, "num": 5, "total_num": 5},
            {"room_id": 82, "num": 0, "total_num": 5},
            {"room_id": 99, "num": 0, "total_num": 3},
            {"room_id": 70, "num": 0, "total_num": 0},
            {"room_id": 71, "num": 0, "total_num": 0},
            {"room_id": 72, "num": 0, "total_num": 0},
            {"room_id": 73, "num": 0, "total_num": 0},
            {"room_id": 74, "num": 0, "total_num": 0},
            {"room_id": 75, "num": 0, "total_num": 0},
            {"room_id": 76, "num": 0, "total_num": 0},
            {"room_id": 77, "num": 0, "total_num": 0},
            {"room_id": 78, "num": 0, "total_num": 0},
            {"room_id": 79, "num": 0, "total_num": 0},
            {"room_id": 85, "num": 0, "total_num": 0},
            {"room_id": 86, "num": 0, "total_num": 0},
            {"room_id": 87, "num": 0, "total_num": 0},
            {"room_id": 88, "num": 0, "total_num": 0},
            {"room_id": 89, "num": 0, "total_num": 0},
            {"room_id": 90, "num": 0, "total_num": 0},
            {"room_id": 91, "num": 0, "total_num": 0},
            {"room_id": 92, "num": 0, "total_num": 0},
            {"room_id": 93, "num": 0, "total_num": 0},
            {"room_id": 94, "num": 0, "total_num": 0
             }
        ],
        "game_statistics": {
            "total": {"game_count": 0, "win_cash": 0, "fastest_time": 0, "clear_rate": 0},
            "statistics": [
                {"category": 1, "game_count": 0, "win_cash": 0, "clear_rate": 0, "fastest_time": 0},
                {"category": 4, "game_count": 0, "win_cash": 0, "clear_rate": 0, "fastest_time": 0},
                {"category": 3, "game_count": 0, "win_cash": 0, "clear_rate": 0, "fastest_time": 0},
                {"category": 5, "game_count": 0, "win_cash": 0, "clear_rate": 0, "fastest_time": 0},
                {"category": 7, "game_count": 0, "win_cash": 0, "clear_rate": 0, "fastest_time": 0},
                {"category": 6, "game_count": 0, "win_cash": 0, "clear_rate": 0, "fastest_time": 0},
                {"category": 8, "game_count": 0, "win_cash": 0, "clear_rate": 0, "fastest_time": 0},
                {"category": 9, "game_count": 0, "win_cash": 0, "clear_rate": 0, "fastest_time": 0}
            ]
        },

"match_task": {
    "open": true,
    "tasks": [
        {"index": 1, "room_id": 6, "conf_ids": [6], "task_count": 3, "prizes": {"bonus_money": 2}, "conf_id": 6,
         "finished_count": 0, "is_finished": false, "is_claimed": false},
        {"index": 2, "room_id": 7, "conf_ids": [7, 507], "task_count": 3, "prizes": {"bonus_money": 3.5}, "conf_id": 7,
         "finished_count": 0, "is_finished": false, "is_claimed": false},
        {"index": 3, "room_id": 8, "conf_ids": [8, 508], "task_count": 3, "prizes": {"bonus_money": 5.5}, "conf_id": 8,
         "finished_count": 0, "is_finished": false, "is_claimed": false},
        {"index": 4, "room_id": 9, "conf_ids": [9, 509], "task_count": 3, "prizes": {"bonus_money": 10}, "conf_id": 9,
         "finished_count": 0, "is_finished": false, "is_claimed": false}]},
"more_bonus": {
    "open": true,
    "remained_time": 2259,
    "bonus_percent": 100,
    "gift_configs": [
        {"amount": 5, "gift": 5, "rate": "100%"},
        {"amount": 15, "gift": 15, "rate": "100%"},
        {"amount": 25, "gift": 25, "rate": "100%"},
        {"amount": 35, "gift": 35, "rate": "100%"},
        {"amount": 50, "gift": 50, "rate": "100%"},
        {"amount": 100, "gift": 100, "rate": "100%"},
        {"amount": 200, "gift": 200, "rate": "100%"},
        {"amount": 500, "gift": 500, "rate": "100%"}
    ],
    "pop_up": false
},
"push_open": {"open": true, "claimed": false, "prizes": {"bonus_money": 0.5}, "show_icon": false},
"register_reward": {"rewards": {"chips": 20}},
"room_ids": [30052, 30051, 30050, 30009, 30347, 30008, 30350, 30007, 30006, 30004, 30002, 30021],
"second_charge": {
    "charge_1": {"id": 0, "chance": 0, "remained_time": 0},
    "charge_2": {"id": 0, "chance": 0, "remained_time": 0, "show_time": 0}
},
"store_ad": {
    "open": true,
    "chips_ad": {"open": true, "remained_time": 0, "daily_limit_count": 5, "daily_claimed_count": 0,
                 "next_prize": {"chips": 10}, "free": true},
    "bonus_ad": {"open": false, "remained_time": 0, "daily_limit_count": 5, "daily_claimed_count": 0,
                 "next_prize": null, "free": false},
},
"sumsub_status": {"status": -1, "chips": 50},
"user_info": {
    "id": 104189,
    "nick_name": "Ailis",
    "head_pic": "https:\/\/bg21.s3.us-east-2.amazonaws.com\/star\/head_pic_9.png",
    "birthday": null
},
"user_tags": {
    "max_game_level": "299",
    "is_organic": -1,
    "game_count": 1,
    "charge_total": 0,
    "game_max_money": 0,
    "refresh_remained_time": 2271,
    "guide_step": 0,
    "hyper_email": null,
    "user_create_time": 1770794538,
    "login_record_id": 602000000559,
    "game_tips": true,
    "last_charge_time": 0,
    "applepay_direct_charge": false,
    "is_white_user": false,
    "free_game_tips": true,
    "charge_discount_open": false,
    "show_laundering": true,
    "anti_money_laundering": "1500",
    "paypal_valid": false,
    "upload_fb_event": false,
    "inorganic_need_location": false,
    "is_open_new_guide": true,
    "new_guide_step": 0,
    "oragnic_tongdun_fake_location": false,
    "game_tags": [4],
    "default_game_tag": 4,
    "level_show_new_game_tag": 6,
    "open_guide1_move": false,
    "user_guide_steps_reduce": false,
    "use_pay_center": true,
    "game_guide_group": "B",
    "has_agree_protocol": true,
    "push_notification_group": "A",
    "pop_register_reward_group": "B",
    "rolling_ratio_rooms": [

    ]
},
"user_xp": {"xp": 0, "level": 1, "prize_level": "0"},
"vip_system": {"open": true, "vip": {"score": 0, "level": "0", "nameplate": 0, "avatar_frame": 0, "level_up": false},
               "ad_config": {"remain_num": 10, "remain_time": 2260, "ad_score": 5}, "prizes": {}, "charged": []},
"wait_charge_unlock": [
    {"activity_name": "festival", "wait_charge_unlock": true, "unlock_charge_id": 900},
    {"activity_name": "festival_spring", "wait_charge_unlock": true, "unlock_charge_id": 900},
    {"activity_name": "plinko", "wait_charge_unlock": true, "unlock_charge_id": 900},
    {"activity_name": "new_user_gifts", "wait_charge_unlock": true, "unlock_charge_id": 900},
    {"activity_name": "pairs_tour", "wait_charge_unlock": true, "unlock_charge_id": 900},
    {"activity_name": "poker_master", "wait_charge_unlock": true, "unlock_charge_id": 900},
    {"activity_name": "spin_for_lucky", "wait_charge_unlock": true, "unlock_charge_id": 900},
    {"activity_name": "slot_bingo", "wait_charge_unlock": true, "unlock_charge_id": 900},
    {"activity_name": "multiple_disks", "wait_charge_unlock": true, "unlock_charge_id": 900},
    {"activity_name": "baking_cakes", "wait_charge_unlock": true, "unlock_charge_id": 900},
    {"activity_name": "globetrotter_quest", "wait_charge_unlock": true, "unlock_charge_id": 900}
],
"welcome_recharge": {"open": true, "remained_time": 598, "charge_id": 11850},
"day_end_timestamp": 1770796800
}
}

# api/user/verify_gps
#    {"code":0,"time":1771904539,"message":"success","data":{}}
param_verify_gps = {"city": "", "country": "China",
                    "gps_info": '{"country":"China","ISOcountryCode":"CN","administrativeArea":"Sichuan","longitude":"104.0570063335558","latitude":"30.55461243780987","thoroughfare":"Jiqing 1st Road","name":"Jiqing 1st Road"}',
                    "state": "Sichuan"}

# api/charge/get_methods
#    {"code":0,"time":1771904540,"message":"success","data":[{"id":1,"name":"credit_card","show_name":"Credit Card","method":"credit_card","config":{"discount":5},"condition":null,"icon_url":"https:\/\/bg21.s3.us-east-2.amazonaws.com\/star\/credit_card_icon.png","open":"1","sort":"0","created_at":"2021-04-01 00:00:00","updated_at":"2024-06-12 05:07:47"},{"id":2,"name":"paypal","show_name":"Paypal","method":"simple","config":{"discount":5},"condition":null,"icon_url":"https:\/\/bg21.s3.us-east-2.amazonaws.com\/star\/paypal_icon.png","open":"1","sort":"0","created_at":"2021-04-01 00:00:00","updated_at":"2023-09-27 05:27:55"},{"id":4,"name":"apple_pay","show_name":"Apple Pay","method":"simple","config":{"max_amount":10000},"condition":null,"icon_url":"https:\/\/bg21.s3.us-east-2.amazonaws.com\/star\/apple_pay_icon.png","open":"1","sort":"0","created_at":"2023-02-17 09:20:49","updated_at":"2023-08-04 10:26:41"}]}

param_charge_method = {"Authorization": ""}

# api/charge/create
param_charge_create  ={
    "bundle_id": "com.game.solitairethrill",
    "card_number": "NDIwMDAwMDAwMDAwMDAwMA==",
    "carrier_name": "\u65e0\u8fd0\u8425\u5546",
    "charge_id": "201",
    "client_version": "18",
    "country_code": "CN",
    "name": "credit_card",
    "session_id": "1041891771904537",
    "signature": "7b8dba39d0f9df02a9a3eb91a01b0200ab24ac89",
    "system_language": "zh-Hans-CN",
    "time_zone": "Asia/Shanghai",
    "timestamp": 1771904582,
    "udid": "49C59AD0-457B-4CF0-9429-9C3CB3A91278",
    "version": "44"
}
resp_charge_create={
    "code": 0,
    "time": 1771904584,
    "message": "success",
    "notification": [
        {
            "name": "aft_info",
            "value": {
                "open": true,
                "rewards": {
                    "bonus_money": 1
                }
            }
        }
    ],
    "data": {
        "amount": "10.00",
        "charge_id": "201",
        "order_id": "pay_center_6687",
        "app_order_id": "20260224-034303-46771918-104189",
        "callback_url": "http:\/\/bfc-solitaire-ios.luckfun.vip\/api\/callback\/paycenter",
        "extra_key": {
            "currency": "USD",
            "country": "US",
            "state": "",
            "app_data": {
                "user_id": 104189,
                "desc": "Deposit for 10.00",
                "app_name": "Solitaire Thrill",
                "support_wait_form": 1
            },
            "app_remark": ""
        },
        "billing_address": {

        },
        "step": "pay_center",
        "riskCnt": {
            "province": "",
            "region": "US",
            "city": "",
            "zip": "",
            "register_time": 1770794538,
            "past_orders_count": 0,
            "past_orders_amount": 0,
            "last_login_ip": "149.52.96.24",
            "register_ip": "149.52.96.24",
            "email": null
        }
    }
}






app_data = {"user_id": login_data['data']['user_id'], "desc": "Deposit for 10.00", "app_name": common_data["bundle_id"],
            "support_wait_form": 1}

charge_id="solitairethrill_"+
extra_params = {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "platform": "ios",
        "app_vesion": "1.1.1",
        "device_brand": "iPhone",
        "device_model": "iPhone 7(15.2)",
        "uuid": udid,
        "charge_id": "solitairethrill_201",
        "account_id": account_id,
        "character_name": login_data['data']['user_info']['nick_name'],
        "player_level": login_data['data']['user_xp']['level'],
        "game_name": "solitairethrill",
        "game_item_amount": ,
        "mobile_uid": "D3080F16-F03D-4285-90D9-081615E5D39B",
        "bundle_name": common_data["bundle_id"],
        "client_ips": "149.52.96.24",
        "language": common_data["system_language""],
        "province": "",
        "region": "US",
        "city": "",
        "zip": "",
        "register_time": login_data['data']['user_info']['register_time'],
        "past_orders_count": resp_charge_create['data']['risk_cnt']['past_orders_count'],
        "past_orders_amount": resp_charge_create['data']['risk_cnt']['past_orders_amount'],
        "last_login_ip": resp_charge_create['data']['last_login_ip'],
        "register_ip": resp_charge_create['data']['register_ip'],
        }


billing_address = {"first_name": "Ggg", "last_name": "Hhh", "email": "Gucy@gmail.com"}
card_info = {"card_number": "4200000000000000", "email": "Gucy@gmail.com", "cvc": "555", "year": "2027", "month": "04",
             "first_name": "Ggg", "last_name": "Hhh"}
import time

time_stamp = str(int(time.time()))

uuid = "solitairethrill_" + common_data["udid"]
account_id = "solitairethrill_" + login_data['data']['user_id']

param_card_payment = {
    "app_order_id": "20260224-034303-46771918-104189",
    "callback_url": "http://bfc-solitaire-ios.luckfun.vip/api/callback/paycenter",
    "currency": "USD",
    "country": "US",
    "state": "",
    "app_data": str(app_data),
    "app_remark": "",
    "extra_params": extra_params,
    "billing_address": billing_address,
    "card_number": card_info['card_number'],
    "email": card_info['email'],
    "cvc": card_info['cvc'],
    "year": card_info['year'],
    "month": card_info['month'],
    "first_name": card_info['first_name'],
    "last_name": card_info['last_name'],
    "amount": "10",
    "nonce": "hGXyRb",
    "timestamp": time_stamp,
    "app_user_id": login_data['data']['user_id'],
    "app_key": "H5yOEN2mYC4MMEcg",
    "signature": "cc323f08260f305966e97cb4e0832c37"
}







class CardCharge:
    def __init__(self):
        pass

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

    def verify_gps(self):
        url = "/api/user/verify_gps "

        pass

    def charge_methods(self):
        url = "/api/user/charge_methods "
        pass

    def charge_create(self):
        url = "/api/user/charge_create "
        pass

    def card_charge(self):
        url = "https://paymentcenter-test.winnerstudio.vip/api/v1/payments/credit_card"
        pass
