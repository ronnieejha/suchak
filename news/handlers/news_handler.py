from news.helpers.news_helper import EventRegistryApi
import logging

SOURCES = {'EventRegistry':EventRegistryApi}


def collect_news_from_source(locationname):
    news = list()
    for source in SOURCES:
        try:
            news.extend(SOURCES[source]().get_news_by_location(locationname))
        except:
            logging.warning('Failed to obatian news from {}'.format(source))
            continue

    if news:
        return news
    else:
        return None
