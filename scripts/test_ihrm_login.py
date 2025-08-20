from api.ihrm_login_api import IhrmLoginApi
from common.assert_tools import common_asserts
from common.read_json_file import read_json_data
from config import BASE_DIR
import pytest


class TestIhrmLogin(object):
    # 读取json文件
    data = read_json_data(BASE_DIR + "/data/login_data.json")

    @pytest.mark.parametrize("desc,req_data,status_code,success,code,message", data)
    def test_ihrm_login(self, desc, req_data, status_code, success, code, message):
        resp = IhrmLoginApi.login(req_data)
        print(desc, ":", resp.json())
        common_asserts(resp, status_code, success, code, message)


    # # 登录成功
    # def test01_login_success(self):
    #     data = {"mobile": "13800000002",
    #             "password": "929itheima.CN032@.20250814"}
    #     resp = IhrmLoginApi.login(data)
    #     print('登录成功:', resp.json())
    #
    #     common_asserts(resp, 200, True, 10000, '操作成功')
    #
    # # 手机号未注册
    # def test02_mobile_not_register(self):
    #     data = {"mobile": "13800000882",
    #             "password": "929itheima.CN032@.20250814"}
    #     resp = IhrmLoginApi.login(data)
    #     print('手机号未注册:', resp.json())
    #
    #     common_asserts(resp, 200, False, 20001, '用户名或密码错误')
    #
    # # 密码错误
    # def test03_pwd_err(self):
    #     data = {"mobile": "13800000002",
    #             "password": "929itheima.CN032@.20240814"}
    #     resp = IhrmLoginApi.login(data)
    #     print('密码错误:', resp.json())
    #
    #     common_asserts(resp, 200, False, 20001, '用户名或密码错误')
    #
    # def test04_mobile_is_none(self):
    #     data = {"mobile": None,
    #             "password": "929itheima.CN032@.20250814"}
    #     resp = IhrmLoginApi.login(data)
    #     print('手机号为空:', resp.json())
    #
    #     common_asserts(resp, 200, False, 20001, '用户名或密码错误')
    #
    # def test05_mobile_have_special_char(self):
    #     data = {"mobile": "138000ab#02",
    #             "password": "929itheima.CN032@.20250814"}
    #     resp = IhrmLoginApi.login(data)
    #     print('手机号含有特殊字符:', resp.json())
    #
    #     common_asserts(resp, 200, False, 20001, '用户名或密码错误')
    #
    # def test06_10_mobile(self):
    #     data = {"mobile": "1380000002",
    #             "password": "929itheima.CN032@.20250814"}
    #     resp = IhrmLoginApi.login(data)
    #     print('10位手机号:', resp.json())
    #
    #     common_asserts(resp, 200, False, 20001, '用户名或密码错误')
    #
    # def test07_12_mobile(self):
    #     data = {"mobile": "138000000002",
    #             "password": "929itheima.CN032@.20250814"}
    #     resp = IhrmLoginApi.login(data)
    #     print('12位手机号:', resp.json())
    #
    #     common_asserts(resp, 200, False, 20001, '用户名或密码错误')
    #
    # def test08_pwd_none(self):
    #     data = {"mobile": "13800000002",
    #             "password": None}
    #     resp = IhrmLoginApi.login(data)
    #     print('密码为空:', resp.json())
    #
    #     common_asserts(resp, 200, False, 20001, '用户名或密码错误')
    #
    # def test09_pwd_have_special_char(self):
    #     data = {"mobile": "13800000002",
    #             "password": "929itheima.CN032@.20250814#$"}
    #     resp = IhrmLoginApi.login(data)
    #     print('密码含有特殊字符:', resp.json())
    #
    #     common_asserts(resp, 200, False, 20001, '用户名或密码错误')
    #
    # def test10_pwd_1(self):
    #     data = {"mobile": "13800000002",
    #             "password": "1"}
    #     resp = IhrmLoginApi.login(data)
    #     print('密码1位 :', resp.json())
    #
    #     common_asserts(resp, 200, False, 20001, '用户名或密码错误')
    #
    # def test11_pwd_100(self):
    #     data = {"mobile": "13800000002",
    #             "password": "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"}
    #     resp = IhrmLoginApi.login(data)
    #     print('密码100位 :', resp.json())
    #
    #     common_asserts(resp, 200, False, 20001, '用户名或密码错误')
    #
    # def test12_more_params(self):
    #     data = {"mobile": "13800000002",
    #             "password": "929itheima.CN032@.20250814", "abc": "123"}
    #     resp = IhrmLoginApi.login(data)
    #     print('多参:', resp.json())
    #
    #     common_asserts(resp, 200, True, 10000, '操作成功')
    #
    # def test13_less_params(self):
    #     data = {"mobile": "13800000002"}
    #     resp = IhrmLoginApi.login(data)
    #     print('少参-password:', resp.json())
    #
    #     common_asserts(resp, 200, False, 20001, '用户名或密码错误')
    #
    # def test14_none_params(self):
    #     data = None
    #     resp = IhrmLoginApi.login(data)
    #     print('无参:', resp.json())
    #
    #     common_asserts(resp, 200, False, 99999, '抱歉，系统繁忙，请稍后重试！')
    #
    # def test15_err_params(self):
    #     data = {"abc": "13800000002",
    #             "password": "929itheima.CN032@.20250814"}
    #     resp = IhrmLoginApi.login(data)
    #     print('错误参数:', resp.json())
    #
    #     common_asserts(resp, 200, False, 20001, '用户名或密码错误')
    #
