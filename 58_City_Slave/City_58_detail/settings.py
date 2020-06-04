# -*- coding: utf-8 -*-

# Scrapy settings for City_58_detail project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'City_58_detail'

SPIDER_MODULES = ['City_58_detail.spiders']
NEWSPIDER_MODULE = 'City_58_detail.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'City_58_detail (+http://www.yourdomain.com)'

# Obey robots.txt rules
# 关闭robots规范的遵循
ROBOTSTXT_OBEY = False
# 关闭重定向
REDIRECT_ENABLED = False


# 下载超时时间
DOWNLOAD_TIMEOUT = 15
# 设置下载重试次数
RETRY_TIMES = 2
# 是否启动重试
RETRY_ENABLED = True

DOWNLOAD_DELAY = 50
# 下载页面的等待时间

RANDOMIZE_DOWNLOAD_DELAY = False
# 是否随机delay
CONCURRENT_REQUESTS_PER_IP = 5
# 同一个网站的并发量



# 使用scrapy_redis相关配置
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'   # 使用优先级队列进行采集
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 300,
    'City_58_detail.pipelines.MysqlTwistedPipline': 290,
}


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'City_58_detail.middlewares.City58DetailSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'City_58_detail.middlewares.RandomUserAgentMiddlware': 490,
    # 'City_58_detail.middlewares.RandomProxyMiddleware': 500,
   'City_58_detail.middlewares.DownloadRetryMiddleware': 510,

}
# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'City_58_detail.pipelines.City58DetailPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# redis相关配置信息
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = 'qq1362441'

# mysql相关配置信息
MYSQL_HOST = "182.92.122.154"
MYSQL_DBNAME = "luoxuanhao"
MYSQL_USER = "luoxuanhao"
MYSQL_PASSWORD = "luoxuanhao123"

