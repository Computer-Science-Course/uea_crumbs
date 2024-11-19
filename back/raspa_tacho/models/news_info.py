"""
News Info entitiy.
"""

class NewsInfo:
    def __init__(
        self,
        datetime,
        title,
        cover_image_src,
        post_images_srcs,
        paragraphs,
        related_links,
    ):
        self.datetime = datetime
        self.title = title
        self.cover_image_src = cover_image_src
        self.post_images_srcs = post_images_srcs
        self.paragraphs = paragraphs
        self.related_links = related_links

    def __str__(self):
        return '\n'.join([
            f'Datetime: {self.datetime}',
            f'Title: {self.title}',
            f'Cover image src: {self.cover_image_src}',
            f'Post images srcs: {self.post_images_srcs}',
            '\n\n'.join(self.paragraphs),
            f'Related links: {self.related_links}'
        ])