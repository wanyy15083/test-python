# -*- coding: utf-8 -*-

BOT_NAME = 'douban_new_movie'

SPIDER_MODULES = ['douban_new_movie.spiders']
NEWSPIDER_MODULE = 'douban_new_movie.spiders'

ROBOTSTXT_OBEY = False

ITEM_PIPELINES={
    'douban_new_movie.pipelines.DoubanNewMoviePipeline':300
}


# DEFAULT_REQUEST_HEADERS = {
#     'referer': 'http://www.douban.com/',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
# }

# DOWNLOAD_DELAY=3