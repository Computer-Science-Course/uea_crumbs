from raspa_tacho.services.minde import Minde
from raspa_tacho.services.tome.home import TomeHome
from raspa_tacho.services.tome.news import TomeNews

minde = Minde()
home_content = minde.get_data('https://www.uea.edu.br/')

tome_home = TomeHome(home_content)
for url in tome_home.last_news_urls():
    response = minde.get_data(url)
    tome_news = TomeNews(response)
    print(tome_news.info())
    print('*' * 100)
