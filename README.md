# 58_CIty_ScrapyRedis
使用scrapy_redis

#前言
  使用scrapy_redis部署 主从式分布式爬虫 抓取58同城房产数据。
  破解58同城页面字体文件反爬。
  主机 使用单线程维护代理池, 存储redis


# 文件结构  
58_City_Slave 从机采集程序  
58_City_master 主机采集程序  

# 配置文件
1.主机配置  
  # redis相关配置信息  
  REDIS_HOST = 'localhost'  
  REDIS_PORT = 6379  
  REDIS_PASSWORD = 'qq1362441'  

  # mysql相关配置信息  
  MYSQL_HOST = "182.92.122.154"  
  MYSQL_DBNAME = "luoxuanhao"  
  MYSQL_USER = "luoxuanhao"  
  MYSQL_PASSWORD = "luoxuanhao123"  
  
  # 代理池相关配置  
  IP_POOL_API = ''   # 原项目使用熊猫代理 需将url中count字段值修改为 count={ip_num}  
  
 2.从机同上  
 
 
