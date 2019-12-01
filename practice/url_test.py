# coding:UTF-8
from urllib import request
import requests
from bs4 import BeautifulSoup
url = 'http://www.nxpic.org/module/forum/forum-1331-1.html'

res = requests.get(url)

soup = BeautifulSoup(res.text, "lxml")

