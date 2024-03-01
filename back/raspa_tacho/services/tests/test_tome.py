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
    def setUp(self):
        with open(
            join(MOCK_PAGES_PATH, 'home.html'), 'r', encoding='utf-8',
        ) as home_page_file:
            home_page = home_page_file.read()
            response = Response()
            response.status_code = 200
            response._content = home_page.encode()
            self.tome = Tome(response)

    def test_convert_reponse_to_BeautifulSoup_when_status_code_is_200(self):
        self.assertIs(type(self.tome.content), BeautifulSoup)
