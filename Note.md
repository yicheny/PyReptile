[TOC]

# 踩坑记录
## requests-请求接口长时间未响应
- 原因：默认request访问一个请求会一直等待下去
- 解决：设置timeout和max_retries

## bs4-获取到的内容乱码
- 原因：bs输出时默认以`UTF-8`编码
- 解决：通过浏览器控制台查看网页所使用的编码，并通过`response.enconding='指定编码'`设置