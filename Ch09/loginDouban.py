# 使用request登陆豆瓣
import requests
from bs4 import BeautifulSoup

url = 'https://www.douban.com/accounts/login'
# 账号密码
params = {'form_email': ' ', 'form_password': ' '}
r = requests.post(url, data=params)

bsObj = BeautifulSoup(r.text, 'html.parser')
name = bsObj.find("a", {"class": 'bn-more'})
print(name)
