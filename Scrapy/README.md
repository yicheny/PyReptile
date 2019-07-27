[TOC]

# 安装
1. 先安装[Twisted](http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted),下载文件后执行:

`pip install G:\2019\pyCharmProject\Twisted-19.2.1-cp36-cp36m-win_amd64.whl` 
> 注意：一定要将路径带上去

2. 执行`pip install scrapy`

# 指令
- 创建项目:`scrapy startproject 项目名称`,然后切换到刚刚创建的目录下
    - 创建Spider:`scrapy genspider 文件名称 网站域名`
    - 创建CrawlSpider:`scrapy genspider -t crawl 文件名称 网站域名`