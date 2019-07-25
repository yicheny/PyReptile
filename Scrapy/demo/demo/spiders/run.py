import os

if __name__ == '__main__':
    # os.system('scrapy crawl quotes')
    # scrapy支持输出为csv,xml,pickle,json等，还支持ftp等远程输出
    os.system('scrapy crawl quotes -o quotes.json')
    # os.system('scrapy crawl quotes -o quotes.csv')
    # os.system('scrapy crawl quotes -o quotes.xml')
