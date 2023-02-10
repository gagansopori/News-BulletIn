import asyncio
from src.util.NewsBulletinUtils import NewsBulletinUtils


def main():
    news = NewsBulletinUtils()
    news.parse_json()


if __name__ == '__main__':
    main()
