# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class City58DetailItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class City58ChuZuFang(Item):
    # 出租房详情页item
    table = "58_chuzu"
    id = Field()
    title = Field()
    price = Field()
    pay_type = Field()
    lease_type = Field()
    room_type = Field()
    size = Field()
    renovation = Field()
    orientation = Field()
    floor_level = Field()
    floor_nums = Field()
    from_village = Field()
    from_part1 = Field()
    from_part2 = Field()
    address = Field()
    facilities = Field()
    advantage = Field()
    requirements = Field()
    introduce = Field()

class City58ErShouFang(Item):
    # 二手房详情页item
    table = '58_ershoufang'
    id = Field()
    title = Field()
    price = Field()
    meter_price = Field()
    floor_level = Field()
    room_type = Field()
    size = Field()
    orientation = Field()
    is_first_hand = Field()
    renovation = Field()
    property_years = Field()
    buiding_years = Field()
    advantage = Field()
    master = Field()
    house_type = Field()
    ownership = Field()
    downpayment = Field()



