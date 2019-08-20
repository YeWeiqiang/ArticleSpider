import requests
from PIL import Image
from pytesseract import *
import re

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
}
post_url = "http://es.bnuz.edu.cn/default2.aspx"
s = requests.session()

def initTable(threshold=140):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table


def checkcode():
    api = 'http://es.bnuz.edu.cn/CheckCode.aspx'
    img_response = s.get(api, headers=header)
    with open("img.jpg", "wb") as f:
        f.write(img_response.content)
    img = Image.open('img.jpg')
    img = img.convert('L')
    binaryImage = img.point(initTable(), '1')
    img = binaryImage.convert('L')
    result = pytesseract.image_to_string(img)
    return result


def bnuz_loin(account, password):
    post_data = {
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": "",
        "__VIEWSTATE": "/wEPDwUJLTQwNjEzNDEyDxYCHgh1c2VybmFtZWgWAmYPZBYEAgEPDxYCHgRUZXh0BQU1NjQ2NGRkAhkPFgQeCWlubmVyaHRtbAUS6aqM6K+B56CB5LiN5q2j56GuHgdWaXNpYmxlZ2Rk/IAmeaQEpUsOgwHaquNCgLzuygY=",
        "__VIEWSTATEGENERATOR": "09394A33",
        "__PREVIOUSPAGE": "P41Qx-bOUYMcrSUDsalSZQ66PXL-H_8xeQ4t7bJ3gWnYCDI-j8Z8SOoK8eM1",
        "__EVENTVALIDATION": "/wEWDALmncP/DwLs0bLrBgLs0fbZDALs0Yq1BQK/wuqQDgKAqenNDQLN7c0VAveMotMNAu6ImbYPArursYYIApXa/eQDAoixx8kBMLLMm5GFYNoPs5MaRP8bYvFaQso=",
        "TextBox1": account,
        "TextBox2": password,
        "TextBox3": checkcode(),
        "RadioButtonList1": "学生",
        "Button4_test": ""
    }
    # response = requests.get("http://es.bnuz.edu.cn/default2.aspx", headers=header)
    # print(response.content)

    response_text = s.post(url=post_url, data=post_data, headers=header)
    print(response_text.content.decode('utf8'))


bnuz_loin('1701040120', '1.11.1111.1')

