from tkinter import Frame, Label
from tkinter.constants import *
from feedparser import parse


class DisplayNewsBulletIn(Frame):
    news_url = 'http://feeds.bbci.co.uk/news/world/rss.xml'

    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.frame = Frame(parent, bg='black')
        self.frame.pack(side=BOTTOM, fill=BOTH, expand=False)

        self.world_news = {}
        self.headline_ctr = 0

    def displayNewsBulletins(self, news_headline, news_description):
        # Generate New Child Label
        for child in self.frame.winfo_children():
            child.destroy()

        # Headline
        self.headline_label = Label(self.frame, font=('Segoe UI Semilight', 20), fg='white', bg='black')
        self.headline_label.config(text=news_headline, wraplength=self.winfo_screenwidth()-5, justify=CENTER)
        self.headline_label.pack(side=TOP, anchor=CENTER, padx=5)

        # Description
        self.description_label = Label(self.frame, font=('Segoe UI Semilight', 14), fg='white', bg='black')
        self.description_label.config(text=news_description, wraplength=self.winfo_screenwidth()-10, justify=CENTER)
        self.description_label.pack(side=TOP, anchor=CENTER, padx=10, pady=10)

    def getBasicWorldNews(self):
        if self.headline_ctr == 0 and len(self.world_news) == 0:
            self.world_news = parse(self.news_url)
        elif self.headline_ctr > len(self.world_news['entries']) - 1:
            self.headline_ctr = 0
            self.world_news = parse(self.news_url)
        news_headline = self.world_news.entries[self.headline_ctr].title
        news_description = self.world_news.entries[self.headline_ctr].description
        self.headline_ctr += 1
        print('%d. %s' %(self.headline_ctr, news_headline))

        self.displayNewsBulletins(news_headline, news_description)
        self.headline_label.after(15000, self.getBasicWorldNews)
