import requests
import re
import json
import base64
import rsa
import binascii

session = requests.session()
login_url = "https://login.sina.com.cn/sso/login.php"
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    # "Cache-Control": "max-age=0",
    # "Connection": "keep-alive",
    # "Content-Length": "1013",
    "Content-Type": "application/x-www-form-urlencoded",
    # "Cookie": "UOR=www.baidu.com,finance.sina.com.cn,; ULV=1565742847507:1:1:1::; SINAGLOBAL=219.128.72.70_1565742850.89500; UM_distinctid=16c8d8be09657c-01fbce7354af34-7373e61-13c680-16c8d8be0975b8; lxlrttp=1560672234; U_TRS1=00000046.2074f62.5d54da91.36b57c7a; SUB=_2AkMqCu0qf8NxqwJRmP4QyGngbIVwwgjEieKcVhzxJRMyHRl-yD83qnEOtRB6AYrDxVoe5hnWcsSftrcF8mHaIRc-rurE; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWmxh1v5cQCB9R0ebU8Ru1G; login=48088277f83072f029fddb1edad3803b; Apache=219.128.72.70_1565942305.911990",
    "Host": "login.sina.com.cn",
    "Origin": "https://weibo.com",
    "Referer": "https://weibo.com/",
    # "Sec-Fetch-Mode": "nested-navigate",
    # "Sec-Fetch-Site": "cross-site",
    # "Sec-Fetch-User": "?1",
    # "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
}

data = {
    "entry": "weibo",
    "gateway": "1",
    "savestate:": "7",
    # "qrcode_flag": "false",
    "useticket": "1",
    "pagerefer": "https://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=https%3A%2F%2Fweibo.com%2F&domain=.weibo.com&sudaref=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DDZ88shdA6I1rGo7ZDaxun0yvZVOqi3yIva7sEx07P6_%26wd%3D%26eqid%3Def29d5c700004c80000000065d566213&ua=php-sso_sdk_client-0.6.28&_rand=1565942296.8878",
    "vsnf": "1",
    "su": "",
    "service": "miniblog",
    "servertime": "",
    "nonce": "",
    "pwencode": "rsa2",
    "rsakv": "",
    "sp": "",
    "sr": "1440*900",
    "encoding": "UTF-8",
    "prelt": "17",
    "url": "https://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack",
    "returntype": "META",
}


def getInfo():
    url = "https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)"
    text = session.get(url).text
    info = re.compile(r'({.*})')
    i = json.loads(str(info))
    print(i)
    data["servertime"] = str(i['servertime'])
    data["rsakv"] = i['rsakv']
    data["nonce"] = i['nonce']
    data['pubkey'] = i['pubkey']
    print(text)


if __name__ == '__main__':
    getInfo()
