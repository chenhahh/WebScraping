# 从给定网站起不断随机获取外链访问
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random


pages = set()
random.seed(datetime.datetime.now())

# 获取页面所有内链的列表
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    # 找到所有以/开头的链接
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                    internalLinks.append(includeUrl+link.attrs['href'])
    return internalLinks

# 获取页面所有的外链列表
def getExternalLinks(bsObj, excluderUrl):
    externalLinks = []
    # 找出所有http or www 开头不包含当前URL的链接
    for link in bsObj.findAll("a",
                              href=re.compile("^(http|www)((?!"+excluderUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

# 随机获取一个外部链接
def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html)
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage)
        return getRandomExternalLink(internalLinks[random.randint(0,
                                     len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is " + externalLink)
    followExternalOnly(externalLink)


followExternalOnly("http://oreilly.com")
