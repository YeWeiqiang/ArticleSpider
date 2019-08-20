import requests
from bs4 import BeautifulSoup

url = 'http://es.bnuz.edu.cn/default2.aspx'
headers = {
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
}
s = requests.Session()
index = s.get(url, headers=headers)
soup = BeautifulSoup(index.content, 'html5lib')
value1 = soup.find('input', id='__VIEWSTATE')['value']
value2 = soup.find('input', id='__PREVIOUSPAGE')['value']
value3 = soup.find('input', id='__EVENTVALIDATION')['value']
payload = {
           "__EVENTTARGET": "",
           "__EVENTARGUMENT": "",
           "__VIEWSTATE":
               value1,
           "__VIEWSTATEGENERATOR": "09394A33",
           "__PREVIOUSPAGE": value2,
           "__EVENTVALIDATION": value3,
           "TextBox1": "",
           "TextBox2": "",
           "RadioButtonList1": "学生",
           "Button4_test": ""
           }
post1 = s.post(url, data=payload, headers=headers)
content = post1.content.decode('utf-8')
print(content)
