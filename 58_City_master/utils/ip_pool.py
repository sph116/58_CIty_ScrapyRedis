import requests
import redis
import settings
import time
import json

class ip_pool():
    def __init__(self, ip_nums, sleep_time):
        self.ip_nums = ip_nums
        self.ip_url = settings.IP_POOL_API.format(ip_num=ip_nums)
        self.sleep_time = sleep_time
        self.rd = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, password=settings.REDIS_PASSWORD, decode_responses=True)

    def keep_ip_pool(self):
        """
        维持ip池
        :return:
        """
        while 1:
            ip_ls = self.get_ip_list()

            print(f"======ip_pool更新======{ip_ls}")
            for ip in ip_ls:
                self.rd.sadd('ip_pool', ip)   # 将代理写入redis
            time.sleep(self.sleep_time)
            for ip in ip_ls:                  # 休眠完成后 删除ip重新写入
                self.rd.srem('ip_pool', ip)



    def get_ip_list(self):
        """
        从代理接口获得ip 并入库
        :return:
        """
        ip_ls = requests.get(self.ip_url).text
        ip_item = json.loads(ip_ls)['obj']

        return ["https://{}:{}".format(i["ip"], i["port"]) for i in ip_item]


Ip_pool = ip_pool(ip_nums=30, sleep_time=30)
Ip_pool.keep_ip_pool()





