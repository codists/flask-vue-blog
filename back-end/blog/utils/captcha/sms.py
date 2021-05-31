# @Date: 2021/5/24
# @Author: Hugh
# @Email: 609799548@qq.com

import os
import threading

from qcloudsms_py import SmsSingleSender

from ...utils.cache import cache


APPID = 1400304164  # SDK AppID 以1400开头
# 短信应用 SDK AppKey
APPKEY = os.getenv('sms_key')
# 短信模板ID，需要在短信控制台中申请
TEMPLATE_ID = 519595  # NOTE: 这里的模板 ID`7839`只是示例，真实的模板 ID 需要在短信控制台中申请
# 签名
SMS_SIGN = "丘家劲个人日常学习记录"  # NOTE: 签名参数使用的是`签名内容`，而不是`签名ID`。这里的签名"腾讯云"只是示例，真实的签名需要在短信控制台中申请

sender = SmsSingleSender(APPID, APPKEY)


class SendSms:

    @classmethod
    def send(cls, mobile, random_number):
        t = threading.Thread(target=cls._send, args=(mobile, random_number))
        t.start()


    @staticmethod
    def _send(mobile, random_number):
        try:
            response = sender.send_with_param(86, mobile, TEMPLATE_ID, (random_number,), sign=SMS_SIGN, extend="", ext="")
        except TypeError as e:
            pass
        except Exception as e:
            print('sms error: %s' % e)
            return False
        if response and response['result'] == 0:
            print('%s 发送的短信验证码是:' % mobile, random_number)
            cache.set(mobile, random_number)
            return True
        print('sms error:%s' % response['errmsg'])
        return False

