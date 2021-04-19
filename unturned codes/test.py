from bs4 import BeautifulSoup as bs
import requests as req
import json


site = 'https://unturneditems.com/'
resp = req.get(site)

soup = bs(resp.text, 'lxml')
ids = [x.text for x in soup.findAll("span", class_='item-id')]
name = [x.text for x in soup.findAll("span", class_='item-name')]
rare = [x.text for x in soup.findAll("span", class_='rarity')]

items = dict(zip(ids, zip(name, rare)))
print(items['363'])

with open('items.json', 'w', encoding='utf-8') as f:
    json.dump(items, f)
