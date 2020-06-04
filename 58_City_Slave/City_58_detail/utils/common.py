import re
import base64
import hashlib
from io import BytesIO
from fontTools.ttLib import TTFont


def get_md5(url):
    # 转化为md5
    if isinstance(url, str):
        url = url.encode('utf-8')
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()


def handlefont(page_source, prase_string):
    """
    处理字体
    """
    base64_str = re.findall("charset=utf-8;base64,(.*?)'\)", page_source)[0]
    font = TTFont(BytesIO(base64.decodebytes(base64_str.encode())))
    cmap_ = font['cmap'].tables[0].ttFont.tables['cmap'].tables[0].cmap
    handled_string = []
    try:
        for char_ in prase_string:
            decode_num = ord(char_)
            if decode_num in cmap_:
                num = cmap_[decode_num]
                num = int(num[-2:]) - 1
                handled_string.append(str(num))
            else:
                handled_string.append(char_)
        return ''.join(handled_string)
    except Exception as e:
        _ = e