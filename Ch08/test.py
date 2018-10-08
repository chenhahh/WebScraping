from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.python.org/dev/peps/pep-0257/")
bsObj = BeautifulSoup(html)
text = bsObj.get_text()
text = text.replace("\n", " ")
print(text)