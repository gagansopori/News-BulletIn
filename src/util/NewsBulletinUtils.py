import feedparser, json, asyncio
from time import perf_counter


class NewsBulletinUtils:
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.news = {}
        self.results = []

    def parse_json(self):
        with open('C:/Users/gagan/Documents/GitHub/News-BulletIn/src/resources/source_urls.json') as source:
            data_frame = json.load(source)
            world_news_urls = data_frame['news']['world']
            self.heavy_driver(world_news_urls)
            self.heavy_driver_sync(world_news_urls)
            # result = await asyncio.gather(*[self.fetch_news_async(url) for url in self.news_urls.values()])

    def fetch_news_sync(self, url):
        print(url)
        return feedparser.parse(url)

    async def fetch_news(self, url):
        return await asyncio.to_thread(self.fetch_news_sync, url)

    async def get_ready(self, url):
        return await self.fetch_news(url)

    async def driver(self, url_list):
        start = perf_counter()
        r2d2 = await asyncio.gather(*[self.get_ready(url) for url in url_list.values()])
        stop = perf_counter()
        # print(r2d2)
        print(f'Time Taken for Async - {stop - start}')

    def heavy_driver(self, url_list):
        return self.loop.run_until_complete(self.driver(url_list))

    def heavy_driver_sync(self, url_list):
        start = perf_counter()
        for url in url_list.values():
            print(url)
            result = feedparser.parse(url)

        stop = perf_counter()
        print(f'Time Taken for Sync - {stop - start}')
