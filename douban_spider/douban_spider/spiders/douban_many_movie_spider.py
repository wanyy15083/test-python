from pyquery import rules
from scrapy.http import HtmlResponse
from scrapy.spider import Spider
from scrapy.http import Request, response
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from douban_spider.items import DoubanSpiderItem


class DoubanSpider(CrawlSpider):
    name = "douban_many_movie_spider"

    download_delay = 1
    allowed_domins = []

    start_urls = [
        'http://movie.douban.com/top250?start=0&filter='
    ]

    rules = (
        Rule(LinkExtractor(allow=(r'movie\.douban\.com/top250\?start=\d+&filter='), ), callback='parse_item',
             follow=True),
    )


    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, headers={
                'referer:': 'http://movie.douban.com/top250',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
            })


    def parse_item(self, response):
        print response

        sel = Selector(response)
        item = DoubanSpiderItem()

        movie_name = sel.xpath('//div[@class="hd"]/a/span[@class="title"][1]/text()').extract()
        print movie_name
        star = sel.xpath('//div[@class="star"]/span[@class="rating_num"]/text()').extract()
        quote = sel.xpath('//p[@class="quote"]/span[@class="inq"]/text()').extract()

        item['movie_name'] = [n.encode('utf-8') for n in movie_name]
        item['star'] = [n.encode('utf-8') for n in star]
        item['quote'] = [n.encode('utf-8') for n in quote]

        yield item


        # print movie_name,star,quote
