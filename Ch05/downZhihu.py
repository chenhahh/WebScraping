from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.douban.com")
bsObj = BeautifulSoup(html)
print(html)
Lists = bsObj.findAll("a", {"class": "cover audio new"})
pictures = [list.find("img")['src'] for list in Lists ]
print(pictures)
for picture in pictures:
    name = picture.split("/")[-1]
    print(name)
    urlretrieve(picture, name)
