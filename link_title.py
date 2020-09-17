import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup


class LinkTitleException(Exception):
    """ Base LinkerTitle Exception """
    pass


class LinkTitle:
    def __init__(self, url):
        self._url = url

    def _get_html(self):
        response = requests.get(self._url)
        response.raise_for_status()
        if response:
            return response.text
        return ""


    def _get_title(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        if soup.title.string:
            return soup.title.string
        return ""

    def get(self):
        try:
            html = self._get_html()
        except HTTPError as e:
            raise LinkerTitleException("There was a network error")
        return self._get_title(html)
