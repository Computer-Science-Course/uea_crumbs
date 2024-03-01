"""
Module to convert response data and handle searchs on the soup.
"""
from bs4 import BeautifulSoup
from requests.models import Response

class Tome:
    def __init__(self, data: Response):
        self.content = None
        if data.status_code == 200:
            self.content = BeautifulSoup(
                data.text, 'lxml', parser='html.parser',
            )
