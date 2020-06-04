# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy.selector import Selector
from City_58.items import City58XiaoQuInfo
from City_58.utils.parse import *
import redis
from City_58 import settings
import json
from fake_useragent import UserAgent


class City58Spider(scrapy.Spider):
    name = 'city_58'
    allowed_domains = ['58.com']
    start = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))   # 启动时间
    xiaoqu_url = 'https://{}/xiaoqu/{}/'
    redis_cli = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, password=settings.REDIS_PASSWORD, decode_responses=True)
    ua = UserAgent()

    def parse(self, response):
        pass

    def start_requests(self, ):
        area_url_list = []
        response = Selector(requests.get(url='https://{}/xiaoqu/'.format(self.settings.get('HOST')), headers={"User-Agent": self.ua.random}))   # 获取并解析某市 行政区代码
        area_code_list = response.css('.filter-wrap dl:nth-child(1) dd > a::attr(value)').extract()
        if area_code_list:
            for code in area_code_list:
                if code:
                    area_url_list.append(self.xiaoqu_url.format(self.settings.get('HOST'), str(code)))

        for area_url in area_url_list:
            yield Request(url=area_url,
                          callback=self.parse_xiaoqu_url_list,
                          priority=10, dont_filter=True)
            # 抓取行政区小区列表
            # 测试仅抓取一个行政区
            break


    def parse_xiaoqu_url_list(self, response):
        """
        获取行政区 小区列表页
        """
        self.crawler.stats.inc_value("Success_Reqeust")
        xiaoqu_url_list = response.css('.content-wrap .content-side-left ul > li .list-info > h2 > a::attr(href)').extract()
        # 小区详情页url

        if xiaoqu_url_list:
            for xiaoqu_url in xiaoqu_url_list:
                if xiaoqu_url:
                    yield Request(url=xiaoqu_url,
                                  callback=self.xiaoqu_detail_page,
                                  priority=9, dont_filter=True)

        # if response.xpath('//a[@class="nextPage next"]/span'):
        #     if response.meta.get("page_num"):
        #         page_num = response.meta.get("page_num")
        #         next_url = "{}pn_{}/".format(response.url, page_num)
        #         yield Request(url=next_url, meta={"page_num": page_num + 1}, dont_filter=True)
        #     else:
        #         page_num = 2
        #         next_url = "{}pn_{}/".format(response.url, page_num)
        #         yield Request(url=next_url, meta={"page_num": page_num + 1}, dont_filter=True)
                # 测试仅抓取一个小区
                # break

    def xiaoqu_detail_page(self, response):
        """
        解析小区详情页
        """
        xiaoqu_detail_data = parse_xiaoqu_detail_page(response)
        item = City58XiaoQuInfo()
        item.update(xiaoqu_detail_data)
        self.logger.debug(item)
        yield item

        # 二手房列表页首页
        ershoufang_url = response.url + 'ershoufang/'
        yield Request(url=ershoufang_url,
                      callback=self.ershoufang_list_page,
                      priority=8, dont_filter=True)

        # 出租房列表页首页
        chuzufang_url = response.url + 'chuzu/?ib=0/'
        yield Request(url=chuzufang_url,
                      callback=self.chuzufang_list_page,
                      priority=7, dont_filter=True)


    def ershoufang_list_page(self, response):
        """
        解析二手房列表页信息 (从列表页直接获取有效信息,不再递归向下处理)
        """
        # 获取当前小区二手房的数量
        ersohufang_nums = eval(response.css("div.fl.filterCheckbox > span > b::text").extract_first())
        if ersohufang_nums:
            # 记录请求成功的数量
            ershoufang_urls = response.xpath('//table[@class="tbimg"]//tr/td[2]/a[1]/@href').extract()

            if ershoufang_urls:
                for url in ershoufang_urls:
                    url_data = (url, "8", "parse_sel_datail")
                    self.redis_cli.rpush("city_58_detail:new_urls", json.dumps(url_data))

            # 测试仅抓取二手房列表的第一页数据

            # 获取二手房列表下一页数据
            next_page_url = response.css('.listwrap .pagerNumber  a:last-child::attr(href)').extract_first()
            if next_page_url:
                yield Request(url=next_page_url,
                              callback=self.ershoufang_list_page)


    def chuzufang_list_page(self, response):
        """
        获取小区出租房详情页URL
        """
        chuzufang_detail_url_list = response.xpath('//table[@class="tbimg"]//tr[contains(@logr, "_")]/td[2]/a[1]/@href').extract()
        if chuzufang_detail_url_list:
            for url in chuzufang_detail_url_list:
                url_data = (url, "8", "parse_chuzu_detail")
                self.redis_cli.rpush("city_58_detail:new_urls", json.dumps(url_data))



        # 测试仅抓取出租房列表页第一页

        # 获取小区出租房列表下一页
        next_page_url = response.css('.listwrap .pagerNumber a:last-child::attr(href)').extract_first()
        if next_page_url:
            yield Request(url=next_page_url,
                          callback=self.chuzufang_list_page)
















