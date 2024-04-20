import requests

r = requests.get("https://www.github.com/Light-Yagami-The-Kira/Python-Dump-File/")
print(r.text)