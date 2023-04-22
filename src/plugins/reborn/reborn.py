import requests


def send_get_request():
    url = "https://api.azite.cn/reborn/"

    # 发送 GET 请求并获取响应
    response = requests.get(url)

    # 输出响应内容
    return response.text

