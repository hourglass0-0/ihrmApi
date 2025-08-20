def common_asserts(resp, status_code, success, code, message):
    assert status_code == resp.status_code
    assert success is resp.json().get('success')
    assert code == resp.json().get('code')
    assert message in resp.json().get('message')
