import os, json, asyncio
import feedparser
from time import perf_counter, strftime, gmtime

from src.util.JsonParserUtil import JsonParser


# url_source = 'src/resources/source_urls.json'
class NewsBulletinUtils:
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.news = {}
        self.results = []

    def stage_source_urls(self, url_list=None):
        """
        Driver Method that helps enrich & validate source urls, fetch RSS feeds from the provided json. If no JSON is
        provided the app with consider the default json.
        :param url_list:
        :return:
        """
        if url_list is not None:
            if isinstance(url_list, list):
                self.gather_data(url_list)
            else:
                raise TypeError
        else:
            sources = JsonParser()
            begin = perf_counter()
            url_list = sources.parse_json()
            self.gather_data(url_list)
            # self.feed_driver_sync(url_list)
            print(f'Time taken to fetch all news: {perf_counter() - begin}')
            # print(self.results[0][0].entries[0].title)

    def gather_data(self, url_list):
        return self.loop.run_until_complete(self.feed_driver(url_list))

    async def feed_driver(self, url_list):
        start = perf_counter()
        self.results.append(await asyncio.gather(*[self.fetch_news(url) for url in url_list]))
        stop = perf_counter()
        print(f'Time Taken for Async - {stop - start}')

    async def fetch_news(self, url):
        return await asyncio.to_thread(self.fetch_news_report, url)

    def fetch_news_report(self, url):
        x = feedparser.parse(url)
        for i in x.entries:
            # print(f'{url}\n')
            print(i.title)
        return x

    # def feed_driver_sync(self, url_list):
    #     start = perf_counter()
    #     for url in url_list:
    #         result = feedparser.parse(url)
    #
    #     stop = perf_counter()
    #     print(f'Time Taken for Sync - {stop - start}')
