import requests


def send_get_request(mode, msg, uuid):
    url = "http://104.168.144.135:5000/api/query"

    # 将参数添加到字典中
    params = {
        "mode": mode,
        "msg": msg,
        "uuid": uuid
    }

    # 发送 GET 请求并获取响应
    response = requests.get(url, params=params)

    # 输出响应内容
    return response.text

