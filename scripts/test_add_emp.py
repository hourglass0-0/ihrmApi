from common.assert_tools import common_asserts
from api.ihrm_emp_api import IhrmEmpApi
# from common.db_tools import DBTools
from config import TEL
from common.get_header import get_header


# 定义测试类
class TestAddEmp(object):
    req_header = None

    def setup_class(self):
        self.req_header = get_header()

    # def setup_method(self):
    #     # del_sql = "delete from bs_user where mobile='13500001111';"
    #     del_sql = f"delete from bs_user where mobile='{TEL}';"
    #     DBTools.db_uid(del_sql)
    #
    # def teardown_method(self):
    #     del_sql = "delete from bs_user where mobile='13500001111';"
    #     DBTools.db_uid(del_sql)
    # 定义测试方法 - 添加成功
    def test01_add_ok(self):
        # 调用自己封装的 api，发送 添加员工请求
        # req_header = {"Authorization": "3e85e548-cdfb-4442-8e74-da5e05a7330c"}
        req_data = {
            "username": "user87655430",
            "mobile": "13500121111",
            "workNumber": "9527890aa"
        }
        resp = IhrmEmpApi.add_emp(self.req_header, req_data)
        print("必选-添加成功：", resp.json())
        # 断言
        common_asserts(resp, 200, True, 10000, "操作成功")

    def test02_add_ok_all(self):
        # 调用自己封装的 api，发送 添加员工请求
        # req_header = {"Authorization": "3e85e548-cdfb-4442-8e74-da5e05a7330c"}
        req_data = {
            "username": "齐天小圣朱小姐001",
            "mobile": "13500541111",
            "timeOfEntry": "2022-02-01",
            "formOfEmployment": 1,
            "workNumber": "9009",
            "departmentName": "研发部",
            "departmentId": "1480198742740082688",
            "correctionTime": "2022-02-27T16:00:00.000Z"
        }
        resp = IhrmEmpApi.add_emp(self.req_header, req_data)
        print("全部-添加成功：", resp.json())
        # 断言
        common_asserts(resp, 200, True, 10000, "操作成功")

    def test03_username_None(self):
        # 调用自己封装的 api，发送 添加员工请求
        # req_header = {"Authorization": "3e85e548-cdfb-4442-8e74-da5e05a7330c"}
        req_data = {
            "username": None,
            "mobile": "13505001111",
            "timeOfEntry": "2022-02-01",
            "formOfEmployment": 1,
            "workNumber": "9009",
            "departmentName": "研发部",
            "departmentId": "1480198742740082688",
            "correctionTime": "2022-02-27T16:00:00.000Z"
        }
        resp = IhrmEmpApi.add_emp(self.req_header, req_data)
        print("用户名为空：", resp.json())
        # 断言
        common_asserts(resp, 200, False, 99999, "抱歉")
