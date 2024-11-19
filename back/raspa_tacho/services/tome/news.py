"""
Parsing on news pages.
"""
from datetime import datetime
import locale

from requests.models import Response

from raspa_tacho.services.tome import Tome
from raspa_tacho.models.news_info import NewsInfo

class TomeNews(Tome):
    def __init__(self, data: Response):
        super().__init__(data)

    def info(self) -> NewsInfo:
        """
        Get news info.

        Return (NewsInfo): Info from news page.
        """
        raw_datetime = self.content.select('header ul .meta-date')[0].text
        title = self.content.select('.page-title')[0].text
        cover_image_src = self.content.select('.hero-section img')[0]['src']
        post_images_srcs = [image['src'] for image in self.content.select('.ct-container > article img')]
        raw_paragraphs = self.content.select('article p')
        raw_related_link_anchors = self.content.select('.panel .panel-body .panel-group .panel-default > a')
        raw_related_link_titles = self.content.select('.panel .panel-body .panel-group .panel-default > a p')

        paragraphs = [raw_paragraph.text for raw_paragraph in raw_paragraphs if raw_paragraph.text]

        related_links = [
            { 'title': raw_related_link_title.text, 'href': raw_related_link_ancor.get('href'), 'src': raw_related_link_ancor.get('href'), }
            for raw_related_link_title, raw_related_link_ancor in zip(raw_related_link_titles, raw_related_link_anchors)
        ]

        datetime_object = self.parse_str_datetime_to_datetime(raw_datetime)

        return NewsInfo(
            str(datetime_object),
            title,
            cover_image_src,
            post_images_srcs,
            paragraphs,
            related_links,
        )

    @staticmethod
    def parse_str_datetime_to_datetime(str_datetime: str) -> datetime:
        """
        Parse raw datetime from web page to a python datetime object.

        Args:
            str_datetime (str): Raw datetime.

        Return (datetime): Datetime object.
        """
        locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

        return datetime.strptime(str_datetime, "%d de %B de %Y").date()