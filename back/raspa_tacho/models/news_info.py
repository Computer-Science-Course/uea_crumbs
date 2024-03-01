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
        return ' | '.join([
            self.datetime,
            self.title,
            self.src_image,
            self.paragraphs[0],
            str(self.related_links),
        ])