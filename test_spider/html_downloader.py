# coding:UTF-8
import requests


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        response = requests.get(url)
        response.encoding = response.apparent_encoding

        if response.status_code != 200:
            return None

        return response.text
