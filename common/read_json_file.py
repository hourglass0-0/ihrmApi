import json


def read_json_data(filename):
    with open(filename, 'r', encoding='utf8') as f:
        json_data = json.load(f)
        login_list = []
        for data in json_data:
            tmp = tuple(data.values())
            login_list.append(tmp)

        return login_list


if __name__ == '__main__':
    res = read_json_data('../data/login_data.json')
    print(res)
