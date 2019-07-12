import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
res = requests.get('http://www.dilidili.name/anime/201904/',headers=headers)

try:
    soup = BeautifulSoup(res.text,'html.parser')
    titList = soup.select('div.anime_list > dl > dd > h3 > a')
    for v in titList:
        print(v.get_text())
except ConnectionError:
    print('拒绝连接')

# 注
