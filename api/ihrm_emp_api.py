import requests


# 定义员工管理表
class IhrmEmpApi(object):
    # 添加员工
    @classmethod
    def add_emp(cls, header, req_data):
        resp = requests.post(url='https://ihrm-java.itheima.net/api/sys/user', headers=header, json=req_data)
        return resp

    # 查询员工
    @classmethod
    def query_emp(cls, emp_id, header):
        resp = requests.get(url='https://ihrm-java.itheima.net/api/sys/user/' + emp_id, headers=header)
        return resp

    # 修改员工
    @classmethod
    def modify_emp(cls, emp_id, header, req_data):
        resp = requests.put(url='https://ihrm-java.itheima.net/api/sys/user/' + emp_id, headers=header, json=req_data)
        return resp

    # 删除员工
    @classmethod
    def del_emp(cls, emp_id, header):
        resp = requests.delete(url='https://ihrm-java.itheima.net/api/sys/user/' + emp_id, headers=header)
        return resp


if __name__ == '__main__':
    req_header = {"Authorization": "3e85e548-cdfb-4442-8e74-da5e05a7330c"}
    json = {
        "username": "user87655430",
        "mobile": "13947874780",
        "workNumber": "9527890aa"
    }
    response = IhrmEmpApi.add_emp(req_header, json)
    print("添加员工结果：", response.json())

    response = IhrmEmpApi.query_emp("1066370498633486336", req_header)
    print("查询员工结果：", response.json())

    modify_data = {"username": "放大镜考虑"}
    response = IhrmEmpApi.modify_emp("1066370498633486336", req_header, modify_data)
    print("修改员工结果：", response.json())

    response = IhrmEmpApi.del_emp("1066370498633486336", req_header)
    print("删除员工结果：", response.json())
