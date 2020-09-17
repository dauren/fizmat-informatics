import requests


r = requests.get("https://fizmat.kz")
a = 11
b = a ** 10
print(r.text())