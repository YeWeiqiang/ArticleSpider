import requests

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
}
post_url = "http://es.bnuz.edu.cn/default2.aspx"


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
        "RadioButtonList1": "学生",
        "Button4_test": ""
    }
    # response = requests.get("http://es.bnuz.edu.cn/default2.aspx", headers=header)
    # print(response)
    response_text = requests.post(url=post_url, data=post_data, headers=header)
    print(response_text.content.decode('utf8'))


bnuz_loin()
