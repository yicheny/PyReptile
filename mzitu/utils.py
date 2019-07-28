IMAGE_FILE_NAME = 'images' #保存图片的文件夹名称

import requests,os,re
from requests.adapters import HTTPAdapter

s = requests.Session()
s.mount('http://',HTTPAdapter(max_retries=5))
s.mount('https://',HTTPAdapter(max_retries=5))

base_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
}

def get_page(url,options={},type='text'):
    headers = dict(base_headers, **options)
    print('正在抓取...', url)
    try:
        response = s.get(url,headers=headers,timeout=10)
        print('抓取成功', url, response.status_code)
        if response.status_code == 200:
            if type=='content':
                return response.content
            else:
                return response.text
    except Exception:
        print('抓取失败', url)
        return None

'''
@params
file_name:保存图片的总目录
path:图片的url路径
referer:引入页——用于设置headers,没有这一项会报403错误
tit:用于目录的中文标题
'''
def save_images(file_name=IMAGE_FILE_NAME,path='/',referer='/',tit=''):
    img_name =  path.split('/')[-1] #用于保存的图片名称
    menu_name = re.search('https://www.mzitu.com/\d+',referer).group().split('/')[-1] #保存的图片子目录——方便管理和查看,这里需要更灵活一些，或者直接作为参数传入

    cwd = os.getcwd()
    menu_path = '%s\%s\%s-%s'%(cwd,file_name,menu_name,tit)
    print(menu_path)
    if not os.path.exists(menu_path):
        os.mkdir(menu_path)

    options = {
        'Referer':referer
    }
    res = get_page(path,options=options,type='content')
    try:
        save_path = ('%s\%s' % (menu_path, img_name))
        with open(save_path, 'wb') as f:
            f.write(res)
    except Exception as e:
        print('Error',e.args,'报错页面 %s' % (referer))

if __name__ == "__main__":
    save_images()