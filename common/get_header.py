from api.ihrm_login_api import IhrmLoginApi

def get_header():
    req_data={"mobile": "13800000002",
            "password": "929itheima.CN032@.20250818"}
    resp=IhrmLoginApi.login(req_data)
    header={"Authorization":resp.json().get("data")}
    return header

if __name__ == '__main__':
    ret=get_header()
    print(ret)
