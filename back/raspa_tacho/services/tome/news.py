"""
Parsing on news pages.
"""
import re
from datetime import datetime

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
        raw_datetime = self.content.select('.panel .panel-body h5')[0].text
        title = self.content.select('.panel .panel-body h2')[0].text
        src_image = self.content.select('.panel .panel-body .container-fluid .row img')[0]['src']
        raw_paragraphs = self.content.select('.panel .panel-body > p')
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
            src_image,
            paragraphs,
            related_links
        )

    @staticmethod
    def parse_str_datetime_to_datetime(str_datetime: str) -> datetime:
        """
        Parse raw datetime from web page to a python datetime object.

        Args:
            str_datetime (str): Raw datetime.
        
        Return (datetime): Datetime object.
        """
        pattern = r'^Publicada em:.*(?P<date>\d{2}\/\d{2}\/\d{4}) (?P<time>\d{2}:\d{2})$'
        match = re.match(pattern, str_datetime)
        conversion = None
        if match:
            raw_date = match.groupdict().get('date')
            raw_time = match.groupdict().get('time')
            conversion = datetime.strptime(
                f'{raw_date} {raw_time}', '%d/%m/%Y %H:%M',
            )
        return conversion