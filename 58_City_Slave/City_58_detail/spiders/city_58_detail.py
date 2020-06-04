# -*- coding: utf-8 -*-
import scrapy
from City_58_detail.items import City58ChuZuFang, City58ErShouFang
from City_58_detail.utils.parse import parse_chuzu_detail_page, parse_ershoufang_detail_page
from scrapy_redis.spiders import RedisSpider
import redis
from City_58_detail import settings


class City58DetailSpider(RedisSpider):
    name = 'city_58_detail'
    allowed_domains = ['58.com']
    # start_urls = ['http://58.com/']
    redis_key = 'city_58_detail:start_urls'

    custom_settings = {
        # 'LOG_LEVEL': 'DEBUG',
        'DOWNLOAD_DELAY': 0,

        # 指定redis数据库的连接参数
        'REDIS_HOST': settings.REDIS_HOST,
        'REDIS_PORT': settings.REDIS_PORT,

        # 指定 redis链接密码，和使用哪一个数据库
        'REDIS_PARAMS': {
            'password': settings.REDIS_PASSWORD,
        },
    }

    def parse(self, response):
        pass

    def parse_sel_datail(self, response):
        """
        解析并存储 sel
        :param response:
        :return:
        """
        sel_detail_data = parse_ershoufang_detail_page(response)
        item = City58ErShouFang()
        item.update(sel_detail_data)
        yield item

    def parse_chuzu_detail(self, response):
        chuzu_detail_data = parse_chuzu_detail_page(response)
        item = City58ChuZuFang()
        item.update(chuzu_detail_data)
        yield item



