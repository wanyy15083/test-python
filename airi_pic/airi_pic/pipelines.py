# -*- coding: utf-8 -*-

from scrapy import Request
from scrapy.exceptions import DropItem

from scrapy.pipelines.images import ImagesPipeline


class AiriPicPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['airi_image_url']:
            yield Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('图片未下载好 %s' % image_paths)
