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

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename="cookies.txt")  # save()方法
try:
    session.cookies.load(ignore_discard=True)
    print("yes")
except:
    print("cookie未能加载")


def get_index():
    response = session.get("https://www.zhihu.com", headers=header)
    with open("index_page.html", "wb") as f:
        f.write(response.text.encode("utf8"))
    print("ok")


def zhihu_login(account, password):
    # 知乎登录
    response = session.get("https://www.zhihu.com", headers=header)
    if re.match("^1\d{10}", account):
        print("手机号码登录")
        post_url = "https://www.zhihu.com/signin?next=%2Fnotifications"
        post_data = {
            "username": account,
            "password": password,
        }

        response_text = session.post(post_url, data=post_data, headers=header)
        print(response_text.content.decode('utf8'))

        session.cookies.save()


zhihu_login()
# get_index()
