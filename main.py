import asyncio

from src.util.JsonParserUtil import JsonParser
from src.util.NewsBulletinUtils import NewsBulletinUtils


def main():
    news = NewsBulletinUtils()
    # json_obj = JsonParser()
    # json_obj.parse_json()
    news.stage_source_urls()


if __name__ == '__main__':
    main()
