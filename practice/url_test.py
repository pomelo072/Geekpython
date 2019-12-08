# coding:UTF-8
import requests
from bs4 import BeautifulSoup
import urllib.parse
import re


class Urlmanagers(object):
    def __init__(self):
        self.new_urls = set()
        self.odd_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.odd_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.odd_urls.add(new_url)
        return new_url


class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, "lxml")
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()

# <a href="forum-1331-2.html">2</a>
        for link in soup.find_all('div', class_='pg'):
            for lk in link.find_all('a', href= re.match(r'forum-1331-+\d{1,3}.html')):
                new_url = link.get('href')
                new_full_url = urllib.parse.urljoin(page_url, new_url)
                new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        title_node = soup.find('a', class_="s xst")
        res_data['title'] = title_node.string

        summary_node = soup.find('a', class_='s xst')
        res_data['summary'] = urllib.parse.urljoin('http://www.nxpic.org/module/forum/', summary_node.get('href'))

        return res_data


class HtmlDownloader(object):
    def download(self, new_url):
        if new_url is None:
            return None
        response = requests.get(new_url)
        if response.status_code != 200:
            return None
        response.encoding = response.apparent_encoding

        return response.text


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<tb>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")
        fout.write("</tb>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()


class SpiderMain(object):
    def __init__(self):
        self.urls = Urlmanagers()
        self.parser = HtmlParser()
        self.downloader = HtmlDownloader()
        self.outputer = HtmlOutputer()

    def craw(self, root_url):
        self.urls.add_new_url(root_url)
        count = 1
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            print('craw {0} : {1}'.format(count, new_url))
            html_cont = self.downloader.download(new_url)
            new_urls, new_data = self.parser.parse(new_url, html_cont)
            self.urls.add_new_urls(new_urls)
            self.outputer.collect_data(new_data)
            count = count + 1

            if count == 1000:
                break

        self.outputer.output_html()


if __name__ == "__main__":
    root_url = 'http://www.nxpic.org/module/forum/forum-1331-1.html'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
