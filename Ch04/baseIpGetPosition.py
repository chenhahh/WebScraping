# 根据传入的IP地址返回国家代码

import json
from urllib.request import urlopen

key = '43872f9fe4509069f8f3404217c8a875'
def getCountry(ipAddress):
    html = "http://api.ipstack.com/"+ipAddress+"?access_key=43872f9fe4509069f8f3404217c8a875"
    response = urlopen(html).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("country_code")

print(getCountry("50.78.253.58"))