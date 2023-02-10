"""
{
  "news": {
    "bbc": {"world": "url", "sports": "url", "finance": "url","technology": "url", "entertainment": "url"},
    "cnn": {"world": "url", "sports": "url", "finance": "url","technology": "url", "entertainment": "url"},
    "fox": {"world": "url", "sports": "url", "finance": "url","technology": "url", "entertainment": "url"},
    "cnbc": {"world": "url", "sports": "url", "finance": "url","technology": "url", "entertainment": "url"},
    "yahoo": {"world": "url", "sports": "url", "finance": "url","technology": "url", "entertainment": "url"},
    "npr": {"world": "url", "sports": "url", "finance": "url","technology": "url", "entertainment": "url"},
    "abc": {"world": "url", "sports": "url", "finance": "url","technology": "url", "entertainment": "url"},
    "cbs": {"world": "url", "sports": "url", "finance": "url","technology": "url", "entertainment": "url"},
    "politico": {"world": "url", "sports": "url", "finance": "url","technology": "url", "entertainment": "url"}
  }
}
"""

"""
{
  "news": {
    "us": {
      "cnn": {
        "world": "url",
        "sports": "url",
        "finance": "url",
        "technology": "url",
        "entertainment": "url"
      },
      "fox": {
        "world": "url",
        "sports": "url",
        "finance": "url",
        "technology": "url",
        "entertainment": "url"
      }
    },
    "in": {
      "NDTV": {
        "top": "https://feeds.feedburner.com/ndtvnews-top-stories",
        "world": "https://feeds.feedburner.com/ndtvnews-world-news",
        "sports": "https://feeds.feedburner.com/ndtvsports-latest",
        "finance": "https://feeds.feedburner.com/ndtvprofit-latest",
        "technology": "https://feeds.feedburner.com/gadgets360-latest",
        "entertainment": "https://feeds.feedburner.com/ndtvmovies-latest"
      },
      "India Today": {
        "top": "https://www.indiatoday.in/rss/1206584",
        "world": "https://www.indiatoday.in/rss/1206577",
        "sports": "https://www.indiatoday.in/rss/1206550",
        "finance": "https://www.indiatoday.in/rss/1206513",
        "technology": "url",
        "entertainment": "url"
      },
      "The Indian Express": {
        "world": "url",
        "sports": "url",
        "finance": "url",
        "technology": "url",
        "entertainment": "url"
      },
      "The Hindu": {
        "world": "url",
        "sports": "url",
        "finance": "url",
        "technology": "url",
        "entertainment": "url"
      },
      "News 18": {
        "world": "url",
        "sports": "url",
        "finance": "url",
        "technology": "url",
        "entertainment": "url"
      },
      "Firstpost": {
        "world": "url",
        "sports": "url",
        "finance": "url",
        "technology": "url",
        "entertainment": "url"
      },
      "Zee News": {
        "world": "url",
        "sports": "url",
        "finance": "url",
        "technology": "url",
        "entertainment": "url"
      },
      "Hindustan Times": {
        "world": "url",
        "sports": "url",
        "finance": "url",
        "technology": "url",
        "entertainment": "url"
      }
    }
  }
}
"""


"""
{
  "news": {
    "world": {"bbc": "url", "cnn": "url", "fox": "url","cnbc": "url", "yahoo": "url"},
    "sports": {"cnn": "url", "fox": "url", "espn": "url","yahoo": "url", "npr": "url"},
    "finance": {"cnbc": "url", "fox": "url", "npr": "url","msn": "url", "yahoo": "url"},
    "technology": {"yahoo": "url", "msn": "url", "npr": "url","abc": "url", "cbs": "url"},
    "entertainment": {"ftv": "url", "hooters": "url", "avn": "url","xbiz": "url", "et": "url"},
    "politics": {"npr": "url", "politico": "url", "cnn": "url","fox": "url", "cbs": "url"},
    "weather": {"npr": "url", "weatherchannel": "url", "some-other-shit": "url","noshit": "url", "noshitmf": "url"}
  }
}
"""

le_news = {
  "news": {
    "entertainment": {
      "avn": "url",
      "et": "url",
      "ftv": "url",
      "hooters": "url",
      "xbiz": "url"
    },
    "finance": {
      "cnbc": "url",
      "fox": "url",
      "msn": "url",
      "npr": "url",
      "yahoo": "url"
    },
    "politics": {
      "cbs": "url",
      "cnn": "url",
      "fox": "url",
      "npr": "url",
      "politico": "url"
    },
    "sports": {
      "cnn": "url",
      "espn": "url",
      "fox": "url",
      "npr": "url",
      "yahoo": "url"
    },
    "technology": {
      "abc": "url",
      "cbs": "url",
      "msn": "url",
      "npr": "url",
      "yahoo": "url"
    },
    "weather": {
      "noshit": "url",
      "noshitmf": "url",
      "npr": "url",
      "some-other-shit": "url",
      "weatherchannel": "url"
    },
    "world": {
      "bbc": "http://feeds.bbci.co.uk/news/world/rss.xml",
      "buzzfeed": "https://www.buzzfeed.com/world.xml",
      "cnbc": "https://www.cnbc.com/id/100727362/device/rss/rss.html",
      "cnn": "http://rss.cnn.com/rss/edition_world.rss",
      "fox": "https://moxie.foxnews.com/google-publisher/world.xml",
      "npr": "https://feeds.npr.org/1004/rss.xml",
      "nytimes": "https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/world/rss.xml",
      "un": "https://news.un.org/feed/subscribe/en/news/all/rss.xml",
      "washingtonpost": "https://feeds.washingtonpost.com/rss/world",
      "ndtv": "https://feeds.feedburner.com/ndtvnews-world-news",
      "indiatoday": "https://www.indiatoday.in/rss/1206577",
      "indianexpress": "https://indianexpress.com/section/world/feed/",
      "thehindu": "https://www.thehindu.com/news/national/?service=rss"
    }
  }
}