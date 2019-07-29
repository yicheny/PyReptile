from PyReptile.common.utils import get_page
from pyquery import PyQuery as pq
import re

def get_pansoso_info():
    res = pq(get_page('http://www.pansoso.com/zh/hello'))
    item_list = res('div#content>div.pss')
    for item in item_list.items():
        tits = item('h2>a')
        des = item('div.des').text().split(',')

        info = {
            'tit': tits.text(),
            'url': tits.attr("href"),
            'fileName': des[0],
            'fileSize': des[1],
            'sharer': des[2],
            'shareDate': des[3],
            'browerCount': des[4],
        }
        print(info)


if __name__ == '__main__':
    get_pansoso_info()