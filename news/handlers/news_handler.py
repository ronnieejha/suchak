from news.helpers.news_helper import EventRegistryApi

SOURCES = [EventRegistryApi]

def collect_news_from_source(locationname):
    news = list()
    for source in SOURCES:
        try:
            news.extend(source().get_news_by_location(locationname))
        except:
            continue
            #log the error
    if news:
        return news
    else:
        return None
