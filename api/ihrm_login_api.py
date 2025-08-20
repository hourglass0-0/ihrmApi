import requests


class IhrmLoginApi(object):
    @classmethod
    def login(cls, req_data):
        resp = requests.post(url='https://ihrm-java.itheima.net/api/sys/login', json=req_data)
        return resp


if __name__ == '__main__':
    data = {"mobile": "13800000002",
            "password": "929itheima.CN032@.20250816"}
    resp = IhrmLoginApi.login(data)
    print('登录成功：',resp.json())
