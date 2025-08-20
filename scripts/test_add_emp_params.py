import pytest

from common.assert_tools import common_asserts
from api.ihrm_emp_api import IhrmEmpApi
# from common.db_tools import DBTools
from common.get_header import get_header
from common.read_json_file import read_json_data
from config import TEL, BASE_DIR


# 定义测试类 - 实现参数化
class TestAddEmpParams(object):
    req_header = None

    def setup_class(self):
        self.req_header = get_header()

    # def setup(self):
    #     del_sql = f"delete from bs_user where mobile='{TEL}';"
    #     DBTools.db_uid(del_sql)
    #
    # def teardown(self):
    #     del_sql = f"delete from bs_user where mobile='{TEL}';"
    #     DBTools.db_uid(del_sql)

    filename = BASE_DIR + "/data/add_emp_data.json"

    # 定义通用测试方法 - 测试 添加员工 参数化
    @pytest.mark.parametrize("desc, req_data, status_code, success, code, message", read_json_data(filename))
    def test_add_emp(self, desc, req_data, status_code, success, code, message):
        # 调用自己封装的 api，发送 添加员工请求
        resp = IhrmEmpApi.add_emp(self.req_header, req_data)
        print(desc, "：", resp.json())
        # 断言
        common_asserts(resp, status_code, success, code, message)

    # def test02_add_ok_all(self):
    #     # 调用自己封装的 api，发送 添加员工请求
    #     req_header = {"Authorization": "58ad27cc-cb05-48f4-9812-becaa72308e5"}
    #     req_data = {
    #         "username": "齐天小圣朱小姐001",
    #         "mobile": TEL,
    #         "timeOfEntry": "2022-02-01",
    #         "formOfEmployment": 1,
    #         "workNumber": "9009",
    #         "departmentName": "研发部",
    #         "departmentId": "1480198742740082688",
    #         "correctionTime": "2022-02-27T16:00:00.000Z"
    #     }
    #     resp = IhrmEmpApi.add_emp(req_header, req_data)
    #     print("全部-添加成功：", resp.json())
    #     # 断言
    #     common_assert(resp, 200, True, 10000, "操作成功")
    #
    # def test03_username_None(self):
    #     # 调用自己封装的 api，发送 添加员工请求
    #     req_header = {"Authorization": "58ad27cc-cb05-48f4-9812-becaa72308e5"}
    #     req_data = {
    #         "username": None,
    #         "mobile": TEL,
    #         "timeOfEntry": "2022-02-01",
    #         "formOfEmployment": 1,
    #         "workNumber": "9009",
    #         "departmentName": "研发部",
    #         "departmentId": "1480198742740082688",
    #         "correctionTime": "2022-02-27T16:00:00.000Z"
    #     }
    #     resp = IhrmEmpApi.add_emp(req_header, req_data)
    #     print("用户名为空：", resp.json())
    #     # 断言
    #     common_assert(resp, 200, False, 20002, "新增员工失败")
