import sys
from consts import FLICKR_KEY
from datetime import date
from icrawler.builtin import FlickrImageCrawler

tag = sys.argv[1]
print(tag)
flickr_crawler = FlickrImageCrawler(FLICKR_KEY, storage={'root_dir': './images'})

flickr_crawler.crawl(
        max_num=20000, tags=tag,
        min_upload_date=date(2013, 5, 25),
        sort='interestingness-desc'
)
