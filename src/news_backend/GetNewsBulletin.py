from feedparser import parse


# TODO: Testing if title & description are present. Get more reliable news sources than bbc

class GetNewsBulletIn:
    news_url = 'http://feeds.bbci.co.uk/news/world/rss.xml'

    def aggregateRelevantNews(self):
        try:
            return parse(self.news_url)
        except Exception:
            raise Exception
