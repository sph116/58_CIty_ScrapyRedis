from City_58_detail.utils.common import get_md5, handlefont
import requests
import re
from scrapy.http import Request

def parse_chuzu_detail_page(response):
    """
    解析小区出租房详情页
    """
    result = dict()
    text = response.text
    try:
        result["id"] = get_md5(response.url)
        result["title"] = handlefont(text, response.xpath('//div[@class="house-title"]/h1/text()').extract_first())
        # 租房标题
        result["price"] = handlefont(text, response.xpath('//div[@class="house-basic-right fr"]/div[1]/div[1]/div[1]/span/b/text()').extract_first())
        # 租房价格
        result["pay_type"] = handlefont(text, response.xpath('//div[@class="house-basic-right fr"]/div[1]/div[1]/div[1]/span[2]/text()').extract_first())
        # 支付方式 
        result["lease_type"] = handlefont(text, response.xpath('//div[@class="house-basic-right fr"]/div[1]/div[1]/ul/li[1]/span[2]/text()').extract_first())
        # 租赁类型 整 
        li2 = response.xpath('//div[@class="house-basic-right fr"]/div[1]/div[1]/ul/li[2]/span[2]/text()').extract()[0].split('\xa0\xa0')
        result["room_type"] = handlefont(text, li2[0])
        # 房屋类型 几市几厅
        result["size"] = handlefont(text, li2[1]).replace(' ', '').replace("平", "")
        # 房屋大小
        result["renovation"] = handlefont(text, li2[2]).replace(' ', '')
        # 装修程度
        li3 = response.xpath('//div[@class="house-basic-right fr"]/div[1]/div[1]/ul/li[3]/span[2]/text()').extract()[0].split('\xa0\xa0')
        result["orientation"] = handlefont(text, li3[0])
        # 房屋朝向
        try:
            result["floor_level"] = handlefont(text, li3[1].split('/')[0])
            # 楼层类型
            result["floor_nums"] = handlefont(text, li3[1].split('/')[1]).replace('层', '')
            # 楼层数
        except:
            result["floor_level"] = handlefont(text, li3[1])
        result["from_village"] = handlefont(text, response.xpath('//div[@class="house-basic-right fr"]/div[1]/div[1]/ul/li[4]/span[2]/a/text()').extract_first())
        # 所属小区
        result["from_part1"] = handlefont(text, response.xpath('//div[@class="house-basic-right fr"]/div[1]/div[1]/ul/li[5]/span[2]/a[1]/text()').extract_first())
        # 所属区
        result["from_part2"] = handlefont(text, response.xpath('//div[@class="house-basic-right fr"]/div[1]/div[1]/ul/li[5]/span[2]/a[2]/text()').extract_first())
        # 所属区域
        result["address"] = handlefont(text, response.xpath('//div[@class="house-basic-right fr"]/div[1]/div[1]/ul/li[6]/span[2]/text()').extract_first()).replace('\n', '').replace(' ', '')
        # 具体地址
        result["facilities"] = handlefont(text, ",".join(response.xpath('//ul[@class="house-disposal"]/li/text()').extract()))
        # 房屋内设施
        result["advantage"] = handlefont(text,",".join(response.xpath('//ul[@class="introduce-item"]/li[1]/span[2]/em/text()').extract()))
        # 房屋优点
        result["requirements"] = handlefont(text, ",".join(response.xpath('//ul[@class="introduce-item"]/li[2]/span[2]/em/text()').extract()))
        # 租房要求
        result["introduce"] = handlefont(text, response.xpath('//ul[@class="introduce-item"]/li[3]/span[2]/text()').extract_first())

        return result
    except Exception as e:
        _ = e

def parse_ershoufang_detail_page(response):
    # 解析小区二手房 详情页
    result = {}
    text = response.text
    try:
        result["id"] = get_md5(response.url)
        result["title"] = handlefont(text, response.xpath('//div[@class="house-title"]/h1/text()').extract_first())
        # 标题
        result["price"] = handlefont(text, response.xpath('//span[@class="price strongbox"]/text()').extract_first())
        # 总价
        result["meter_price"] = handlefont(text, response.xpath('//span[@class="unit strongbox"]/text()').extract_first()).replace("\xa0元/平", "")
        # 每平米价格
        result["floor_level"] = handlefont(text, response.xpath('//div[@class="general-item general-situation"]/div/ul[2]/li[1]/span[2]/text()').extract_first())
        # 楼层级别
        result["room_type"] = handlefont(text, response.xpath('//div[@class="general-item general-situation"]/div/ul[1]/li[2]/span[2]/text()').extract_first())
        # 房屋分布
        result["size"] = handlefont(text, response.xpath('//div[@class="general-item general-situation"]/div/ul[1]/li[3]/span[2]/text()').extract_first()).replace('㎡', '')
        # 房屋面积
        result["orientation"] = handlefont(text, response.xpath('//div[@class="general-item general-situation"]/div/ul[1]/li[4]/span[2]/text()').extract_first())
        # 房屋朝向
        result['is_first_hand'] = handlefont(text, response.xpath('//div[@class="general-item general-situation"]/div/ul[1]/li[5]/span[2]/text()').extract_first())
        # 几手房源
        result['renovation'] = handlefont(text, response.xpath('//div[@class="general-item general-situation"]/div/ul[2]/li[2]/span[2]/text()').extract_first())
        # 装修程度
        result['property_years'] = handlefont(text, response.xpath('//div[@class="general-item general-situation"]/div/ul[2]/li[3]/span[2]/text()').extract_first())
        if result['property_years'] != None:
            result['property_years'] = result['property_years'].replace("年产权", "")
        # 产权年限
        result['buiding_years'] = handlefont(text, response.xpath('//div[@class="general-item general-situation"]/div/ul[2]/li[4]/span[2]/text()').extract_first())
        if result['buiding_years'] != None:
            result['buiding_years'] = result['buiding_years'].replace("年", "")
        # 建筑时间
        result['advantage'] = handlefont(text, "\n".join(response.xpath('//div[@id="generalDesc"]/div/div[1]/p//text()').extract()))
        # 优点
        result['master'] = handlefont(text, "\n".join(response.xpath('//div[@id="generalDesc"]/div/div[2]/p//text()').extract()))
        # 房主
        result['house_type'] = handlefont(text, response.xpath('//div[@id="generalExpense"]/div/ul[1]/li[2]/span[2]/text()').extract_first())
        # 房屋类型
        result['ownership'] = handlefont(text, response.xpath('//div[@id="generalExpense"]/div/ul[1]/li[3]/span[2]/text()').extract_first())
        # 交易权属
        result['downpayment'] = handlefont(text, response.xpath('//div[@id="generalExpense"]/div/ul[2]/li[1]/span[2]/text()').extract_first()).replace(" ", "").replace("\n", "")

        return result

    except Exception as e:
        _ = e



if __name__ == '__main__':
    pass