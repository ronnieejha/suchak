import random
import string
from datetime import datetime

from eventregistry import *

from news.configs.news_apis import EventRegistryKey


def _parse_datetime(timestamp):
    return datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")


def _generate_key():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))


class EventRegistryApi:
    def __init__(self):
        # Intitializing eventregistry api
        self.er = EventRegistry(apiKey=EventRegistryKey)

    def get_news_by_location(self, location_name):
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
        q = QueryArticlesIter(locationUri=self.er.getLocationUri(locationLabel=location_name))
        news = list()
        for art in q.execQuery(self.er, sortBy="date", sortByAsc=True, maxItems=20):
            news.append({
                'key': _generate_key(),
                'lang': art.get('lang', None),
                'publishDate': _parse_datetime(art.get('dateTimePub', 'dateTime')),
                'url': art.get('url', None),
                'title': art.get('title', None),
                'body': art.get('body', None)
            }
            )
        return news

    def get_new_by_cordinates(self, location_cordinates):
        pass
