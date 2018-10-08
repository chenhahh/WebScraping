import requests

params = {'firstname': 'Chen', 'lastname': 'han'}
r = requests.post("http://pythonscraping.com/files/processing.php", data=params)
print(r.text)