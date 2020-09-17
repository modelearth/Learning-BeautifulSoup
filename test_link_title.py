import pytest
import requests
from link_title import LinkTitle


class MockResponse:

    @property
    def text(self):
        return '<html><head><title>test</title></head><body>test</body></html>'

    @property
    def status_code(self):
        return 200

    def raise_for_status(self):
       pass
    

def mock_get(*args, **kwargs):
    return MockResponse()


def test_link_title_returns_title(monkeypatch):
    monkeypatch.setattr(requests, "get", mock_get)
    url = 'http://example.com'
    title = LinkTitle(url).get()
    assert title == 'test' 
