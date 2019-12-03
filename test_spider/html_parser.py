# coding:UTF-8
import urllib.parse
from bs4 import BeautifulSoup
import re


class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, "html.parser", from_encoding="UTF-8")
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()

        for link in soup.find_all('a', class_='pg'):
            new_url = link.get('href')
            new_full_url = urllib.parse.urljoin('http://www.nxpic.org/module/forum/', new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url

        # <dd class="lemmaWgt-lemmaTitle-title"> <h1 >Python</h1>
        title_node = soup.find('a', class_="s xst")
        res_data['title'] = title_node.string

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('a', class_='s xst')
        res_data['summary'] = summary_node.get('href')

        return res_data
