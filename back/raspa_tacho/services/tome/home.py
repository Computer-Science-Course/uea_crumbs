"""
Parsing on home page.
"""
from typing import List

from requests.models import Response

from raspa_tacho.services.tome import Tome

class TomeHome(Tome):
    def __init__(self, data: Response):
        super().__init__(data)

    def last_news_urls(self) -> List[str]:
        """
        Get last news urls.

        Return (List[str]): Last news urls.
        """
        a_tags = self.content.select('.carousel-inner .item a')
        urls = [a_tag['href'] for a_tag in a_tags]
        return urls