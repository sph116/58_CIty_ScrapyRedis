from City_58.utils.common import get_md5, handlefont
import requests
import re
from scrapy.http import Request

def parse_xiaoqu_detail_page(response):
    """
    解析小区详情页
    """
    result = dict()
    try:
        result['id'] = get_md5(response.url)
        result['name'] = response.css('.title-bar > span.title::text').extract_first()
        # 小区名称
        result['location'] = response.css('.title-bar > span.addr::text').extract_first()
        # 小区地址
        result['business_location'] = ",".join(response.xpath('//table[@class="info-tb"]//tr[1]/td[2]/a/text()').extract())
        # 商圈位置
        result['detail_location'] = response.xpath('//table[@class="info-tb"]//tr[1]/td[4]/text()').extract_first().replace("\n", '').replace(' ', '')
        # 小区具体位置
        result['building_type'] = response.xpath('//table[@class="info-tb"]//tr[2]/td[2]/@title').extract_first()
        # 建筑类型
        result['households'] = response.xpath('//table[@class="info-tb"]//tr[2]/td[4]/text()').re_first('\d+')
        # 现存用户
        result['price'] = response.css('.price-container > span.price::text').extract_first(0)
        # 价格 /平米
        result['building_age'] = response.xpath('//table[@class="info-tb"]/tr[5]/td[2]/@title').re_first('\d+')
        # 建筑年限
        result['plot_ratio'] = response.xpath('//table[@class="info-tb"]/tr[4]/td[4]/@title').extract_first(0)
        if result['plot_ratio'] == '':
            result['plot_ratio'] = None
        # 容积率
        result['buiding_area'] = response.xpath('//table[@class="info-tb"]/tr[6]/td[2]/@title').extract_first(0)
        # 建筑面积
        result['Parking_space'] = response.xpath('//table[@class="info-tb"]/tr[6]/td[4]/@title').re_first('\d+')
        # 停车位数量
        result['present_sale_rooms'] = response.css('tr[class="tb-btm"]').css('td:nth-child(2) > a > span::text').re_first('\d+')
        # 在售数量
        result['present_zu_rooms'] = response.css('tr[class="tb-btm"]').css('td:nth-child(4) > a > span::text').re_first('\d+')
        # 在租数量
        result['Property_right_type'] = response.xpath('//table[@class="info-tb"]/tr[3]/td[2]/@title').extract_first()
        # 产权类型
        result['Afforestation_rate'] = response.xpath('//table[@class="info-tb"]/tr[5]/td[4]/@title').re_first('\d+')
        # 绿化率
        result['Developers'] = response.xpath('//table[@class="info-tb"]/tr[8]/td[2]/@title').extract_first()
        # 开发商
        result['introduce'] = response.xpath('//div[@class="detail-mod desc-mod"]/p/text()').extract_first()


        return result
    except Exception as e:
        _ = e


if __name__ == '__main__':
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}
    response = Request("https://cs.58.com/xiaoqu/baolilugulinyu", callback=parse_xiaoqu_detail_page)