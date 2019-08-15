import requests

try:
    import cookielib
except:
    import http.cookiejar as cookielib

import re

agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
header = {
    # "HOST": "www.zhihu.com",
    # "Referer": "https://www.zhihu.com",
    "User-Agent": agent
}


def get_xsrf():
    response = requests.get("https://www.zhihu.com", headers=header)
    print(response.text)
    return ""


def zhihu_login(account, password):
    # 知乎登录
    if re.match("^1\d{10}", account):
        print("手机号码登录")
        post_url = ""


get_xsrf()
