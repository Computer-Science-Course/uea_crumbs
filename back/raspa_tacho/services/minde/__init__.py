"""
Module to fetch data from website.
"""
import requests
from requests.models import Response

class Minde:
    def get_data(self, url: str) -> Response:
        """
        Get a address data.

        Args:
            url (str): Target url.

        Return (Response): Target content.
        """
        response = requests.get(
            url=url,
            verify=False
        )
        return response
