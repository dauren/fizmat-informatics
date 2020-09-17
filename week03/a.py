import requests


r = requests.get("https://fizmat.kz")

print(r.text())