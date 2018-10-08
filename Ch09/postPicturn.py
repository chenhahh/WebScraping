import requests

files = {'uploadFile': open('../files/editors.csv', 'rb')}
print(files)
r = requests.post("http://pythonscraping.com/pages/processing2.php",
                  files=files)
print(r.text)