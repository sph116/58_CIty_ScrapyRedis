# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field

class City58Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class City58XiaoQuInfo(Item):
    table = '58_xiaoqu'
    id = Field()
    name = Field()
    location = Field()
    business_location = Field()
    detail_location = Field()
    building_type = Field()
    households = Field()
    price = Field()
    building_age = Field()
    plot_ratio = Field()
    buiding_area = Field()
    Parking_space = Field()
    present_sale_rooms = Field()
    present_zu_rooms = Field()

    Property_right_type = Field()
    Afforestation_rate = Field()
    Developers = Field()
    introduce = Field()

