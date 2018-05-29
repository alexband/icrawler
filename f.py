import sys
from consts import FLICKR_KEY
from datetime import date
from icrawler.builtin import FlickrImageCrawler


def processor(tag):
    flickr_crawler = FlickrImageCrawler(
        FLICKR_KEY,
        feeder_threads=5,
        parser_threads=5,
        downloader_threads=5,
        storage={'root_dir': '/data1/flickr/%s/' % tag})

    flickr_crawler.crawl(
        max_num=1000,
        tags=tag,
        min_upload_date=date(2015, 5, 25),
        sort='interestingness-desc',
        #downloader_kwargs={'name': tag}
    )


if __name__ == '__main__':
    tags = open("./new_tags", "r")
    tags = sorted([l.strip() for l in tags])
    for t in tags:
        print('start')
        print(t)
        processor(t)
        print('end')
