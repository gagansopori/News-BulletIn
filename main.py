from tkinter import *

from src.news_ui.DisplayNewsBulletIn import DisplayNewsBulletIn

if __name__ == '__main__':
    root = Tk()
    root.title('News Bulletin')
    news_object = DisplayNewsBulletIn(root)
    news_object.getBasicWorldNews()
    news_object.config(bg = 'black')
    news_object.pack(side=BOTTOM, fill=BOTH, expand=True)
    root.mainloop()
