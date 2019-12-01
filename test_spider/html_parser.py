# coding:UTF-8
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import re


class HtmlPasser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, "html.parser", from_encoding="UTF-8")
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._gei_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()

        # /item/python/123.htm
        h_ref = re.complie(r'/forum-1331-\d{1,5}.html')
        links = soup.find_all('a', href=h_ref.re.match())
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _gei_new_data(self, page_url, soup):
        res_data = {}

        # url

        # <dd class="lemmaWgt-lemmaTitle-title"> <h1 >Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()

        return res_data
