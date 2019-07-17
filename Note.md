[TOC]

# 踩坑记录
## requests-请求接口长时间未响应
- 原因：默认request访问一个请求会一直等待下去
- 解决：设置timeout和max_retries

## bs4-获取到的内容乱码
- 原因：bs输出时默认以`UTF-8`编码
- 解决：通过浏览器控制台查看网页所使用的编码，并通过`response.enconding='指定编码'`设置

## 文件写入乱码
- 原因：文件写入时，windows打开文件默认以“gbk“编码的，造成不识别unicode字符
- 解决：打开文件时加参数`encoding='utf-8'`，例：
`f = open('./source/斗破苍穹.txt','a+',encoding='utf-8')`

## 递归函数报错
- 原因：python递归默认最大深度为997,超过则会报错
- 解决：通过`sys.setrecursionlimit`设置递归最大深度，如`sys.setrecursionlimit(10000)`
- 注意，即使设的递归深度再大，也会受限于计算机本身的计算能力、系统版本、python版本等

# 数据存储

# 克制反爬
- 通过`header`伪装浏览器访问
- 设置随机等待时间
- IP池

# 性能提升
- 协程
- 多进程
- 分布式

# 待解决的问题
- 如果爬虫中途出错，从断点处继续下载