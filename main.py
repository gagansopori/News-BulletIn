from tkinter import *

from src.news_ui.DisplayNewsBulletIn import DisplayNewsBulletIn


def main():
    root = Tk()
    root.title('News Bulletin')
    news_object = DisplayNewsBulletIn(root)
    news_object.formatNewsBulletins()
    news_object.config(bg='black')
    news_object.pack(side=BOTTOM, fill=BOTH, expand=True)
    root.mainloop()


if __name__ == '__main__':
    main()
