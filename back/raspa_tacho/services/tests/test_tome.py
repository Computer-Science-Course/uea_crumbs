import unittest
from os.path import join

from bs4 import BeautifulSoup
from requests.models import Response

from raspa_tacho.services.utils.directory import ROOT_PATH
from raspa_tacho.services.tome import Tome

MOCK_PAGES_PATH = join(
    ROOT_PATH, 'services', 'tests', '__mocks__', 'pages',
)
class TestTome(unittest.TestCase):
    """Test suite for Tome class."""
    def setUp(self):
        self.ok_response = Response()
        self.ok_response.status_code = 200

        self.not_ok_response = Response()
        self.not_ok_response.status_code = 404
        with open(
            join(MOCK_PAGES_PATH, 'home.html'), 'r', encoding='utf-8',
        ) as home_page_file:
            home_page = home_page_file.read()
            self.ok_response._content = home_page.encode() # pylint: disable=W0212
            self.not_ok_response._content = None # pylint: disable=W0212

    def test_convert_reponse_to_beautiful_soup_when_status_code_is_200(self):
        """Should convert response to BeautifulSoup when status code is 200."""
        tome = Tome(self.ok_response)
        self.assertIs(type(tome.content), BeautifulSoup)

    def test_not_convert_reponse_to_beautiful_soup_when_status_code_is_not_200(self):
        """Should not convert response to BeautifulSoup when status code is not 200."""
        tome = Tome(self.not_ok_response)
        self.assertIsNone(tome.content)
