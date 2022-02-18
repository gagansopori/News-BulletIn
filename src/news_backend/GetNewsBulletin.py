# from feedparser import parse
#
#
# class GetNewsBulletIn:
#     # news_url = 'http://feeds.bbci.co.uk/news/world/rss.xml'
#
#     def __init__(self, parent, *args, **kwargs):
#         # DisplayNewsBulletIn.__init__(self, parent, *args, **kwargs)
#         self.world_news = {}
#         self.headline_ctr = 0
#         # self.display_news = DisplayNewsBulletIn(parent)
#
#     def getBasicWorldNews(self):
#         return parse(self.news_url)
#
#         # if self.headline_ctr == 0 and len(self.world_news) == 0:
#         #     self.world_news = parse(self.news_url)
#         # elif self.headline_ctr > len(self.world_news['entries']) - 1:
#         #     self.headline_ctr = 0
#         #     self.world_news = parse(self.news_url)
#         #
#         # news_headline = self.world_news.entries[self.headline_ctr].title
#         # news_description = self.world_news.entries[self.headline_ctr].description
#         # self.headline_ctr += 1
#         #
#         # self.display_news.displayNewsBulletins(news_headline, news_description)
#         # self.displayNewsBulletins(news_headline,news_description)
