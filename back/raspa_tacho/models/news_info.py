"""
News Info entitiy.
"""

class NewsInfo:
    def __init__(
        self,
        datetime,
        title,
        src_image,
        paragraphs,
        related_links,
    ):
        self.datetime = datetime
        self.title = title
        self.src_image = src_image
        self.paragraphs = paragraphs
        self.related_links = related_links

    def __str__(self):
        return '\n'.join([
            f'Datetime: {self.datetime}',
            f'Title: {self.title}',
            f'Image src: {self.src_image}',
            '\n\n'.join(self.paragraphs),
            f'Related links: {self.related_links}'
        ])