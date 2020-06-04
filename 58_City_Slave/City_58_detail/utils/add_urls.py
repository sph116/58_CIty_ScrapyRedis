import redis
import json

rd = redis.Redis("127.0.0.1", password='qq1362441', decode_responses=True)
rd.lpush('city_58_detail:start_urls', "https://cs.58.com/zufang/41526823072406x.shtml")

urls = [("https://cs.58.com/zufang/34646960631231x.shtml", 8, "parse_chuzu_detail"),
        ("https://cs.58.com/ershoufang/41617717835278x.shtml", 8, "parse_sel_datail"),
        ("https://cs.58.com/ershoufang/41648810074373x.shtml", 8, "parse_sel_datail"),
        ("https://cs.58.com/ershoufang/41571418805278x.shtml", 8, "parse_sel_datail"),
        ("https://cs.58.com/ershoufang/40243816258591x.shtml", 8, "parse_sel_datail"),
        ("https://cs.58.com/ershoufang/41473078050575x.shtml", 8, "parse_sel_datail"),
        ("https://cs.58.com/ershoufang/41659754938664x.shtml", 8, "parse_sel_datail"),
        ("https://cs.58.com/ershoufang/41580810496034x.shtml", 8, "parse_sel_datail"),
        ("https://cs.58.com/ershoufang/41506727087361x.shtml", 8, "parse_sel_datail"),
        ("https://cs.58.com/ershoufang/40617494681229x.shtml", 8, "parse_sel_datail"),
        ("https://cs.58.com/ershoufang/41645846844293x.shtml", 8, "parse_sel_datail")
        ]
# urls = [("https://cs.58.com/ershoufang/41384179727641x.shtml", 8, "parse_sel_datail")]
for url in urls:
    rd.rpush("city_58_detail:new_urls", json.dumps(url))

