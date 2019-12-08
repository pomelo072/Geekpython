# coding:UTF-8
import requests
from bs4 import BeautifulSoup
import urllib.parse

url = 'http://www.nxpic.org/module/forum/forum-1331-1.html'

res = requests.get(url)

soup = BeautifulSoup(res.text, "lxml")

for link in soup.find_all('a', class_='s xst'):
    print(link.string)
    print(urllib.parse.urljoin(url, link.get('href')))
