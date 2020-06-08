from eventregistry import *
from datetime import datetime


def _parse_datetime(timestamp):
    return datetime.strptime(timestamp,"%Y-%m-%dT%H:%M:%SZ")


class EventRegistryApi:
    def __init__(self):
        # Intitializing eventregistry api
        self.er = EventRegistry(apiKey='7fb9174e-f694-432c-a7ad-aa931be69178')

    def get_news_by_location(self,location_name):
        """

        :param location_name: Name of the location
        :return: list of  {
        'lang': #language of article #String
        'publishDate': # date of publishing #Datetime
        'url': #news urls #string
        'title': #title of article #String
        'body': #body of article
        }
        """
        q= QueryArticlesIter(locationUri=self.er.getLocationUri(locationLabel=location_name))
        news = list()
        for art in q.execQuery(self.er, sortBy = "date",sortByAsc = True,maxItems=10):
            news.append({
                'lang': art.get('lang',None),
                'publishDate': _parse_datetime(art.get('dateTimePub','dateTime')),
                'url': art.get('url',None),
                'title': art.get('title',None),
                'body':art.get('body',None)
            }
            )
        return news

    def get_new_by_location(self,location_cordinates):
        pass